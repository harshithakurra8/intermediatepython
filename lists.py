#Lists : ordered ,mutable, allows duplicates

mylist =["banana","cherry","apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

item = mylist[1]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("no")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1,"blueberry")
print(mylist)

item =mylist.pop()
print(item)
print(mylist)

item =mylist.remove("apple")
print(item)
print(mylist)

mylist = [4 ,3, -2, 10, -1 , -5]
print(mylist)

item = mylist.sort()
print(item)
print(mylist)

mylist = [1, 2, 3, 4, 5]

a= mylist[::-1]
print(a)


list_org = ["banana", "cherry", "apple"]
list_cpy =list_org[:]

list_cpy.append("lemon")
print(list_org)
print(list_cpy)

a = [1, 2, 3, 4, 5]
b = [i+i for i in a]
print(a)
print(b)