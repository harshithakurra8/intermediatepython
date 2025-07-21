# "%", f-string , .format()

var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

var = 5
my_string = "the variable is %d" % var
print(my_string)

var = 3.148637486
my_string = "the variable is %.2f" % var
print(my_string)

var = 5.8746875
var2 = 6
my_string ="the variable is {:.2f} and {}".format(var, var2)
print(my_string)

var = 6.8438
var2 = 7
my_string = f"the variable is {var} and {var2}"
print(my_string)