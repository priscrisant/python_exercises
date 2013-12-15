#!/usr/bin/env python

#if the user wants to assing a new information

class Base:
	def __init__(self):
		pass

	def info(self):
		d = {}
		user = raw_input ("what is the website?\n")
		user_2 = raw_input ("what is the password?\n")
		d[user] = user_2
		#print "This is the website %s and this is the password %s" % (user, user_2)
		print d


if __name__ == '__main__':
	root = Base()
	root.info()