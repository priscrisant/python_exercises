#!/usr/bin/env python

class Team:
    def __init__(self):
        pass


    def example(self):
        scores = [] #set up an empty list
        
        number = input("Number of Teams:\n") #inputs the number of the teams
        print "Insert the name of the Team and the number of scores separeted by spaces\n"


        for i in range(0,number): #it will enumerate each team that will be inputed
            info = raw_input("Team %s:" % (i)) #gets the user information
            scores.append(info.split()) #append the inputs
        print scores #print the result

if __name__ == "__main__":
    root = Team()
    root.example()

    '''if i use the .split() BIF the name of the team and the number of goals
will be printed separated. If I do not use it, it'll be printed as a only
string'''
