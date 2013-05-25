import time
start=time.time()

a=[]
b=[]
a.append(0)
a.append(0)
for i in range(2,10000):
	a.append(1)

for i in range(2,10000):
	if(a[i]==1):
		x=str(i)
		y=len(x)
		if(y==4):
			b.append(i)
		
	j=2
	while 1:
		temp=j*i
		if(temp>9999):
			break
		a[temp]=0
		j+=1


c=[]
x=len(b)
for i in range(0,x):
	for j in range(i+1,x):
		z=b[j]-b[i]
		k=b[j]+z
		if(k>9999):
			break
		if(k in b):
			c.append(b[i])
			c.append(b[j])
			c.append(k)
		
cnt=0			
z=len(c)
for i in range(0,z,3):
	data=str(c[i])
	data1=str(c[i+1])
	data2=str(c[i+2])
	datai=sorted(data)
	dataj=sorted(data1)
	datak=sorted(data2)
	data=''
	data1=''
	data2=''
	for j in range(0,4):
		data+=datai[j]
		data1+=dataj[j]
		data2+=datak[j]
	
	if(int(data)==int(data1) and int(data1)==int(data2)):
		data=''
		data+=str(c[i])+str(c[i+1])+str(c[i+2])
		if(int(data)!=148748178147):
			print "Ans = ", data
		cnt+=1
		if(cnt==2):
			break
	
elapsed=time.time()-start
print "Time taken to find the result = %s seconds"%elapsed

