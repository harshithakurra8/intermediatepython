#Dictionary : Key-value pairs, Unordered, Mutable, Indexed

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(mydict)

mydict2 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict2)

value = mydict["name"]
print(value)

mydict["EMAIL"] = "jhfjkjhjhfds@cdj.com"
print(mydict)

#Dictionary : Key-value pairs, Unordered, Mutable, Indexed

mydict = {
    "name": "Max",
    "age": 28,
    "city": "New York"
}

print(mydict)

mydict2 = dict(name = "Mary", age = 27, city = "Boston")
print(mydict2)

value = mydict["name"]
print(value)


mydict["EMAIL"] = "jhfjkjhjhfds@cdj.com"
print(mydict)

mydict["EMAIL"] = "cooljhfjkjhjhfds@cdj.com"
print(mydict)

del mydict["EMAIL"]
print(mydict)


mydict .pop("age")
print(mydict)

if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["city"])
except:
        print("error")

for key in mydict.keys():
    print(key)

for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict
mydict_cpy["email"] = "jhefjg@xyz.com"

print(mydict_cpy)
print(mydict)


my_dict = {"name": "Max", "age": 28, "email": "iireiihit@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")

my_dict.update(my_dict_2)
print(my_dict)


my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)


mytuple = (8,7)
my_dict = {mytuple: 15}
print(my_dict)