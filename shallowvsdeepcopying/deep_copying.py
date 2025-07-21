import copy
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# p1 = Person('Alex', 27)
# p2 = p1
# p2.age = 28
# print(p1.age)
# print(p2.age)

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employeen= employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 55
print(company_clone.boss.age)
print(company.boss.age)