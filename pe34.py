import math
import time
start=time.time()
ans=0
for i in range(10,2540160):
	total=0
	j=i
	while(j!=0):
		rem=j%10
		total=total+math.factorial(rem)
		j=j/10
	
	if(total==i):
		ans+=total

print ans	
elapsed=(time.time()-start)
print "Result found in %s seconds"%elapsed
