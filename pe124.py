import time

start=time.time()
a=[]
a.append(0)
a.append(0)
for i in range(1,100000):
	a.append(1)

b=[]
for i in range(2,100000):
	if(a[i]==1):
		b.append(i)
	
	j=2
	while 1:
		temp=j*i
		if(temp>99999):
			break
		a[temp]=0
		j+=1

rad=[]
rad.append(0)
for i in range(1,100001):
	rad.append(1)

for x in b:
	j=1
	while 1:
		temp=x*j
		if(temp>100000):
			break
		rad[temp]=rad[temp]*x
		j+=1

index=[i[0] for i in sorted(enumerate(rad),key=lambda x:x[1])]

elapsed=time.time()-start
print "Ans = ",index[10000]	
print "Time taken to find the result = %s seconds"%elapsed
