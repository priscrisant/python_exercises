#!/usr/bin/env python

class Base:
	def __init__(self, **book):
		print (book)

		for key, value in book.iteritems():
			print "%s is the Key and %s is the value" % (key, value)







if __name__ == '__main__':
	root = Base(Jupiter = "Planet", Mercury = "Element", Pluto = "Cartoon")