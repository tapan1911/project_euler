import time
start=time.time()
a=1
sum=1
for i in range(1,1000,2): 
	a=a+3*i +i+2	# nw direction elements added
	b=a-(i+1)	# sw direction elements added
	sum=sum+a+b
	
for i in range(3,1002,2): 
	c=i*i		# ne direction elements added
	sum=sum+c
	d=i*i-3*(i-1)	# se direction elements added
	sum=sum+d

elapsed=time.time()-start
print "Ans = ",sum
print "Time taken to find the result = %s seconds"%elapsed

	

