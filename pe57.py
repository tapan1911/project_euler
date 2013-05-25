import time
start=time.time()

num=1393
den=985
count=1
i=9

while i<=1000:
	x=num-den
	y=den
	den=2*y+x
	num=3*y+x
	a=len(str(num))
	b=len(str(den))
	if(a>b):
		count+=1
	i+=1

elapsed=time.time()-start
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed
	
