class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        attrs['add'] = lambda self, val: self.append(val)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)