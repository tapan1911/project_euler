import time
start=time.time()
sum=0
for i in range(1,1000000):
	x=str(i)
	if(x==x[::-1]):
		y=bin(i)
		z=len(y)
		data=''
		for j in range(2,z):
			data=data+y[j]

		if(data==data[::-1]):
			sum=sum+i

elapsed=time.time()-start
print "Ans = ",sum
print "Time taken to find the result = %s seconds"%elapsed
