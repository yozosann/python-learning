def person(name, age, *, city, job):
    print(name, age, city, job)

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)