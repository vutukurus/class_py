import os
file_name = r"C:\Users\Sreedhar\Desktop\class_py\logsss.txt"
new_file = r"C:\Users\Sreedhar\Desktop\class_py\sree_cleaned.txt"

c = open(new_file,'w')

b = open(file_name,'r')

a = b.readlines()
first_lines = b.readline()
print first_lines
headings = []
for i in first_lines:
	print i
	headings.append(i)
	print "==========="
print headings
	
