from plottermagic.line_render import renderable, line, container, error_handling
from plottermagic.geometry import geom2d, geom3d, shapes
from plottermagic.shading import simple_shapes, grid

import numpy as np

from shapely import geometry
from shapely.geometry import Polygon as ShapePoly
from shapely.geometry import LineString
from shapely.geometry import GeometryCollection


def reg_polygon(order, decimals=None, **kwargs):
    pts = shapes.regular_poly_points(order, decimals)
    return Polygon(pts, **kwargs)

class Polygon(renderable.Renderable):

    def __init__(self, points, tag='black', texture=None, draw_boundary = False, **kwargs):

        self.d = 2
        self.tag = tag

        stacked = np.stack([geom3d.hpt(p) for p in points])
        if np.any(stacked[-1] != stacked[0]):
            stacked = np.vstack([stacked, stacked[0]])
        self.pts = stacked

        self.texture = container.Container(texture)
        if draw_boundary:
            self.texture.append(line.Line(self.pts, tag))

    def _z(self, pts=None):
        if pts is None:
            pts = self.pts
        #return np.maximum(pts[:, -1][:,np.newaxis], 1e-5)
        return pts[:, -1][:,np.newaxis]

    def _transform(self, transform, renormalize=False):
        pts = self.pts.copy()
        pts = np.matmul(pts, transform)
        if renormalize:
            pts = pts/self._z(pts)
        texture = self.texture._transform(transform, renormalize)
        # dont need to draw boundary again since this happened in the original constructor
        return Polygon(pts, tag=self.tag, texture=texture, draw_boundary = False)

    def to_2d(self):
        return self.texture.to_2d()

    def to_2d_shapely(self):
        pts = self.pts.copy()
        pts = pts/self._z()

        if np.any(np.isnan(pts)):
            return GeometryCollection()

        s = ShapePoly([(p[0], p[1]) for p in pts])

        if not s.is_valid:
            s = s.buffer(0)

        return s

    def _find_plane_inverse(self):
        if not hasattr(self, '_inv'):
            xy = np.hstack([self.pts[:, 0:2], np.ones((len(self.pts), 1))])
            z = self.pts[:, 2]
            self._inv, _, self._inv_rank, self._inv_sing = np.linalg.lstsq(xy, z, rcond=None)

    def get_z_at_xy(self, pt):
        self._find_plane_inverse()
        return np.dot(self._inv, np.array([pt[0], pt[1], 1]))

    def append_z_to_xy(self, pts):
        self._find_plane_inverse()
        z =  np.dot(self._inv, np.vstack([pts.transpose(), np.ones(len(pts))]))
        return np.hstack([pts, z.reshape(-1,1)])

    def reduce_shape(self, shape):
        if not error_handling.has_2d_area(shape):
            return None

        """
        #TEST
        if not shape.is_valid:
            shape = shape.buffer(0)
        """

        if shape.symmetric_difference(self.to_2d_shapely()).is_empty:
            return Polygon(self.pts, tag=self.tag, texture=self.texture, draw_boundary = False)

        pts = np.array(shape.exterior.xy).transpose()
        """
        we don't want this to get flatted downed to a 2d polygon, since reduce_shape
        ends up getting called multiple times when you try to occulde polyhedrons.
        """
        pts = self.append_z_to_xy(pts)
        return Polygon(pts, tag=self.tag, texture=self.texture, draw_boundary = False)

    def clip_items(self):
        new_texture = self.texture.clip_to_shape(self.to_2d_shapely())
        return Polygon(self.pts, tag=self.tag, texture=new_texture, draw_boundary = False)

    def copy(self, shallow):
        pts = self.pts
        return Polygon(pts, tag=self.tag, texture=self.texture.copy(shallow), draw_boundary = False)

    def snap_to_grid(self, decimals=6):
        return Polygon(np.around(self.pts, decimals=decimals), tag=self.tag, texture=self.texture.snap_to_grid(decimals), draw_boundary = False)

    def add_shading(self, args, num_lines = 10, kind='concentric', color='black', degrees=False):
        lines = []

        #Assumes it is centered around the origin!
        if kind == 'concentric':
            for s in np.linspace(args.get('starting_percent', 0.1), 1, num_lines):
                verts = s*self.pts[:, 0:3]
                r = np.linalg.norm(verts, axis=1)
                lines.append(line.Line(verts, tag=color))
        elif kind == 'parallel' or kind == 'grid':
            min_bb = np.min(self.pts[:, 0:2], axis=0)
            max_bb = np.max(self.pts[:, 0:2], axis=0)

            if kind == 'parallel':
                shading_lines = grid.parallel_line_overlay(min_bb, max_bb, density=num_lines)
            else:
                shading_lines = grid.grid_overlay(min_bb, max_bb, density=num_lines)

            if 'angle' in args:
                pts, ind = geom2d.lines_to_matrix(shading_lines)
                rot_mat = geom2d.rot(args['angle'], degrees=args.get('degrees', True))
                rot = np.matmul(rot_mat, pts.transpose()).transpose()
                shading_lines = geom2d.matrix_to_lines(rot, ind)

            clipped_lines = shapes.lines_in_polygon(shading_lines, self.pts[:, 0:2])
            lines += line.lines_from_list(clipped_lines, tag=color)

        elif kind == 'step_vert':
            sl = simple_shapes.step_and_shade_poly(self.pts, num_lines, random_start=args.get('random_start', True))
            lines += line.lines_from_list(sl, tag=color)

        elif kind == 'None':
            return self.copy()
        else:
            raise Exception('Unimplemented kind')

        return Polygon(self.pts, tag=self.tag, texture=self.texture.items + lines, draw_boundary = False)
