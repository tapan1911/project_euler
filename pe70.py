import time
import math

start = time.time()
first = int(math.sqrt(10000000))-1000
last = int(math.sqrt(10000000))+1000

a = []
a.append(0)
a.append(0)
for i in range(2,last):
	a.append(1)

b = []
for i in range(2,last):
	if(a[i]==1):
		b.append(i)
		j = 2
		while 1:
			temp = j*i
			if(temp>last-1):
				break
			a[temp] = 0
			j+=1
		
total = len(b)
c = []
d = []
i = total-1
while (b[i]>first):
	j = i-1
	while(b[j]>first):
		temp = b[i]*b[j]
		temp1 = (b[i]-1)*(b[j]-1)
		if(sorted(str(temp))==sorted(str(temp1))):
			c.append(temp)
			d.append(temp1)
		j-=1
	i-=1
	
min = 999		
for i in range(len(c)):
	temp = float(c[i])/d[i]
	temp1 = c[i]
	if(temp <min and temp1<10000000 ):
		min = temp
		result = c[i]

elapsed = time.time() - start
print "Ans = ",result
print "Time taken to find the result = %s seconds"%elapsed
						 
