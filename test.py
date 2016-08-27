import bef

prime_match=[100,200,300,900]
expected_count=[50,100,150,450]

test_value=100
print "i added this"
print "i also added this"
count = bef.generate_prime(test_value)
t=prime_match.index(test_value)
h = expected_count[t]
print h
if count == h:
	print "Test passed"
else:
	print "test failed"


