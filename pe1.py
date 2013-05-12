import time
start=time.time()
sum=0

i=3
while i<1000:
	sum=sum+i
	i=i+3

i=5
while i<1000:
	sum=sum+i
	i=i+5 

	
i=15
while i<1000:
	sum=sum-i
	i=i+15

print sum

elapsed=(time.time()-start)
print "Result found in %s seconds"%elapsed
