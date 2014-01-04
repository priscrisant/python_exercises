#!/usr/bin/env python

import gtk

class Base:
	def __init__(self):
		window = gtk.Window()
		window.connect("destroy", lambda w: gtk.main_quit())

		box = gtk.VBox() #vertical box
		entry = gtk.Entry()
		entry_2 = gtk.Entry()

		#we've got a container(window) and we'll
		#put the box inside the container
		window.add(box) 
		box.pack_start(entry)
		box.pack_start(entry_2)

		window.show_all()
		entry.connect("activate", self.entry_go)
		entry_2.connect("activate", self.entry_go)

	def entry_go (self, widget):
		print "You entered this: ", widget.get_text() 

	def main(self):
		gtk.main()

'''we have a window and inside the window we've got a vertical
box and inside the vertical box we have an entry box'''	

if __name__ == '__main__':
	root = Base()
	root.main()