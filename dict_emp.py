temp ={(1,2,3):["90","89"],"sec":"ap34","us":"89"}
temp_2 ={"a":["90","89"],"sec":"ap34","us":"89"}
#This is just a demo for git problem
print "tis is second line"
print temp.update(temp_2)
print temp

print temp["sec"]


print temp["us"]

print temp.keys()
print temp.values()

for k,v in temp.iteritems():
	print k
	print v
	