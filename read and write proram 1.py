__author__ = 'Sreedhar'

import os

get_files = os.listdir(r'C:\Users\Sreedhar\Desktop')

a = open(r'C:\Users\Sreedhar\PycharmProjects\PracticeProrams\prg1.txt','w')


for i in get_files:
    a.write(i+'\n')

file_name = r'C:\Users\Sreedhar\PycharmProjects\PracticeProrams\prg1.txt'
print file_name
b = open(file_name,'r')
c = b.readlines()
for i in c:
    print i