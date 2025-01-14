import numpy as np
from shapely.geometry import base

def get_occuluded_shapes(objects):
    shapes = [o.to_2d_shapely() for o in objects]

    for i in range(len(objects)):
        o1, s1 = objects[i], shapes[i]

        if s1.is_empty:
            continue

        for j in range(i+1, len(objects)):
            o2, s2 = objects[j], shapes[j]

            if s2.is_empty or not s1.intersects(s2):
                continue
            s1, s2 = simple_2obj_occulsions(s1, o1, s2, o2, check_valid = False)
            shapes[i] = s1
            shapes[j] = s2

    return shapes

"""
def invalid_shape(obj, shape):
    #maybe needs to be 1e-5
    thresh = 1e-10
    if obj.d == 2:
        return shape.area<thresh
    elif obj.d==1:
        return shape.length<thresh
    return False
"""

def simple_2obj_occulsions(s1, o1, s2, o2, check_valid = True):
    if check_valid:
        if np.any([s1.is_empty, s2.is_empty, not s1.intersects(s2)]):
            return s1, s2

    """
    #TEST
    if invalid_shape(o1, s1) or invalid_shape(o2, s2):
        return s1, s2
    """
    s1_keep = s1.difference(s2)
    s2_keep = s2.difference(s1)
    shape_intersection = s1.intersection(s2)

    """
    #TEST
    if shape_intersection.area<1e-10:
        return s1, s2
    """

    shapes_to_check = []

    if isinstance(shape_intersection, base.BaseMultipartGeometry):
        shapes_to_check = [g for g in shape_intersection.geoms]
    else:
        shapes_to_check = [shape_intersection]

    for shape in shapes_to_check:
        """
        This doesn't work in the case that two polygons actually intersect each other.
        To fix that you'd need something like

        if both polygons???:
            line_intersection = polygons[i].intersection(polygons[j])
            if line_intersection is not None:
                new_shapes = []
                for s in shapes_to_check:
                    new_shapes += ops.split(s, line_intersection)
        """

        """
        #TEST
        if shape.area<1e-10:
            continue
        """

        pt = shape.representative_point().xy
        #pt = shape.centroid.xy
        xy = (pt[0][0], pt[1][0])
        z1 = o1.get_z_at_xy(xy)
        z2 = o2.get_z_at_xy(xy)

        if z1<z2:
            s1_keep = s1_keep.union(shape)
        elif z2<z1:
            s2_keep = s2_keep.union(shape)
        else:
            # Right now lines might intersect with planes at points
            # randomly pick one so we don't draw two borders.
            if np.random.random()>0.5:
                s1_keep = s1_keep.union(shape)
            else:
                s2_keep = s2_keep.union(shape)

    """
    #TEST
    return s1_keep.simplify(1e-10), s2_keep.simplify(1e-10)
    """
    return s1_keep, s2_keep

def get_occuluded_pieces(objects):
    new_objs = []
    for obj in objects:
        for piece in obj.get_pieces():
            new_objs.append(piece)
    return new_objs

def get_occuluded_objs(objects):

    occluded_shapes = get_occuluded_shapes(objects)

    new_objects = []
    for new_shape, obj in zip(occluded_shapes, objects):

        """
        #TEST
        if not new_shape.is_valid:
            new_shape = new_shape.buffer(0)
        """

        if isinstance(new_shape, base.BaseMultipartGeometry):
            shape_list = [g for g in new_shape.geoms]
        else:
            shape_list = [new_shape]

        for s in shape_list:
            new_obj = obj.reduce_shape(s)
            if new_obj is not None:
                new_objects.append(new_obj)

    return new_objects
