import csv

file_name = open('MSeventviewer.csv','r')

read_file = csv.reader(file_name)

csv_w_error = open('sree_Error.csv','w')
error_fields = csv.writer(csv_w_error)
error_fields.writerow(('Level','Date and Time','Source','Event ID','Task Category',' '))

csv_w_Warning= open('sree_Warning.csv','w')
Warning_fields = csv.writer(csv_w_Warning)
Warning_fields.writerow(('Level','Date and Time','Source','Event ID','Task Category',' '))

for i in read_file:
	if i[0] == "Error":
		error_fields.writerow(tuple(i))
	elif i[0] == "Warning":
		Warning_fields.writerow(tuple(i))
		

