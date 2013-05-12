import time
start=time.time()
a=[]
b=[]
a.append(0)
a.append(0)
for i in range(2,1000):
	b[:]=[]
	j=1
	flag=0
	while(1):
		while(j<i):
			j=j*10
	
		rem=j%i
		if(rem!=0):
			count=0
			for k in b:
				if(k==rem):
					flag=1
					a.append(len(b)-count)
					break
				count+=1
					
			if(flag==0):	
				b.append(rem)
			if(flag==1):
				break
			j=rem
		else:
			a.append(0)
			break

max=0
for i in range(2,1000):
	if(a[i]>max):
		max=a[i]
		index=i

elapsed=time.time() - start
print index
print "time taken to get the result is %s seconds"%elapsed
