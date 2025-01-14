import numpy as np
from plottermagic.geometry import geom2d

class WallpaperGroup:

    """
    https://en.wikipedia.org/wiki/List_of_planar_symmetry_groups#Wallpaper_groups
    http://xahlee.info/Wallpaper_dir/c5_17WallpaperGroups.html
    """

    """
    Our fundamental shape is from o, o+b1, o+b2, o+b1+b2
    b1 = y direction
    b2 = x direction
    (for reading the wiki diagrams)
    """
    shape_to_pattern = {
        "rhombus":["o", "2222"],
        "square":["o", "2222", "*2222", "442", "4*2", '*442', '2*22', '22×'],

    }

    def __init__(self, origin, b1, b2):

        self.origin = origin
        self.b1 = b1
        self.b2 = b2

        dp = np.dot(b1, b2)
        l1, l2 = np.linalg.norm(b1), np.linalg.norm(b2)
        self.internal_angle = np.arccos(dp/(l1*l2))*360/(2*np.pi)

        is_hex = np.abs(self.internal_angle - 60) < 1e-5

        if l1 == l2 and dp == 0:
            self.shape = "square"
        elif dp == 0:
            self.shape = "rectangle"
        elif l1 == l2 and not is_hex:
            self.shape = "rhombus"
        elif is_hex:
            self.shape = "hex_thingy"
        else:
            # TODO not 100% sure this is right....
            raise Exception("not sure about this shape.")

        self.corners = np.stack([origin, origin+b1, origin+b1+b2, origin+b2])
        self.center = origin + 0.5*(b1+b2)
        self.midpoints = np.stack([origin + b1/2, origin+b1+b2/2, origin+b1/2+b2, origin + b2/2])
        self.valid_patterns = self.shape_to_pattern.get(self.shape, ["o"])

    def get_pattern_generator_poly(self, pattern):

        if pattern not in self.valid_patterns:
            print("wasnt really expecting pattern {} for shape {}".format(pattern, self.shape))

        center, origin, b1, b2 = self.center, self.origin, self.b1, self.b2

        if pattern == 'o':
            self.generator =  self.corners.copy()
        elif pattern == '2222':
            if self.shape == 'rhombus':
                self.generator = np.stack([origin, origin+b2, origin+b2+b1])
            if self.shape in ['square', 'rectangle']:
                self.generator = np.stack([origin, origin+b2, origin+b2+b1/2, origin+b1/2])

        elif pattern == '*2222' or pattern == "442":
            self.generator = np.stack([origin, origin+b2/2, origin + b1/2 +b2/2, origin + b1/2])
        elif pattern == '4*2':
            self.generator = np.stack([origin+b2/2, center, origin+ b1/2])
        elif pattern == '*442':
            self.generator = np.stack([origin, origin+b2/2, center])
        elif pattern == '2*22':
            self.generator = np.stack([origin, origin+b2, center])
        elif pattern == '22×':
            self.generator = np.stack([origin+b2/2, origin+b2+b1/2, origin+b1/2])


        return self.generator


    def complete_pattern(self, lines, pattern):
        homo_pts, inds = geom2d.lines_to_matrix(lines)
        center, origin, b1, b2 = self.center, self.origin, self.b1, self.b2

        functions = []
        clean_up_lines = False

        if pattern == 'o':
            return lines
        elif pattern == '2222':
            f = geom2d.rot_about_pt(center, np.pi)
            functions = [np.eye(3), f]
        elif pattern == '*2222':
            functions = [np.eye(3)]
            for offset, angle in [(origin+b2/2, 90), (origin+b1/2, 0)]:
                functions.append(geom2d.ref_about_point(offset, angle, degrees=True))
            functions.append(geom2d.rot_about_pt(center, np.pi))
        elif pattern == "442":
            functions = [geom2d.rot_about_pt(center, i*np.pi/2) for i in range(4)]
        elif pattern == '4*2':
            base = [np.eye(3), geom2d.ref_about_point(origin+b2/2, 135, degrees=True)]
            functions = []
            for i in range(4):
                for b in base:
                    functions.append(np.matmul(geom2d.rot_about_pt(center, i*np.pi/2) ,b))

        elif pattern == '*442':
            bases = [np.eye(3), geom2d.ref_about_point(origin+b2/2, 90, degrees=True)]

            functions = []
            for i in range(4):
                for base in bases:
                    functions.append(np.matmul(geom2d.rot_about_pt(center, i*np.pi/2), base))

        elif pattern == '2*22':
            ref1 = [np.eye(3), geom2d.ref_about_point(origin, 45, degrees=True)]
            ref2 = []
            for ref in ref1:
                ref2.append(np.matmul(geom2d.ref_about_point(center, 135, degrees=True),ref))
            functions = ref1 + ref2

        elif pattern == '22×':

            weird_flip = geom2d.ref_about_point(origin+b2/2, 0, degrees=True)
            glide1 = np.matmul(geom2d.translate(b1/2+b2/2), weird_flip)
            glide2 = np.matmul(geom2d.translate(b1/2-b2/2), weird_flip)

            bottom = [np.eye(3), glide1, glide2]
            top = []
            for b in bottom:
                top.append(np.matmul(geom2d.rot_about_pt(center, np.pi), b))

            functions = bottom+top
            clean_up_lines = True


        if len(functions) == 0:
            print("uhhhhhh this doesnt seem implemented yet")
            functions = [np.eye(3)]

        transformed_pts = []
        for f in functions:
            result_pts = np.matmul(f, homo_pts.transpose()).transpose()
            transformed_pts.append(result_pts)

        transformed_lines = []
        for pts in transformed_pts:
            new_lines = geom2d.matrix_to_lines(pts, inds)
            for line in new_lines:
                transformed_lines.append(line)

        if clean_up_lines:
            # TODO should probably make this better and throw it in shading. Would be useful later for hatching.
            if len(self.b1.shape) > 1 or len(self.b2.shape) > 1:
                raise Exception("uhhh wasnt expecting a shaped basis vector.")

            T = np.stack([self.b2, self.b1]).transpose()
            t_inv = np.linalg.inv(T)

            def is_in(pt):
                coord = np.matmul(t_inv, (pt - origin))
                return np.all(coord == np.clip(coord, 0, 1))

            # TODO just make this shapely!
            clipped_lines = []
            for line in transformed_lines:
                for i in range(len(line) - 1):
                    a = line[i]
                    b = line[i+1]

                    if is_in(a) and is_in(b):
                        clipped_lines.append((a, b))
                    else:
                        is_drawing = False
                        start = None

                        for l in np.linspace(0, 1, 20):
                            c = a*l+b*(1-l)
                            is_valid = is_in(c)

                            if is_valid:
                                if is_drawing:
                                    pass
                                else:
                                    is_drawing = True
                                    start = c
                            else:
                                if is_drawing:
                                    clipped_lines.append((start, c))
                                    is_drawing = False
                                    start = None
                                else:
                                    is_drawing = False

                        if is_drawing:
                            clipped_lines.append((start, c))

            return clipped_lines

        else:
            return transformed_lines
