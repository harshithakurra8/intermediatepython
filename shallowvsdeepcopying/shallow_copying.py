# org = 5
# cpy = org
# cpy = 6

# print(cpy)
# print(org)

import copy
org = [1, 2, 3, 4, 5]
cpy = copy.copy(org)

cpy[0] = -10
print(org)
print(org)


import copy
org = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
cpy = copy.copy(org)
org[0][1]= -10
print(org)
print(cpy)