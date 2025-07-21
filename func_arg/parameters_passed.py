#immutable -no change
def foo(x):
    x = 5

var = 10
print('var before foo():', var)
foo(var)
print('var after foo():', var)

# mutable

def foo(a_list):
    a_list.append(4)

my_list = [1, 2, 3]
print('my_list before foo():', my_list)
foo(my_list)
print('my_list after foo():', my_list)