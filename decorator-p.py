def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('call %s() - %s:' % (func.__name__,text))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
now()