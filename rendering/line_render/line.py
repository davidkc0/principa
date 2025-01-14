from plottermagic.geometry import geom3d
from plottermagic.line_render import renderable, container

import numpy as np

from shapely import geometry
from shapely.geometry import LineString
from shapely.geometry import base
from shapely.geometry import GeometryCollection


class Line(renderable.Renderable):

    def __init__(self, points, tag='black'):
        self.d  = 1
        if isinstance(points, np.ndarray) and points.shape[1] == 4:
            self.pts = points
        else:
            self.pts = np.stack([geom3d.hpt(p) for p in points])

        self.tag = tag

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
        return Line(pts, self.tag)

    def to_2d(self):
        pts = self.pts.copy()
        pts = pts/self._z()

        lines = []
        for i, pt in enumerate(pts):
            if i != len(pts) - 1:
                x, y, _, _ = pt
                x1, y1, _, _ = pts[i+1]
                lines.append(((x, y), (x1, y1)))
        return renderable.TaggedRenderObject(self.tag, lines=lines)

    def to_2d_shapely(self):
        pts = self.pts.copy()
        pts = pts/self._z()
        if np.any(np.isnan(pts)):
            return GeometryCollection()
        return LineString([(p[0], p[1]) for p in pts])

    def get_z_at_xy(self, pt):

        pt2d = np.array(pt)
        z = []
        for i in range(len(self.pts) - 1):
            p1 = self.pts[i][0:2]
            p2 = self.pts[i+1][0:2]

            if np.all(np.isclose(pt2d, p1)):
                z.append(self.pts[i][2])
                continue

            vp = pt2d - p1
            vl = p2 - p1

            len_l = np.linalg.norm(vl)
            len_lp = np.linalg.norm(vp)
            w = len_lp/len_l

            same_dir = np.isclose(1, np.dot(vp, vl)/(len_l*len_lp))
            in_inter = w>=0 and w<=1
            if same_dir and in_inter:
                pt = self.pts[i]*(1-w) + self.pts[i+1]*w
                z.append(pt[2])
        if len(z) == 0:
            raise Exception("{} wasn't on any of the lines!".format(pt))
        return np.min(z)

    def reduce_shape(self, shape):
        """
        TODO this isn't really correct. This turning our 3d lines -> 2d line. If we try to have
        lines in a bounded big shape (like a polyhedron), then this will get reduced to 2d before it should be.
        """
        if shape.is_empty:
            return None
        return Line(np.array(shape.xy).transpose(), tag=self.tag)

    def copy(self, shallow=False):
        if shallow:
            return Line(self.pts, tag=self.tag)
        else:
            return Line(self.pts.copy(), tag=self.tag)

    def snap_to_grid(self, decimals=6):
        return Line(np.around(self.pts, decimals=6), tag=self.tag)


def lines_from_list(lines, tag):
    return [Line(l, tag=tag) for l in lines]
