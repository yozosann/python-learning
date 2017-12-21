import threading

local_school = threading.local()

class Student(object):
    def __init__(self, name):
        self._name = name

    def print_name(self):
        print(self._name)

def std_thread(name):
    local_school.student = Student(name)

    do_task_1()
    do_task_2()

def do_task_1():
    std = local_school.student
    print('task 1:')
    std.print_name()

def do_task_2():
    std = local_school.student
    print('task 2:')
    std.print_name()

t1 = threading.Thread(target=std_thread, args=('yozo' ,))
t2 = threading.Thread(target=std_thread, args=('bbbddd', ))

t1.start()
t2.start()
t1.join()
t2.join()

print('END')