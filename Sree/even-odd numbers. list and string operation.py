test=[]
def singlenumbertype(num):
    num = int(num)
    if num % 2 == 0:
        num_ret= str(num)+"its an even number"
        
    else:
        num_ret= str(num)+"it's a odd number"
    return num_ret




list_temp = range(200,301)

a = open(r'temp1.txt','w')


for i in list_temp:
    t=singlenumbertype(i)
    a.write("\n"+str(t))

