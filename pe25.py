import sys
a=[]
a.append(0)
a.append(1)
a.append(1)
i=3
while(i>=3):
	z=a[i-1]+a[i-2]
	if(len(str(z))==1000):
		print i
		sys.exit(0)
	a.append(z)
	i+=1
	
		
