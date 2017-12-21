def fn(self, name = 'world'):
    print('Hello , %s' % name)

def init(self, name):
    self._name = name

def _print(self):
    print(self._name)
Hello = type('Hello', (object, ), dict(hello = fn, __init__ = init, print = _print))
h = Hello('11')
h.hello()
h.print()