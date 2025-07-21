#Sets : unordered , mutable, no duplicates

myset = {1, 2, 3, 1, 2}
print(myset)

myset = set("Hello")
print(myset)

myset = {}
print(type(myset))


myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(5)

print(myset)  
 #discard,pop
print(myset.pop())
print(myset)



for i in myset:
    print(i)


if 1 in myset:
    print("yes")
else:
    print("no")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i = odds.intersection(primes)
print(i)


setA = {1, 2, 3, 4, 5}
setB = {1, 4, 5, 6, 7, 8}
diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)

diff  = setB.symmetric_difference(setA)
print(diff)

setA.update(setB)
print(setA)

setA.intersection_update(setB)
print(setA)

setA.symmetric_difference_update(setB)
print(setA)

setA ={1, 2, 3, 4, 5}
setB = {1, 2, 3}
setC = {7, 8}
print(setB.issubset(setA))


setA = {1, 2, 3, 4, 5}
setB = set(setA)

setB.add(6)
print(setB)
print(setA)


a = frozenset([1, 2, 3, 4, 5])
a.remove(1)          #this will raise an error
print(a)