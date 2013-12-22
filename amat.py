#!/usr/bin/python
# coding: utf-8

import time
from datetime import datetime
from time import mktime

big_data_file = open("AMAT.txt", "r")

read_file = big_data_file.read()
line_split = read_file.split("\n")

for every_line in line_split:
	devided_line = every_line.split(',')
	stock_name = devided_line[0].split('.')[1]
	#initialDate = dividedLine[2]+dividedLine[3] unixStamp = mktime(datetime.strptime(initialDate, ‘%Y%m%d%H%M%S’).timetuple())
	date_stamp = time.strftime('%m/%d/%Y%H:%M:%S')


	stock_price = devided_line[4]

	reformatted = date_stamp, stock_name, stock_price
	save_format = tr(reformatted).replace(‘\”,”).replace(‘(‘,”).replace(‘)’,”)


	append_file = open("example.txt", "a")
	append_file.write(save_format)
	append_file.write("\n")
	append_file.close()
