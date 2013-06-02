import time

start = time.time()
a=[]
a.append(0)
a.append(0)
for i in range(2,100000):
	a.append(1)

b=[]
for i in range(2,100000):
	if(a[i]==1):
		b.append(i)
	j=2
	while 1:
		temp=j*i
		if(temp>99999):	
			break
		a[temp]=0
		j+=1

count=[]
for i in range(0,200000):
		count.append(0)

for x in b:
	j=1
	while 1:
		temp=j*x
		if(temp>199999):
			break

		count[temp]+=1
		j+=1

From = 644
while  From<200000:
	if (count[From]==4):
		if(count[From+1]==4):
			if(count[From+2]==4):
				if(count[From+3]==4):
					break
				else:
					From+=4
			else:
				From+=3
	
		else:
			From+=2
	else:
		From+=1

elapsed = time.time()-start
print "Ans = ",From
print "Time taken to find the result = %s seconds"%elapsed
