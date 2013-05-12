import math
total=1
a=[]
a.append(0)
a.append(0)
for i in range(2,10000):
	z=int(math.floor(math.sqrt(i)))
	for j in range(2,z+1):
		if(i%j==0):
			if((j*j)!=i):
				total+=j+(i/j)
			else:
				total+=j
	
	a.append(total)
	total=1		

ans=0
for k in range(4,10000):
	l=a[k]
	if(l!=k):
		if(l<10000):
			if(a[l]==k ):
				print a[k],k,"\n"
				ans=ans+k+a[k]
				a[k]=0


print ans
			
		
