from plottermagic.line_render import polygon, line, container
from plottermagic.geometry import geom2d, geom3d, shapes

import numpy as np

"""
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
"""

"""
custom texture polygon to fill!
"""

"""
concentric - some shape that we stretch and fill
pattern texture -
"""

"""
class ConcentricMoire:

    def __init__(self, ...):
        MoireShape(transform(...))

    pass
"""

def make_concentric_circles(n_lines=10, n_sides=100, decimals=None, start_percent=0.01, rescale=1, color='black'):
    base_circle = shapes.regular_poly_points(n_sides, decimals=decimals)
    #close the loop!
    base_circle = np.vstack([base_circle, base_circle[0]])
    return make_concentric_pattern(base_circle, n_lines=n_lines, start_percent=start_percent, rescale=rescale, color=color, init_rot='cont')


def make_concentric_poly(n_lines=10, n_sides=4, decimals=None, start_percent=0.01, rescale=1, color='black'):
    base_shape = shapes.regular_poly_points(n_sides, decimals=decimals)
    #close the loop!
    base_shape = np.vstack([base_shape, base_shape[0]])
    return make_concentric_pattern(base_shape, n_lines=n_lines, start_percent=start_percent, rescale=rescale, color=color)

def make_concentric_pattern(verts, start_percent=0.01, end_percent=1, n_lines=10, rescale=1, color='black', init_rot=None):
    objs = []
    for r in np.linspace(start_percent, end_percent, n_lines):
        l = line.Line(rescale*r*verts, tag=color)

        if init_rot == 'cont':
            rand_rot = geom3d.rotate_z(np.random.randint(0, 360), degrees=True)
            l = l.transform(rand_rot)
        #TODO add lists for ordern N polygons.

        objs.append(l)

    return container.Container(objs)


def zxy_rot(x=0, y=0, z=0, degrees=True):
    transform = np.linalg.multi_dot([geom3d.rotate_z(z, degrees=degrees),
                                     geom3d.rotate_x(x, degrees=degrees),
                                     geom3d.rotate_y(y, degrees=degrees)])
    return transform


def circle_translations(r, n_pieces, offset_angle=0):
    transforms = []
    for i in range(n_pieces):
        rotation_angle = i*(360/n_pieces)+offset_angle
        translation = geom3d.translate((-r, 0, 0))
        rotation = geom3d.rotate_z(rotation_angle, degrees=True)
        transforms.append(np.linalg.multi_dot([rotation, translation]))

    return transforms


class MoireShape(polygon.Polygon):

    #def __init__(self, outline, texture, tag='black', transforms=None, rot_x=0, rot_y=0, rot_z=0):
    def __init__(self, outline, tag, texture_layers=None, draw_boundary=False):

        self.tag = tag
        self.pts = polygon.Polygon(outline).pts
        self.texture = container.Container([])

        if draw_boundary:
            self.texture.append(line.Line(self.pts, tag))

        if texture_layers is not None:
            shape = self.to_2d_shapely()
            for texture in texture_layers:
                for clipped in texture.clip_to_shape(shape).items:
                    self.texture.append(clipped)

"""
outline
texture layer - [unclipped base texture, color, texture transform]
common transforms
-


"""

"""
class MShape:
    def __init__(self, n_sides, scale = 1, n_lines = 5, fill_type='concentric', color='black', start_ratio=0.1, xy_rots=(0,0)):
        self.n_sides = n_sides
        self.n_lines = n_lines
        self.fill_type = fill_type
        self.color = color
        self.scale = scale
        self.start = start_ratio
        self.rots = xy_rots

    def make_shapes(self):

        objs = []
        self.unit_verts = shapes.regular_poly_points(self.n_sides, decimals=p.precision)

        if self.fill_type == 'concentric':
            for r in np.linspace(self.start, 1, self.n_lines):
                poly = polygon.Polygon(self.scale*r*self.unit_verts, tag=self.color, draw_boundary=True)

                t = np.linalg.multi_dot([geom3d.rotate_x(self.rots[0], degrees=True),
                                         geom3d.rotate_y(self.rots[1], degrees=True),
                                        geom3d.rotate_z(np.random.randint(0, 360), degrees=True)])

                poly = poly.transform(t)
                objs.append(poly)

        return objs


for i, ms in enumerate(mshapes):


    rotation_angle = i*(2*np.pi/n_shapes)

    translation = geom3d.translate((-p.sphere_radius, 0, 0))
    #translation = np.eye(4)
    rotation = geom3d.rotate_z(rotation_angle)
    #rotation = np.eye(4)


    a = np.random.randint(0, 360)
    print(a)

    transform = np.linalg.multi_dot([rotation, translation, geom3d.rotate_z(a, degrees=True)])
    #transform = np.linalg.multi_dot([translation, geom3d.rotate_z(a, degrees=True)])
    #transform = geom3d.rotate_z(a, degrees=True)
    #transform = np.eye(4)



    for s in ms.make_shapes():
        renderable_shapes.append(s.transform(transform))
"""
