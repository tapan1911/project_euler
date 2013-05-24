from time import time
start=time()

a=[]	
a.append(0)
a.append(0)
for i in range(2,1000000):
	a.append(1)
	
b=[]
for i in range(3,1000000):
	x=str(i)
	y=len(x)
	for z in x:
		k=int(z)
		if(k==2 or k==4 or k==6 or k==8):
			a[i]=0
			break
	

	
for i in range(2,1000000):
	
	if(a[i]==1):
		b.append(i)
	
	j=2
	while 1:
		temp=i*j
		if(temp>999999):
			break
		a[temp]=0
		j+=1

count=0
c=[]
for x in b:
	if(x not in c):
		y=str(x)
		z=len(y)
		y=y[z-1:]+y[:z-1]
		flag=0
		while(int(y)!=x):
			if(int(y) not in b):
				flag=1
				break
			

			y=y[z-1:]+y[:z-1]
	
		if(flag==0):
			count+=1		
			y=y[z-1:]+y[:z-1]
			while(int(y)!=x):
				count+=1
				c.append(int(y))
				y=y[z-1:]+y[:z-1]

	

elapsed=time()-start
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed
		
