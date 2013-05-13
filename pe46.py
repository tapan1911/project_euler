import time
start=time.time()
a=[]
b=[]
a.append(0)
a.append(0)
for i in range(2,10000):
	a.append(1)

for i in range(2,10000):
	if(a[i]==1):
		b.append(i)
	
	count=2
	while(1):
		z=count*i
		if(z>9999):	
			break
		a[z]=0
		count+=1


c=[]
for i in range(1,100):
	z=i*i
	c.append(z)


j=35
while 1:
	flag=1
	for i in c:
		rem=j-2*i
		if(rem in b):
			flag=0
			break

	if(flag==1 and (j not in b)):
		print "Ans = ",j
		break
	
	j+=2

elapsed=time.time()-start
print "Time taken to find the result = %s seconds"%elapsed
	
				

