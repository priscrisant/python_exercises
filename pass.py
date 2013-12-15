#!/usr/bin/env python

import sys
class Psw:

    def __init__(self):
        print "------------------------------"
        print "This is your password manager!"
        print "------------------------------"

    def Info(self):
        user = raw_input ("Please, enter the main password to have access:\n")
        if user == "mainpassword":
            print "Access Guaranteed! Welcome to your Password Manager!"
        else:
            print "Something went wrong! You typed an invalid information. Exiting the program!"


    def main(self):
        user_2 = raw_input ("Please type the name of the website/software you want to know the password:\n")
        if user_2 == "outlook":
            print "Your Outlook Password is: HAYHEYHSH"
        else:
            print "There's no such information here."


if __name__ == "__main__":
    root = Psw()
    root.Info()
    root.main()