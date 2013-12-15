#!/usr/bin/env python


counts = {}

print "Enter a line of text:\n"
line = raw_input("")

words = line.split() #this piece will split the text
#split takes a line and turns it into a list of strings
print "Words:\n", words

print "Counting..."
for word in words:
    counts[word] = counts.get(word,0) + 1

       
print "Counts", counts

#how to skip ponctuation??
