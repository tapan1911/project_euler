a=[]
for i in range(0,1000000):
	a.append(1)

a[0]=0
a[1]=0
for i in range(2,1000000):
	if(a[i]==1):
		for j in range(2*i,1000000,i):
			a[j]=0
	
