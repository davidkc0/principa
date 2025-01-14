import numpy as np

from plottermagic.geometry import geom2d

def parallel_line_overlay(origin, corner, density=None,  spacing=None):
    """
    Given a rectange, this shades it end to end in such a way that all the lines can be
    rotated about the center and it will still cover the entire rectange.
    (basically youll need to mask these lines afterwards.)
    Density controls how many lines there are in the y direction.
    Returns
    - lines
    - line_spacing which is a vector that goes from the start of one line to the next one.
    """

    if density is None and spacing is None:
        raise Exception("Either density or spacing needs to be given")

    orgin = np.array(origin)
    corner = np.array(corner)
    radius = np.linalg.norm(np.array(corner) - np.array(origin))/2
    center = (origin+corner)/2

    if spacing is None:
        y_coord = np.linspace(center[1] - radius, center[1] + radius, density)
    else:
        y_coord = np.arange(center[1] - radius, center[1] + radius, spacing)

    lines = []
    alternate = False
    for y in y_coord:
        if alternate:
            lines.append([(center[0]+radius, y), (center[0] - radius, y)])
        else:
            lines.append([(center[0] - radius, y), (center[0]+radius, y)])

        alternate = not alternate

    return lines


def grid_overlay(origin, corner, density=None, spacing=None):

    orgin = np.array(origin)
    corner = np.array(corner)

    lines = parallel_line_overlay(origin, corner, density, spacing)

    center = (origin+corner)/2

    pts, ind = geom2d.lines_to_matrix(lines)

    rot_mat = geom2d.rot_about_pt(center, 90, degrees=True)
    rot = np.matmul(rot_mat, pts.transpose()).transpose()
    rotated_lines = geom2d.matrix_to_lines(rot, ind)

    return lines + rotated_lines
