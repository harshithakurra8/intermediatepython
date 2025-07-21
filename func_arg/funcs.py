# def foo(a, b, c, d=4):
#     print(a, b, c, d)
                                                            #default arg
# foo(1, 2, 3, 4)
# foo(1, b=2, c=3, d=100)


# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     for arg in args:
#         print(arg)
#     for kwarg in kwargs:
#         print(kwarg, kwargs[kwarg])
# foo(1, 2, 3, 4, 5, six=6, seven=7)
# print()
# foo(1, 2, three=3)


def foo(a, b, c):
    print(a, b, c)
my_list = [4, 5, 6]
foo(*my_list)                                                                   #unpacking  a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
foo(**my_dict)