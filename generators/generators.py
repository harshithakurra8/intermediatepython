def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

# print(g)

# for i in g:
#     print(i)

# value = next(g)
# print(value)
# value = next(g)
# print(value)

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1
cd = countdown(3)
print(next(cd))
print(next(cd))
print(next(cd))


def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")



def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
print(list(fib))



mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator), "bytes")


mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist), "bytes")
