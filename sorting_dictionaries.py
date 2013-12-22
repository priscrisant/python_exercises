#!/usr/bin/env python

stuff = {"Jupiter": "Planet", "Mars": "Chocolate", "Mercury": "Element"}

def sorting_key():
	sorting = sorted (stuff.items(), key = lambda t: t[0])
	print sorting

def sorting_values():
	sorting_v = sorted(stuff.items(), key = lambda t:t[1])
	print sorting_v

if __name__ == '__main__':
	sorting_key()
	sorting_values()