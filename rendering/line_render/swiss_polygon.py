from plottermagic.line_render import renderable, line, container, error_handling
from plottermagic.geometry import geom3d, shapes

import numpy as np

from shapely import geometry
from shapely.geometry import Polygon as ShapePoly
from shapely.geometry import LineString
from shapely.geometry import GeometryCollection


class SwissPolygon(renderable.Renderable):

    def __init__(self, points, tag='black', texture=None, draw_boundary = False, holes = None, **kwargs):

        self.d = 2
        self.tag = tag

        stacked = np.stack([geom3d.hpt(p) for p in points])
        if np.any(stacked[-1] != stacked[0]):
            stacked = np.vstack([stacked, stacked[0]])
        self.pts = stacked

        if holes is not None:
            h = []
            for hole in holes:
                stacked = np.stack([geom3d.hpt(p) for p in hole])
                if np.any(stacked[-1] != stacked[0]):
                    stacked = np.vstack([stacked, stacked[0]])
                h.append(stacked)
            self.holes = h
        else:
            self.holes = []

        self.texture = container.Container(texture)
        if draw_boundary:
            self.texture.append(line.Line(self.pts, tag))
            for hole in self.holes:
                self.texture.append(line.Line(hole, tag))

    def _z(self, pts=None):
        if pts is None:
            pts = self.pts
        return pts[:, -1][:,np.newaxis]

    def _transform(self, transform, renormalize=False):
        pts = self.pts.copy()
        pts = np.matmul(pts, transform)
        if renormalize:
            pts = pts/self._z(pts)

        new_holes = []
        for hole in self.holes:
            h = np.matmul(hole, transform)
            if renormalize:
                h = h/self._z(h)
            new_holes.append(h)
        texture = self.texture._transform(transform, renormalize)
        # dont need to draw boundary again since this happened in the original constructor
        return SwissPolygon(pts, tag=self.tag, texture=texture, draw_boundary = False, holes = new_holes)

    def to_2d(self):
        return self.texture.to_2d()

    def to_2d_shapely(self):
        pts = self.pts.copy()
        pts = pts/self._z()
        if np.any(np.isnan(pts)):
            return GeometryCollection()
        s = ShapePoly([(p[0], p[1]) for p in pts], holes = [h[:, 0:-1] for h in self.holes])
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
        if shape.symmetric_difference(self.to_2d_shapely()).is_empty:
            return SwissPolygon(self.pts, tag=self.tag, texture=self.texture, draw_boundary = False, holes=self.holes)
        pts = np.array(shape.exterior.xy).transpose()
        pts = self.append_z_to_xy(pts)
        # uhhhh idk what to do here
        return SwissPolygon(pts, tag=self.tag, texture=self.texture, draw_boundary = False, holes=self.holes)

    def clip_items(self):
        new_texture = self.texture.clip_to_shape(self.to_2d_shapely())
        return SwissPolygon(self.pts, tag=self.tag, texture=new_texture, draw_boundary = False, holes=self.holes)

    def copy(self, shallow):
        return SwissPolygon(self.pts, tag=self.tag, texture=self.texture.copy(shallow), draw_boundary = False, holes=self.holes)

    def snap_to_grid(self, decimals=6):
        pts = np.around(self.pts, decimals=decimals)
        holes = [np.around(h, decimals=decimals) for h in self.holes]
        return SwissPolygon(pts, tag=self.tag, texture=self.texture.snap_to_grid(decimals), draw_boundary = False, holes = holes)
