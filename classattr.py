class Student(object):
    name = 'Student'

s = Student()

print(s.name)
print(Student.name)
s.name = 123
print(s.name)
del s.name
print(s.name)
