class Student(object):
    pass

s = Student()
s2 = Student()
s.name = 'Michael'

def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(25)

print(s.age)
# print(s2.name)