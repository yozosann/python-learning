import pickle

d = dict(name='b', age = 3)

f = open('./txt/dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('./txt/dump.txt', 'rb')
s = pickle.load(f)
print(s)