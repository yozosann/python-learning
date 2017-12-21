class Student(object):
    def __init__(self, name):
        self.__name = name
    
    def __len__(self):
        return len(self.__name)

st = Student('yozo')

print(len(st))

print(hasattr(st, '__name')) # False
print(hasattr(st, '_Student__name')) # True