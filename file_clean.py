file_name = r"C:\Users\siv\Desktop\log.txt"
new_file =r"C:\Users\siv\Desktop\cleaned.txt"

c= open(new_file,'w')

b= open(file_name, 'r')
a= b.readlines()
print a
for i in a:
	j_split = i.split(' ')
	print j_split[0],j_split[-1]
	c.write(j_split[0]+' '+j_split[1])