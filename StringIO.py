from io import StringIO

f = StringIO()

f.write('hello\n')
f.write('code')

print(f.getvalue())

f2 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f2.readline().strip()
    if s == '':
        break
    print(s)
