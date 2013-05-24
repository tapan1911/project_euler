#finding all the abundant numbers
import time

start=time.time()
sumi=[]
sumi.append(0)
sumi.append(0)
for i in range(2,28124):
	sumi.append(1)

for i in range(2,14062):
	j=2
	while 1:
		temp=j*i
		if(temp>28123):
			break
		sumi[temp]+=i
		j+=1

abn=set()
s=0
for n in range(1,28124):
	if(sumi[n]>n):
		abn.add(n)		
	if not any( (n-a in abn) for a in abn ):
   		 s += n
	

elapsed=time.time()-start
print "Ans = ",s
print "Time taken to find the result = %s seconds"%elapsed

