import time

start=time.time()
a=[]
a.append(0)
a.append(0)

for i in range(2,800000):
	a.append(1)


b=[]
c=[]
for i in range(2,800000):
	if(a[i]==1):
		c.append(i)
		x=str(i)
		y=len(x)
		flag=0
		if(int(x[0])==4 or int(x[0])==6 or int(x[0])==8 or int(x[0])==1):
			flag=1
			
		
		if(int(x[y-1])==1):
			flag=1
		
		for j in range(1,y):
			if(int(x[j])==2 or int(x[j])==4 or int(x[j])==5 or int(x[j])==6 or int(x[j])==8 or int(x[j])== 0):
				flag=1
				break
		
			
			
		if(flag==0):
			b.append(i)
		
		j=2
		while 1:
			temp=j*i
			if(temp>799999):
				break
			a[temp]=0
			j+=1

	
''''
c=[]
for i in range(2,800000):
	if(a[i]==1):
		c.append(i)

'''
tp=[]
for i in b:
	j=i
	flag=0
	temp=j/10
	while temp!=0:
		if(temp not in c):
			flag=1
			break				
		temp=temp/10
	
	if(flag==0):
		k=10
		temp=j%k
		while temp!=j:
			if(temp not in c):
				flag=1
				break

			k=k*10
			temp=j%k

	if(flag==0):
		tp.append(i)	
	
sum=0	
for i in range(4,15):
	sum=sum+tp[i]

elapsed=time.time()-start
print "Ans = ",sum
print "Time taken to find the result = %s seconds"%elapsed





		
	

		
