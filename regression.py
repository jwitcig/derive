from math import pow

points = [
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
]

points = [
    (0, 210),
    (7, 215),
    (14, 225),
    (40, 250),
    (48, 245),
]

a = b = c = 0

for i, (x, y) in enumerate(points):
    if x == 0:
        c = y


poi = points[1]

eq1 = {
    'x': poi[0],
    'y': poi[1],
    'n0': {'cof': a, 'val': pow(poi[0], 2)},
    'n1': {'cof': b, 'val': poi[0]},
    'n2': c,
}

poi = points[2]

eq2 = {
    'x': poi[0],
    'y': poi[1],
    'n0': {'cof': a, 'val': pow(poi[0], 2)},
    'n1': {'cof': b, 'val': poi[0]},
    'n2': c,
}

import ipdb; ipdb.set_trace()

from copy import deepcopy
eq1_result = deepcopy(eq1)
eq2_result = deepcopy(eq2)

eq1_result['y'] -= c
eq2_result['y'] -= c



eq1_result['y'] *= eq2['n1']['val']
eq1_result['n0']['val'] *= eq2['n1']['val']
eq1_result['n1']['val'] *= eq2['n1']['val']

eq2_result['y'] *= eq1['n1']['val']
eq2_result['n0']['val'] *= eq1['n1']['val']
eq2_result['n1']['val'] *= eq1['n1']['val']

eq1_result['n0']['cof'] = (eq1_result['y']-eq2_result['y']) / (eq1_result['n0']['val'] - eq2_result['n0']['val'])

print eq1_result['n0']['cof']

eq1_result['n1']['cof'] = (eq1_result['y'] - eq1_result['n0']['cof']*eq1_result['n0']['val']) / eq1_result['n1']['val']
print eq1_result['n1']['cof']

print c


# print a, b, c
