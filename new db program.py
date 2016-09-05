#get list of two places files and store them in a database

import os
import sqlite3

place1 = raw_input("enter path for place 1:")
place2 = raw_input("enter path for place 2:")

table_list_Places = sqlite3.connect("places.db")
table_list_Places.execute("create table lists(place1 text,place2 text)")

place1_lists = os.listdir(place1)
place2_lists = os.listdir(place2)

insert into lists(place1,place2) values(1,test)

"""
for i in place1_lists:
	for j in place2_lists:
		insert into lists(i,j) values (i,j)
"""