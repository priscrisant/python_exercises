#!/usr/bin/env python

class Base:
	def __init__(self, *letters):
		self.letters = letters

	def print_out(self):
		print str(self.letters) + "\n"

		for item in self.letters:
			print item



if __name__ == '__main__':
	root = Base("Apples", "Juice", "Fruits")
	root.print_out()