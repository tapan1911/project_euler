import time
start=time.time()
count=0
for j in range(1,22):
	for k in range(1,10):
		temp=k**j
		x=str(temp)
		y=len(x)
		if(y==j):
			count+=1
		
elapsed=time.time()-start
print "Ans = ",count
print "Time taken to find the result =  %s seconds"%elapsed
