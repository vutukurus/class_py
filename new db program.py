#get list of two places files and store them in a database

import os
import sqlite3

place1 = raw_input("enter path for place 1:")
place2 = raw_input("enter path for place 2:")

table_list_Places = sqlite3.connect("places.db")
table_list_Places.execute("create table lists_temp_5(place1 text,place2 text)")

place1_lists = os.listdir(r'C:\Users\siv\Desktop\new\class_py')
place2_lists = os.listdir(r'C:\Users\siv\Desktop\automation')
test="sreedhar"
table_list_Places.execute("insert into lists_temp_5(place1,place2) values(1,'%s')" %(test))
table_list_Places.commit()

for i in place1_lists:
	for j in place2_lists:
		table_list_Places.execute("insert into lists_temp_5(place1,place2) values('%s','%s')" %(i,j))
table_list_Places.commit()