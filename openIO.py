fpath = './txt/ee.txt'
wpath = './txt/ee2.txt'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

with open(wpath, 'w') as w:
    w.write(s)