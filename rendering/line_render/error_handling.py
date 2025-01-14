"""
import code
code.interact(local=dict(globals(), **locals()))
"""

AREA_THRESH = 1e-10

def has_2d_area(shape):

    if any([shape.is_empty, shape.area<AREA_THRESH]):
        return False

    return True
