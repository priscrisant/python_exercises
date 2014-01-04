#!/usr/bin/env python

import gtk

class Base:
	
	def __init__(self):
		self.window = gtk.Window( gtk.WINDOW_TOPLEVEL )
		#popup the window in the certer of the screen
		self.window.set_position(gtk.WIN_POS_CENTER )

		#defining the window size
		self.window.set_size_request(490, 490)


		self.window.connect("destroy",self.close_window)
		self.window.show()
		
	def close_window(self, widget, data = None):
		print "you closed the window"
		gtk.main_quit()


	def main(self):
		gtk.main()

if __name__ == '__main__':
	root = Base()
	root.main()
