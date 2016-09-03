#CSV file reading
#700
#Doc
import csv
f= open('book.csv','r') #read mode

read = csv.reader(f)
print type(read)

#import pdb;pdb.set_trace()
csv_w = open('book_cleaned.csv','w') #write mode
test = csv.writer(csv_w)
for i in read:
	print tuple(i)[0:3:2]
	test.writerow(tuple(i)[0:3:2])


