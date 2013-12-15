#!/usr/bin/env python

class File:

    def __init__(self):
        pass


    def writing(self):
        print "Opening the file."
        filename = "/home/priscilla/python/darkside.txt"
        file_handle = open(filename, "w")
        file_handle.write(text)
        file_handle.close()
        print "Closing the file."


if __name__ == "__main__":
    root = File()
    root.writing()