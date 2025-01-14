from plottermagic.geometry import geom3d
from plottermagic.line_render import renderable
import numpy as np

class Points(renderable.Renderable):
    def __init__(self, points, tag='black'):
        self.d = 0
        if isinstance(points, np.ndarray) and points.shape[1] == 4:
            self.pts = points
        else:
            self.pts = np.stack([geom3d.hpt(p) for p in points])

        self.tag = tag

    def _transform(self, transform, renormalize=False):
        pts = self.pts.copy()
        pts = np.matmul(pts, transform)
        if renormalize:
            pts = pts/pts[:, -1][:,np.newaxis]
        return Points(pts, self.tag)

    def to_2d(self):
        pts = self.pts.copy()
        pts = pts/pts[:, -1][:,np.newaxis]
        return renderable.TaggedRenderObject(self.tag, points=pts[:, 0:2])
