import time
from decimal import getcontext, Decimal

start=time.time()
getcontext().prec = 102
squares = set(i*i for i in range(2,10))
 
total = 0
for z in range(2,100):
	if z in squares: continue
    	q = str(int(Decimal(z).sqrt()*10**99))
 
    	for x in q:
		total+=int(x)

elapsed=time.time()-start 
print "Ans = ",total
print "Time taken to find the result = % seconds"%elapsed

