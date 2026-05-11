def max_error(p:dict, l: dict):
    if len(p) != len(l):
        raise ValueError('The length of p does not match the length of l')

    difference = []
    for x in list(p.keys()):
        difference.append(abs(p[x] - l[x]))

    return max(difference)