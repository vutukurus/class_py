file_name = r"C:\Users\Sreedhar\Desktop\log.txt"
new_file =r"C:\Users\Sreedhar\Desktop\cleaned.txt"

#This is a code change for os module demo
#this is a line added to show how to checkin
#checkin- from ur local pc to repository saving..

c= open(new_file,'w')

b= open(file_name, 'r')
a= b.readlines()
print a
for i in a:
	j_split = i.split(' ')
	print j_split[0],j_split[-1]
	c.write(j_split[0]+' '+j_split[1])