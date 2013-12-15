#!/usr/bin/env python


class File:

    def __init__(self):
        pass


    def reading(self):
        try:
            filename = raw_input ("Please, insert the file name:\n")
            file_handle = open (filename, "r")
            prompt = file_handle.read()
            print prompt
            file_handle.close()
        except:
            print "Oops, there is no such file'"


if __name__ == "__main__":
    root = File()
    root.reading()