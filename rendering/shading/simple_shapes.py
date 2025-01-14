import numpy as np
import logging

def shade_triangle(a, b, c, num_lines):
    return shade_quadrilateral(a, b, c, c, num_lines)

def shade_quadrilateral(a1, b1, a2, b2, num_lines):
    """
    Draw lines going from a1->b2, and interpolating those to a2->b2.
    Will make num_lines worth.

    # TODO add endpoint logic.
    """
    lines = []

    # The alternation is an easy drawing optimization trick, so it goes back and forth
    # instead of picking up the pen and going back to the other side first.
    alternate = False
    for l in np.linspace(0, 1, num_lines):
        start = a1*l +a2*(1-l)
        end = b1*l +b2*(1-l)

        if alternate:
            lines.append((end, start))
        else:
            lines.append((start, end))

        alternate = not alternate

    return lines

def grid_arc_shading(pts, n_segments):
    """
    shades 3 points.
    """
    a,b,c = pts[0:3, :]

    interp = np.linspace(0, 1, n_segments+1)
    s = interp[:-1]
    e = interp[1:]
    lines = []

    for i in range(len(s)):
        start = a*(1-s[i])+b*(s[i])
        end = b*(1-e[i])+c*(e[i])
        lines.append((start, end))

    return lines

def step_and_shade_poly(verts, num_lines_f, random_start=True, funky_shading=False):
    """
    Given some verts, this will break the polygon down into quads or triangles and shade them.

    It works with either verts being complete (so [a,b,c,...,a] or each one being unique).
    if the verts are complete, it makes a much denser and it breaks up the poly into multiple pieces.

    To add a funky shading, make sure to have a triangle that is complete.
    """

    if funky_shading and len(verts) == 4:
        verts = verts[:-1]
    if funky_shading and len(verts) != 4:
        logging.info("Was expecting a triangle (3 pts + endpoint)")

    total = len(verts)

    if random_start:
        start = np.random.randint(len(verts))
    else:
        start = 0

    order = [(a, b) for a,b in step_through_poly(start, start+1, len(verts))]

    shading = []
    for i in range(len(order) - 1):
        sa, sb = order[i]
        fa, fb = order[i+1]
        if isinstance(num_lines_f, int):
            shading += shade_quadrilateral(verts[sa], verts[sb], verts[fa], verts[fb], num_lines_f)
        else:
            shading += shade_quadrilateral(verts[sa], verts[sb], verts[fa], verts[fb], num_lines_f())


    return shading


def step_through_poly(a, b, total):
    """
    This function gives you a way of traversing a total sided polygon.
    a, b are 1 away from each other.

    Imainge you have a square with corners 0/4, 1, 2, 3

    you tell it 1,2, and this will give you (1,2), (0,3). This is so you can
    feed in arb shapes into shade_quadrilateral.
    """
    converged = False
    oa, ob = a, b
    count = 0
    while not converged:
        yield a%total, b%total
        a =(a-1)%total
        b = (b+1)%total
        if a == b or (np.abs(a-b) == 1 or np.abs(a-b+total) == 1):
            converged = True
            yield a%total, b%total
        count += 1
        if count>50000:
            print(oa, ob, total)
            raise Exception()
