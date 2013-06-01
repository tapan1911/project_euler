import time

def is_bouncy(n):
	x=str(n)
	y=len(x)
	inc=False
	dec=False
	for i in range(y-1):
		if(x[i]>x[i+1]):
			dec=True
		elif(x[i]<x[i+1]):
			inc=True
		if(inc and dec):
			return True
	return False

count=9*2178
n=21781
start=time.time()

while 1:
	if(is_bouncy(n)):
		count+=1
	
	per=(float(count)/n)*100
	if(per==99.0):
		break
	n+=1


elapsed=time.time()-start
print "Ans = ",n
print "Time taken to find the result = %s seconds"%elapsed
			
			
	
		
