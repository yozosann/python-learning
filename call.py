class Student(object):
    def __init__(self, name):
        self._name = name
    
    def __call__(self):
        return self._name

print(Student('111')())
