def count():
    def j(f):
        def g():
            return f * f
        return g
    fs = []
    for i in range(1,4):
        fs.append(j(i))
    return fs

for f in count():
    print(f())

