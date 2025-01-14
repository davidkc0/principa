import functools

from plottermagic.line_render import camera, occlusion, renderable

def map_to_cam_space(objects, cam):
    view_mat = cam.get_view_matrix()
    return list(map(lambda o:o.transform(view_mat, renormalize=False), objects))

def map_to_proj_space(objects, cam):
    proj_matrix = cam.get_pers_proj_matrix()
    return list(map(lambda o:o.transform(proj_matrix, renormalize=True), objects))

def map_to_viewport(objects, corner, side_lengths):
    viewport_mat = camera.make_viewport_matrix(corner, side_lengths)
    return list(map(lambda o:o.transform(viewport_mat, renormalize=False), objects))

def get_2d(objects):
    if len(objects) == 0:
        return renderable.TaggedRenderObject('no objects found')
    tagged_objects = list(map(lambda o:o.to_2d(), objects))
    return functools.reduce(lambda a,b: a.update(b), tagged_objects)

def proj_via_cam(objects, cam):
    objects = map_to_cam_space(objects, cam)
    objects = map_to_proj_space(objects, cam)
    return objects

def get_viewport_objs(objects, cam, center = (0, 0, 0.5), dimensions = (10,10, 1)):
    objects = proj_via_cam(objects, cam)
    corner = (center[0] - dimensions[0]/2 , center[1] - dimensions[1]/2, center[2] - dimensions[2]/2)
    objects = map_to_viewport(objects, corner, dimensions)
    return objects

def render_no_clipping(objects, cam, center = (0, 0, 0.5), dimensions = (10,10, 1)):
    objects = proj_via_cam(objects, cam)
    corner = (center[0] - dimensions[0]/2 , center[1] - dimensions[1]/2, center[2] - dimensions[2]/2)
    objects = map_to_viewport(objects, corner, dimensions)
    return get_2d(objects)

def clip_obj_textures(objects):
    return list(map(lambda o:o.clip_items(), objects))

def end_this_unholy_floating_point_error_hell(objects):
    return list(map(lambda o:o.snap_to_grid(decimals=5), objects))

def render_occulsion(objects, cam, center = (0, 0, 0.5), dimensions = (10,10, 1)):
    objects = proj_via_cam(objects, cam)

    objects = end_this_unholy_floating_point_error_hell(objects)

    objects = occlusion.get_occuluded_objs(objects)
    objects = occlusion.get_occuluded_pieces(objects)
    objects = clip_obj_textures(objects)

    corner = (center[0] - dimensions[0]/2 , center[1] - dimensions[1]/2, center[2] - dimensions[2]/2)
    objects = map_to_viewport(objects, corner, dimensions)
    return get_2d(objects)
