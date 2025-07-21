# result = 2 ** 4
# print(result)

# zeros = "AB" * 10
# print(zeros)

# def foo(a, b, *args, **kwargs):
#     print(a)
#     for arg in args:
#         print(arg)
#     for key in kwargs:
#         print(key, kwargs[key])
# foo(1, 2, 3, five = 5)

def foo(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
foo(*my_list)

my_string = "ABC"
foo(*my_string)

my_dict = {'a': 4, 'b': 5, 'c': 6}
foo(**my_dict)

#unpack the elements
numbers = (1, 2, 3, 4, 5, 6, 7, 8)

*beginning, last = numbers
print(beginning)
print(last)

print()

first, *end = numbers
print(first)
print(end)

print()
first, *middle, last = numbers
print(first)
print(middle)
print(last)

#merge dictionaries
dict_a = {'one': 1, 'two': 2}
dict_b = {'three': 3, 'four': 4}
dict_c = {**dict_a, **dict_b}
print(dict_c)
