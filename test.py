
eq1 = {'asdf': 19}

from copy import deepcopy
eq2 = deepcopy(eq1)

eq2['asdf'] *= 2

print eq1
print eq2
