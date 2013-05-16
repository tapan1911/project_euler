import math
import time
start=time.time()
x = (math.factorial(23))/(math.factorial(11)*math.factorial(12))
n=23
r=11
count=4
temp=x
n+=1
while(n<=100):
	if(n%2==0):
		r=n/2
		temp=(temp*n)/r
		if(temp>1000000):
			count+=1
	
		temp1=(temp*r)/(n-r+1)
		while(temp1>1000000):
			count+=2
			r=r-1
			temp1=(temp1*r)/(n-r+1)
			
	
	if(n%2!=0):
		r=(n+1)/2
		temp=(temp*n)/r
		temp1=temp
		while(temp1>1000000):
			count+=2
			r=r-1
			temp1=(temp1*r)/(n-r+1)
		

	n+=1

elapsed=time.time()-start
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed
			
