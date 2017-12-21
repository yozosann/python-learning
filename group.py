import itertools

for key, group in itertools.groupby('AAaABBBCCAA', lambda c: c.lower()):
    print(key, list(group))