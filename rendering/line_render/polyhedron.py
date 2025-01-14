from plottermagic.line_render import renderable, container, occlusion, error_handling
from shapely.ops import cascaded_union
from shapely.geometry import Point
from shapely.geometry.collection import GeometryCollection
from shapely.geometry import base

class Polyhedron(renderable.Renderable):
    def __init__(self, faces, params = None):
        """
        params -
            wireframe (bool), should this run internal occulusion algo?
            _inter_occ_ran - internal variable to keep track of if we need to do occulusion

        """
        self.d = 3
        self.faces = container.Container(faces)

        if params is None:
            self.params = {}
        else:
            self.params = params

    def _face_shapes(self):
        if not hasattr(self, 'face_shapes'):
            self.face_shapes = [f.to_2d_shapely() for f in self.faces.items]
        return self.face_shapes

    def _transform(self, transform, renormalize=False):
        return Polyhedron(self.faces._transform(transform, renormalize), params=self.params.copy())

    def to_2d_shapely(self):

        """
        #TEST
        shapes = [s.buffer(0) for s in shapes if s.is_valid]
        """
        face_shapes = []
        for face in self.faces.items:
            shape = face.to_2d_shapely()
            if error_handling.has_2d_area(shape):
                face_shapes.append(shape)

        if len(face_shapes) > 0:
            return cascaded_union(face_shapes)
        else:
            return GeometryCollection()

    def get_z_at_xy(self, pt):
        p = Point(pt)
        faces = [f for f,s in zip(self.faces.items, self._face_shapes()) if s.intersects(p)]
        if len(faces) == 0:
            raise Exception("!!!!")
        z = [f.get_z_at_xy(pt) for f in faces]
        return min(z)

    def reduce_shape(self, reduced_shape):

        """
        #TEST
        if reduced_shape.is_empty or reduced_shape.area<1e-10:
            return None
        """

        new_faces = []
        for face, shape in zip(self.faces.items, self._face_shapes()):

            """
            #TEST
            if not shape.is_valid:
                continue
            """

            fs_reduced = shape.intersection(reduced_shape)

            shapes = [fs_reduced]
            if isinstance(fs_reduced, base.BaseMultipartGeometry):
                shapes = [g for g in fs_reduced.geoms]

            for s in shapes:
                """
                #TEST
                valid_reduced = all([not s.is_empty, not isinstance(s, GeometryCollection), not s.area<1e-10])
                if valid_reduced:
                    reduced_face = face.reduce_shape(s)
                    if reduced_face is not None:
                        new_faces.append(reduced_face)
                """
                reduced_face = face.reduce_shape(s)
                if reduced_face is not None:
                    new_faces.append(reduced_face)
        return Polyhedron(new_faces, params=self.params.copy())

    def copy(self, shallow):
        return Polyhedron(self.faces.copy(shallow), params=self.params.copy())

    def get_pieces(self):
        if self.params.get('wireframe', False):
            for poly in self.faces.items:
                yield poly
        else:
            for poly in occlusion.get_occuluded_objs(self.faces.items):
                yield poly

    def to_2d(self):
        if self.params.get('wireframe', False):
            return self.faces.to_2d()
        else:
            return container.Container(occlusion.get_occuluded_objs(self.faces.items)).to_2d()

    def snap_to_grid(self, decimals=6):
        return Polyhedron([f.snap_to_grid(decimals) for f in self.faces.items], params=self.params)
