from plottermagic.line_render import polyhedron, polygon, line
from plottermagic.geometry import geom3d
import numpy as np
import itertools


class HoveringSquares(polyhedron.Polyhedron):
    def __init__(self, n_segments, colors, tag='black', draw_boundary=False, params=None):

        if params is None:
            params = {}
        params['wireframe'] = True

        if isinstance(colors, str) or not hasattr(colors, "__iter__"):
            colors = [colors]

        lines = []
        for y, color in zip(np.linspace(0, 1, n_segments), itertools.cycle(colors)):
            lines.append(line.Line([(0, y), (1,y)], tag=color))

        base_pts = [(0,0,0),(0,1,0),(1,1,0),(1,0,0)]

        def make_base():
            return polygon.Polygon(base_pts, draw_boundary=draw_boundary, tag=tag, texture=lines)

        front = make_base()
        back = front.transform(geom3d.translate((0,0,1)))

        left = make_base().transform(np.matmul(geom3d.translate((1,0,1)), geom3d.rotate_y(90, degrees=True)))
        right = left.transform(geom3d.translate((-1,0,0)))

        faces = [front, back, left, right]

        super().__init__(faces, params=params)
