__author__ = 'Sreedhar'
import os

def singlenumbertype(num):
    num = int(num)
    if num % 2 == 0:
        print num,"its an even number"
    else:
        print num,"it's a odd number"
    return num

num = raw_input("please enter a number:")
singlenumbertype(num)

list = range(200,301)

a = open(r'C:\Users\Sreedhar\PycharmProjects\PracticeProrams\temp1.txt','w')

for i in list:
    print ','+str(singlenumbertype(i))
    a.write("\n str(singlenumbertype(i))")