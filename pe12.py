import math
import sys
global a
a=[]

for i in range(0,10000):
        a.append(0)

def factors(zz):
	limit=int(math.floor(math.sqrt(zz)))
	for i in range(2,limit+1):
		if(zz%i==0):
			while(zz%i==0):
				a[i]+=1
				zz=zz/i

i=1
divisors=1
while i>=1 :
	z= (i*(i+1))/2
	factors(z)
	limit=int(math.floor(math.sqrt(z)))
	for j in range(2,limit+1):
		if(a[j]>0):
			divisors*=(a[j]+1)
	
	if(divisors>500):
		print z
		sys.exit(0)
	
	divisors=1
	
	for j in range(0,10000):
	        a.append(0)

	i+=1




	
				
			







