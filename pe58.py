import time
import math

def is_prime(num):
	if(num%2==0):
		return False
	i=3
	limit = int(math.sqrt(num+1))
	while i<=limit:
		if(num%i==0):
			return False
		else:
			i+=2
	return True
	


start = time.time()
ne=3
nw=5
sw=7
n=3
count=3
while 1:
        ne=ne+(n-1)*3+n+1
        nw=ne+(n+1)
        sw=nw+(n+1)
        n=n+2
        if is_prime(ne):
                count+=1
        if is_prime(nw):
                count+=1
        if is_prime(sw):
                count+=1

        per=(count*100)/(2*n-1)
        if(per<10):
                break

elapsed = time.time() - start        
print "Ans = ",n
print "Time taken to find the result = %s seconds"%elapsed

