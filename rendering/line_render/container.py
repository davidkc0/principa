from plottermagic.line_render import renderable

from shapely.geometry import base
import numpy as np

class Container(renderable.Renderable):
    def __init__(self, items):

        if items is None:
            self.items = []
        elif isinstance(items, Container):
            self.items = items.items
        elif isinstance(items, list):
            self.items = items
        else:
            self.items = [items]

    def append(self, object):
        self.items.append(object)

    def _transform(self, transform, renormalize=False):
        transformed = [i._transform(transform, renormalize) for i in self.items]
        return Container(transformed)

    def to_2d(self):
        rd = renderable.RenderDict({})
        for obj in self.items:
            rd = rd.update(obj.to_2d())
        return rd

    def clip_to_shape(self, shape):

        new_items = []
        for item in self.items:

            item_shape = item.to_2d_shapely()
            clipped = item_shape.intersection(shape.buffer(0.001))
            if clipped.is_empty:
                continue

            if isinstance(clipped, base.BaseMultipartGeometry):
                shapes = [g for g in clipped.geoms]
            else:
                shapes = [clipped]

            for s in shapes:
                new_item = item.reduce_shape(s)
                if new_item is not None:
                    new_items.append(new_item)

        return Container(new_items)

    def copy(self, shallow=False):
        return Container([i.copy(shallow) for i in self.items])

    def snap_to_grid(self, decimals=6):
        return Container([i.snap_to_grid(decimals) for i in self.items])
