def foo1():
    x = number 
    print('number in function:', x)

number = 0
foo1()

def foo2():
    global number
    number = 3

print('number before foo2(): ', number)
foo2()
print('number after foo2(): ', number)