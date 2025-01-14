import numpy as np
from shapely.geometry import base

class Renderable:

    def __init__(self, tag):
        self.tag = tag

    def transform(self, transform, renormalize=False):
        """
        The points are stored as rows, but column vectors are the way to go for matrix math.
        """
        return self._transform(transform.transpose(), renormalize)

    def _transform(self, transform, renormalize=False):
        raise Exception("Not implemented in base class")

    def to_2d(self):
        """
        Gets a (mpl) usable object for graphing.
        """
        raise Exception("Not implemented in base class")

    def to_2d_shapely(self):
        raise Exception("Not implemented in base class")

    def get_z_at_xy(self, pt):
        raise Exception("Not implemented in base class")

    def reduce_shape(self, shape):
        raise Exception("Not implemented in base class")

    def copy(self, shallow=False):
        raise Exception("Not implemented in base class")

    def get_pieces(self):
        yield self.copy(shallow=True)

    def clip_items(self):
        return self.copy(shallow=True)

    def snap_to_grid(self, decimals=6):
        raise Exception("Not implemented in base class")

class RenderDict:
    def __init__(self, tagged_render_objects):
        self.tagged_render_objects = tagged_render_objects

    def __getitem__(self, item):
        if item in self.tagged_render_objects:
            return self.tagged_render_objects[item]
        if item in ['points', 'lines']:
            if item == 'lines':
                out = []
                for tag, data_structures in self.tagged_render_objects.items():
                    if 'lines' in data_structures:
                        out += data_structures['lines']
            elif item == 'points':
                points = []
                for tag, data_structures in self.tagged_render_objects.items():
                    if 'points' in data_structures:
                        points.append(data_structures['points'])
                out = np.vstack(points)
            return out
        raise Exception('key error', item)


    def update(self, rd, inplace=False):

        tro = self.tagged_render_objects.copy()

        for tag, data_structure_values in rd.tagged_render_objects.items():

            if tag in tro:
                current = tro[tag]
                for data_name, data in data_structure_values.items():
                    if data_name not in current:
                        if data_name not in ['points', 'lines']:
                            raise Exception('invalid render item', data_name)
                        current[data_name] = data
                    else:
                        if data_name == 'points':
                            current[data_name] = np.vstack([current[data_name], data])
                        elif data_name == 'lines':
                            current[data_name] += data
                        else:
                            raise Exception('invalid render item', data_name)
            else:
                tro[tag] = data_structure_values

        if inplace:
            self.tagged_render_objects = tro
        else:
            return RenderDict(tro)

class TaggedRenderObject(RenderDict):
    def __init__(self, tag, points=None, lines=None):
        d = {}
        if points is not None:
            d['points'] = points
        if lines is not None:
            d['lines'] = lines
        super().__init__({tag:d})
