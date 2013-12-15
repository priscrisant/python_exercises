#!/usr/bin/env python

class Stuff(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print "My name is %s and I am %d" % (self.name, self.age)

    def __str__(self):
        print "My name is %s and I am %d" % (self.name, self.age)

root = Stuff("Priscilla", 23)
root.__str__()

'''if I dont use the __str__ they will print out the number of the
object memory, try that out. Print the root = Stuff(object) without the str'''
#but it seems only to work on the shell