#!/usr/bin/env python

'''def sorting(filename):
	words = []
	with open(filename) as file_handle:
		for line in file_handle:
			words += line.strip().split()
	return sorted(words)

print '\n'.join(sorting('food.txt'))'''


class Base:
	def __init__(self):
		pass


	def sorting(self, filename):
		self.filename = filename
		words = []
		with open(self.filename) as file_handle:
			for line in file_handle:
				words += line.split()
		print sorted(words)
		#print '\n'.join(sorting('food.txt'))

if __name__ == '__main__':
	root = Base()
	root.sorting("food.txt")