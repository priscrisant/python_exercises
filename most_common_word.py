#!/usr/bin/env python

d = {}

names = ["john", "Lisa", "jupiter", "lisa", "lisa", "mars", "mars", "john"]

print "this is the list on names:\t" + str(names)



'''for name in names:
    if name not in d:
        d[name]= 1
    else:
        d[name] = d[name] + 1

print d'''





#short line code
for name in names:
    d[name] = d.get(name, 0) + 1 
print d


'''get the value stored name and if you dont find it
give me back a 0 (default) and whatever comes back, either some other
value or 0, it'll add a 1 to it'''
#this going to either create or update the values

