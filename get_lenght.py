#!/usr/bin/env python

class Base:
    def __init__(self):
        self.numbers = 12324
        self.string = "this is a string"
        print self.get_len(self.numbers)
        print self.get_len(self.string)


    def get_len(self, value):

        #to make the code read int and str
        if (type(value)) is int:
            value = str(value)

        #the body of the code
        lenght = 0
        for element in value:
            lenght += 1
        return lenght




if __name__ == "__main__":
    root = Base()
    #remember again that we don't need to call the method
