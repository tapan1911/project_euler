import time
start=time.time()
total=0
for i in range(1,1001):
	total=total+i**i

x=str(total)
y=len(x)-10
s=x[y:]
elapsed=time.time()-start
print "Ans = ",s
print "Time taken to find the result = %s seconds"%elapsed

