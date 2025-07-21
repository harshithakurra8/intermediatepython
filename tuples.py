#Tuple : ordered,immutable, allows duplicates

mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = ("Max")
print(type(mytuple))

mytuple = tuple(("Max", 28, "Boston"))
print(mytuple)

item  = mytuple[0]
print(item)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print("no")

my_tuple =('a','h','a','j','k')
print(my_tuple.count('a'))
print(my_tuple.index('j'))

my_list = list(my_tuple)
print(my_list)

mytuple2 = tuple(my_list)
print(mytuple2)

a = (1, 2, 3, 4, 5)
b = a[2:4]
print(b)


my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4, 5)

i1,*i2,i3 = my_tuple
print(i1) 
print(i3)
print(i2)

import sys
my_list = [0, 1 , 2, "hello",True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list))  
print(sys.getsizeof(my_tuple)) 


import timeit
print(timeit.timeit(stmt='[0, 1, 2, 3, 4, 5]', number=1000000))
print(timeit.timeit(stmt='(0, 1, 2, 3, 4, 5)', number=1000000))