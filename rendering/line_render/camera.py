from plottermagic.geometry import geom3d
from scipy.special import cotdg

import numpy as np

def make_viewport_matrix(corner=(0,0,0), side_lengths = (100,100,1)):
    y_ref = geom3d.reflect_axis(1)
    scale = geom3d.diag_scale(side_lengths[0]/2, side_lengths[1]/2, side_lengths[2])
    trans = geom3d.translate((corner[0]+side_lengths[0]/2, corner[1]+side_lengths[1]/2, corner[2]))
    f = np.linalg.multi_dot([trans, scale, y_ref])
    return f

class Camera:
    def __init__(self, position, at, up, aspect, near, far, field_of_view):
        self.pos = geom3d.pt(position)
        self.at = geom3d.pt(at)
        self.up = geom3d.pt(up)

        self.aspect = aspect
        self.near = near
        self.far = far
        self.fov = field_of_view

    def get_view_matrix(self):

        z = self.pos-self.at
        z = z/np.maximum(np.linalg.norm(z), 1e-10)

        x = np.cross(self.up, z)
        x = x/np.maximum(np.linalg.norm(x), 1e-10)

        y = np.cross(z, x)

        t = geom3d.translate(-self.pos)
        rot = np.eye(4)
        rot[0:3, 0:3] = np.stack([x, y, z])
        return np.matmul(rot, t)

    def get_pers_proj_matrix(self):
        proj = np.eye(4)
        proj = np.eye(4)
        proj[3, 3] = 0
        proj[3, 2] = -1
        proj[0,0] = cotdg(self.fov/2)/self.aspect
        proj[1, 1] = cotdg(self.fov/2)
        proj[2, 2] = -(self.far+self.near)/(self.far-self.near)
        proj[2, 3] = -2*self.near*self.far/(self.far-self.near)
        return proj

class DefaultCamera(Camera):
    def __init__(self, **kwargs):
        position = kwargs.get('position', (0, 0, -1))
        at = kwargs.get('at', (0, 0, 0))
        # normally cameras invert images, and this is annoying af
        up = kwargs.get('up', (0, 1, 0))
        aspect = kwargs.get('aspect', 1)
        near = kwargs.get('near', 5)
        far = kwargs.get('far', 10)
        field_of_view = kwargs.get('field_of_view', 90)

        if 'direction' in kwargs:
            raise Exception('uhhh this is old code from when the camera logic was broken. Use at!')

        super().__init__(position, at, up, aspect, near, far, field_of_view)
