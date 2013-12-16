#!/usr/bin/env python
# Copyright 2013 Google Inc.
#Licensed under the Apache License, Version 2.0



import sys
global full
full = {}

#Receive filename, open the file and process its word counts
#Close the file afterwards

def word_process(filename):
	f = open(filename, "r") #open and read the filename
	for line in f:
		line = line.lower() #turn the word to lowercase
		part = str.split(line) #split the strings
		for word in part:
			if word in full:
				full[word] += 1
			else:
				full[word] = 1
	f.close()

def Fun(x):
	return x[-1]


def print_words(filename):
	word_list = []
	word_process(filename)
	word_list = full.items()
	word_list = sorted(word_list, reverse = True, key = Fun,)
	for items in word_list:
		print (items)

def print_top(filename):
	count = 0
	word_list = []
	word_process(filename)
	word_list = full.items()
	word_list = sorted(word_list, reverse = True, key = Fun,)
	for items in word_list:
		print items
		count += 1
		if count == 20:
			sys.exit(1)


	def main():
		if len(sys.argv) != 3:
			print "usage: ./wordcount.py {--count | --topcount} file"
			sys.exit(1)

		option = sys.argv[1]
		filename = argv[2]
		if option == "--count":
			print_words(filename)
		elif option == "--topcount":
			print_top(filename)
		else:
			print "unknown option: " + option
			sys.exit(1)

if __name__ == '__main__':
	main()