#!/usr/bin/python
# Filename: class_init.py

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print ('Hello, my name is', self.name)  
    def sayHi2():
        print ('Hello2, my name is')

p = Person('Swaroop')

p.sayHi()
Person.sayHi2()