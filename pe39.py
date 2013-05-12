import time
import math
start=time.time()
sol=[]
for p in range(100,1001,2):
	count=0 
	for a in range(1,int(p/2)):
		b=float((p*p-2*p*a)/(2*p-2*a))
		if(math.ceil(b)==b):
			c=p-a-b
			if(c*c==a*a+b*b):
				count+=1
				

	sol.append(count)

maximum=0
for i in range(0,450):
	if(sol[i]>maximum):
		maximum=sol[i]
		index=i


ans=(index+50)*2
elapsed=time.time()-start
print ans
print "time taken to find the result is %s seconds"%elapsed
		
		
