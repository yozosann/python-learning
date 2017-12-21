#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_info(self):
        print('%s : %d' % (self.__name, self.__score))

    def get_name(self):
        print(self.__name)

student = Student('yozo', 99)

student.__name = 123
print(student.__name)
student.get_name()