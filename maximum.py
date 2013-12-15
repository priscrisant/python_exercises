#!/usr/bin/env python

class Base:
    def __init__(self):
        self.numbers = [12,324,20,0]
        print (self.get_maximum(self.numbers))



    def get_maximum(self, value):
        for item in value:
            if item == value[0]:
                maximum = item
            else:
                if item > maximum:
                    maximum = item
        return maximum
        


if __name__ == "__main__":
    root = Base()

#I've just noticed that we do not call the method down here
# or they'll return an error
    
