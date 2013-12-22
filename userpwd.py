#!/usr/bin/env python

db = {}

def new_user():
	prompt = "Login desired:\n" 
	while True:
		name = raw_input(prompt) #using the string to define a raw input
		if db.has_key(name): #if the dict has the key said by the user
			prompt = "name taken, try another:\n" #output message
			continue #continue the program
		else:
			break
	pwd = raw_input("Password:\n")
	db[name] = pwd #key and value

def old_user():
	name = raw_input("Login:\n")
	pwd = raw_input("Password:\n")
	passwd = db.get(name)
	#returns a value for the given key. If key is not available then returns default value None.
	if passwd == pwd:
		print "Welcome back", name
	else:
		print "Login incorrect"

def showmenu():
	prompt = """
	(N)ew User Login
	(E)xisting User Login
	(Q)uit

	Enter choice:\n"""

	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError, KeyboardInterrupt):
				choice = "q"
			print "You picked: %s" % choice
			if choice not in "neq":
				print "Invalid Option, please try again:\n"

			else:
				chosen = True

		if choice == "q":
			done = True
		if choice == "n":
			new_user()
		if choice == "e":
			old_user()
			
if __name__ == '__main__':
	showmenu()