import time

start = time.time()
a=[]
a.append(0)
a.append(0)
for i in range(2,250000):
	a.append(1)

b=[]
for i in range(2,250000):
	if(a[i]==1):
		b.append(i)
		
	j=2
	while 1:
		temp=j*i
		if(temp>249999):
			break
		a[temp]=0
		j+=1
	
n=7039
while 1:
	rem = (2*n*b[n-1])%(b[n-1]*b[n-1])
	if(len(str(rem))>10):
		break
	
	n+=2

elapsed = time.time()- start
print "Ans = ",n
print "Time taken to find the result = %s seconds"%elapsed
	
	

