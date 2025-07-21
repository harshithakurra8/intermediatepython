# import random

# #a = random.random
# #a= random.uniform(1,10)
# #a= random.randint(1,10)
# #a= random.randrange(1,10)
# # a=random.normalvariate(1,10)
# # print(a)



# # mylist = list("ABCDEFG")
# # # a = random.choices(mylist,k=4)
# # # print(a)

# # random.shuffle(mylist)
# # print(mylist)


# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))
# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))


# import secrets

# # a = secrets.randbelow(10)
# # print(a)

# # a = secrets.randbits(4)
# # print(a)

# mylist = list("ABCDEFGH")

# a = secrets.choice(mylist)
# print(a)

import numpy as np

# a = np.random.rand(3,3)
# print(a)

# a = np.random.randint(0,10,3)
# print(a)

# arr = np.array([[1,2,3],[4,5,6],[8,9,7]])
# print(arr)

# np.random.shuffle(arr)
# print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))