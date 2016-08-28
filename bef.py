

def generate_prime(value):
	j=0
	for i in range(0,value):
		if i%2 == 0:
			#print "This is even",i
			j = j+1
	return j

#print generate_prime(100)

