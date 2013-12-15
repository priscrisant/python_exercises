#!/usr/bin/env python

class Base:
    def __init__(self):
        self.numbers = [23,54,-344,]
        print self.get_minimum(self.numbers)



    def get_minimum(self, value):
        for item in value:
            if item == value[0]:
                minimum = item

            else:
                if item < minimum:
                    minimum = item

        return minimum


if __name__ == "__main__":
    root = Base()
