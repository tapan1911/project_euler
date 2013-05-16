import time
start=time.time()
count=0
for i in range(5,10000):
	j=1
	flag=0
	k=i
	while j<=50:
		x=str(k)
		y=x[::-1]
		z=int(x)+int(y)
		a=str(z)
		if(a==a[::-1]):
			flag=1
			break
		k=int(a)		
		j+=1
	
	if(flag==0):
		count+=1

elapsed=time.time()-start
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed
		

