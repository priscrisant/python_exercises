#!/usr/bin/env python

d = {}

planets = ["Jupiter", "Mars", "Jupiter", "Venus", "mars", "mars", "mars", "Uranus"]

print "this is the list of planets:\t" + str(planets)



'''for name in planets:
    if name not in d:
        d[name]= 1
    else:
        d[name] = d[name] + 1

print d'''





#short line code
for name in planets:
    d[name] = d.get(name, 0) + 1 
print d


'''get the value stored name and if you dont find it
give me back a 0 (default) and whatever comes back, either some other
value or 0, it'll add a 1 to it'''
#this going to either create or update the values

