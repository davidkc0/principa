import numpy as np

def get_coord(p):
    return np.round(p).astype(int)

def coord_inside_mask(p, mask):

    p = get_coord(p)

    valid_x = p[0]>=0 and p[0]<mask.shape[0] - 1
    valid_y = p[1]>=0 and p[1]<mask.shape[1] - 1

    if valid_x and valid_y:
        return mask[p[0], p[1]]

    return False

def percent_line_in_mask(start, end, mask, n_segments):
    count = 0
    for l in np.linspace(0, 1, n_segments):
        p = start*l +  end*(1-l)
        p = get_coord(p)
        if coord_inside_mask(p, mask):
            count += 1
    return count/n_segments

def estimate_intersection(p1, p2, mask, n_subdiv):
    starting_value = coord_inside_mask(p1, mask)
    for l in np.linspace(0, 1, n_subdiv):
        p = p1*(1-l)+p2*(l)
        new_value = coord_inside_mask(p, mask)
        if new_value != starting_value:
            return p
    return p2

def get_line_segments(start, end, mask, n_segments, n_subdiv):
    starting_pt = None
    making_line = False

    line_segments = []
    ls = np.linspace(0, 1, n_segments)

    for i in range(len(ls)):
        l = ls[i]
        p = start*l +  end*(1-l)
        valid_point = coord_inside_mask(p, mask)

        if making_line:
            if valid_point:
                continue
            else:
                making_line = False
                last_p = start*ls[i-1] +  end*(1-ls[i-1])
                end_pt = estimate_intersection(last_p, p, mask, n_subdiv)
                line_segments.append((starting_pt, end_pt))
        else:
            if valid_point:
                if i>0:
                    last_p = start*ls[i-1] +  end*(1-ls[i-1])
                    starting_pt = estimate_intersection(last_p, p, mask, n_subdiv)
                else:
                    starting_pt = p

                making_line = True
            else:
                continue

    return line_segments

def clip_lines_to_mask(lines, mask, n_segments=100):
    new_lines = []
    for line in lines:
        for i in range(len(line) - 1):
            start, end = line[i], line[i+1]
            percent = percent_line_in_mask(start, end, mask, n_segments)
            if percent == 0:
                continue
            elif percent == 1:
                new_lines.append((start, end))
            else:
                new_lines+= get_line_segments(start, end, mask, n_segments, 10)

    return new_lines
