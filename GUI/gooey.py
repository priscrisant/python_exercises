#!/usr/bin/env python

import pygtk
import gtk

class Base:

	def destroy (self,widget, data = None):
		gtk.main_quit()
		#kill the application when the window is closed

	def my_hide(self, widget):
		self.button_1.hide()
		#hide the button chosen, in this case the button 1

	def my_show(self, widget):
		self.button_1.show()
		#show the button chosen, in this case the button 2

	def rename(self, widget):
		self.label_1.set_text("Renamed Label")
		#rename the label

	def text_change(self, widget):

		#to change the tile when writing to the textbox
		self.window.set_title(widget.get_text())
		
		#to change the label when writing to the textbox
		self.label_1.set_text(widget.get_text())

	def clearing(self, widget):
		#function to clear the text
		self.textbox.set_text("")

	def combo_text(self, widget):
		#function to create the combo box
		self.textbox.set_text(widget.get_active_text())

	def add_combo(self, widget):
		#appending the text to the combo box
		self.combo.append_text(self.textbox.get_text())

	def about_program(self, widget):

		#creating an about dialog window
		about = gtk.AboutDialog()
		about.set_program_name("My First GTK Program")
		about.set_version("1.0")
		about.set_copyright("(c) Priscrisant")
		about.set_comments("This is my first gtk program written in python")
		about.set_website("pr.risant@gmail.com")
		about.set_logo(gtk.gdk.pixbuf_new_from_file("mask.png"))
		about.run()
		about.destroy()


	def __init__ (self):
		#do the center and the size before size the window
		#creating the main window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) 
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_size_request(600,500)
		self.window.set_title("GUI Program")
		self.window.set_tooltip_text("This is a GTK program\nBy Priscrisant")

		#creating Buttons and defining their functions
		self.button_1 = gtk.Button("Exit") #create a button
		self.button_1.connect("clicked", self.destroy) #connect the button to an existing function
		self.button_1.set_tooltip_text("This Button will close this program")


		self.button_2 = gtk.Button("Hide")
		self.button_2.connect("clicked", self.my_hide)
		self.button_2.set_tooltip_text("This Button will Hide the Exit Button")


		self.button_3 = gtk.Button("Show")
		self.button_3.connect("clicked", self.my_show)
		self.button_3.set_tooltip_text("This Button will Show the Exit Button")
		

		self.button_4 = gtk.Button("Rename Label")
		self.button_4.connect("clicked", self.rename)
		self.button_4.set_tooltip_text("This Button will rename the label")

		self.button_5 = gtk.Button("Clear Text")
		self.button_5.connect("clicked", self.clearing)
		self.button_5.set_tooltip_text("This Button will clear the text")

		self.button_6 = gtk.Button("Add to Combo")
		self.button_6.connect("clicked", self.add_combo)
		self.button_6.set_tooltip_text("This Button add to the Combo Box")

		#creating an about button
		self.about_button = gtk.Button("About")
		self.about_button.connect("clicked", self.about_program)

		#creating a label
		self.label_1 = gtk.Label("New Label")

		#creating a text box
		self.textbox = gtk.Entry()
		self.textbox.connect("changed", self.text_change)

		#creating a combo box with two options
		self.combo = gtk.combo_box_entry_new_text()
		self.combo.connect("changed", self.combo_text)
		self.combo.append_text("This is option #1")
		self.combo.append_text("This is option #2")

	
		#creating a chooser box
		dialog = gtk.FileChooserDialog("Choose an Image", 
			None, gtk.FILE_CHOOSER_ACTION_OPEN,
			(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
				gtk.STOCK_OPEN, gtk.RESPONSE_OK))

		#setting the default response as OK
		dialog.set_default_response(gtk.RESPONSE_OK)
		
		#creating filters to the chooser box
		filter = gtk.FileFilter()
		filter.set_name("Images")
		filter.add_mime_type("image/png")
		filter.add_mime_type("image/jpg")
		filter.add_mime_type("image/jpeg")
		filter.add_mime_type("image/gif")
		filter.add_pattern("*.png")
		filter.add_pattern("*.jpg")
		filter.add_pattern("*.jpeg")
		filter.add_pattern("*.gif")
		dialog.add_filter(filter)

		response = dialog.run() #run the dialog
		if response == gtk.RESPONSE_OK:
			self.pix = gtk.gdk.pixbuf_new_from_file(dialog.get_filename())
			self.pix = self.pix.scale_simple(500,300, gtk.gdk.INTERP_BILINEAR)
			self.image = gtk.image_new_from_pixbuf(self.pix)

		elif response == gtk.RESPONSE_CANCEL:
			print "No File Selected"
			print "Exiting the program"

			#error message box and exiting the program
			error_mes = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT,
				gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "ERROR LOADING FILE\nEXITING!")
			error_mes.run()
			error_mes.destroy()
			raise SystemExit
		
		dialog.destroy()


	#-------- creating boxes and adding the widgets to them -------#
		
		self.box_1 = gtk.HBox() #horizontal box
		
		#adding the buttons created into the box
		self.box_1.pack_start(self.button_1)
		self.box_1.pack_start(self.button_2)
		self.box_1.pack_start(self.button_3)
		self.box_1.pack_start(self.button_4)
		self.box_1.pack_start(self.button_5)
		self.box_1.pack_start(self.about_button)


		self.box_3 = gtk.HBox() #horizontal box
		self.box_3.pack_start(self.textbox)
		self.box_3.pack_start(self.button_6)

		
		self.box_2 = gtk.VBox() #vertical box
		#adding stuff to the vertical box
		self.box_2.pack_start(self.box_1)
		self.box_2.pack_start(self.label_1)
		self.box_2.pack_start(self.box_3)
		self.box_2.pack_start(self.combo)
		self.box_2.pack_start(self.image)
		
		


		#adding all the things created so far to the main window
		self.window.add(self.box_2)
		self.window.show_all()#show all the widgets the window
		self.window.connect("destroy", self.destroy)
		#when the window is closed, destroy-function


	def main (self):
		gtk.main()

if __name__ == '__main__':
	root = Base()
	root.main()

'''to make and show a normal button
fixed = gtk.Fixed()
fixed.put(self.button_1, 5, 30)
fixed.put(self.button_2, 50, 30)
fixed.put(self.button_3, 100, 30)
self.window.add(fixed)'''

#putting an image
'''to scale an image to scale into the program
self.pix = gtk.gdk.pixbuf_new_from_file_at_size("image.jpg", 500, 500)'''
'''self.pix = gtk.gdk.pixbuf_new_from_file('image.jpg') #if I dont need to scale
self.image = gtk.Image()
self.image.set_from_pixbuf(self.pix)'''