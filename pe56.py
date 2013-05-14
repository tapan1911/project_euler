import time
start=time.time()
a=[]
for i in range(1,101):
	for j in range(1,101):
		k=i**j
		a.append(k)

b=[]
for x in a:
	y=str(x)
	z=len(y)
	temp=0
	for i in range(0,z):
		temp=temp+int(y[i])
	
	b.append(temp)


ans=max(b)
elapsed=time.time()-start
print "Ans = ",ans
print "Time taken to find the result = %s seconds"%elapsed

