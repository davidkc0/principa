from plottermagic.line_render import polyhedron, polygon
from plottermagic.geometry import geom3d

import numpy as np


class UnitCube(polyhedron.Polyhedron):
    def __init__(self, tag='black', face_texture=None, draw_boundary = False, params=None):

        base_pts = [(0,0,0),(0,1,0),(1,1,0),(1,0,0)]

        def make_base(base_tag):
            return polygon.Polygon(base_pts, draw_boundary=draw_boundary, tag=base_tag, texture=face_texture)
        """

        l_pts = front.transform(geom3d.rotate_y(90, degrees=True)).pts
        left = polygon.Polygon(l_pts, draw_boundary=True, tag='blue')
        right = left.transform(geom3d.translate((1,0,0)))

        t_pts = front.transform(geom3d.rotate_x(-90, degrees=True)).pts
        top = polygon.Polygon(t_pts, draw_boundary=True, tag='green')
        bot = top.transform(geom3d.translate((0,1,0)))
        """

        fb_tag = 'red' if tag=='rainbow' else tag
        front = make_base(fb_tag)
        back = front.transform(geom3d.translate((0,0,-1)))

        lr_tag = 'blue' if tag=='rainbow' else tag
        right = make_base(lr_tag).transform(geom3d.rotate_y(90, degrees=True))
        left = right.transform(geom3d.translate((1,0,0)))

        tb_tag = 'green' if tag=='rainbow' else tag
        top = make_base(tb_tag).transform(geom3d.rotate_x(-90, degrees=True))
        bot = top.transform(geom3d.translate((0,1,0)))

        faces = [front, back, right, left, top, bot]
        super().__init__(faces, params=params)
