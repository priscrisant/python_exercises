#!/usr/bin/env python


import sys
class Psw:

    def __init__(self):
        print ("\t################################################################")
        print ("\t#                  SIMPLE PASSWORD MANAGER                     #")
        print ("\t#                                    Written by Priscisant     #")
        print ("\t################################################################")


    def Info(self):
        user = raw_input ("Please, enter the main password in lower case to have access:\n")
        if user == "mainpassword":
            print "Access Guaranteed! Welcome to your Password Manager!"
        else:
            print "Something went wrong! You typed an invalid information. Exiting the program!"
            sys.exit(1)

    def main(self):
        user_2 = raw_input ("Please type the name of the website/software you want to know the password in lower case:\n")
        if user_2 == "outlook":
            print "Your Outlook Password is: ********"
        elif user_2 == "yahoo":
            print "Your Yahoo Password is: *********"
        elif user_2 == "instagram":
            print "Your instagram Password is: **********"
        elif user_2 == "gmail":
            print "Your Gmail Password is: **********"
        else:
            print "There's no such information here."
            sys.exit(2)

if __name__ == "__main__":
    root = Psw()
    root.Info()
    root.main()