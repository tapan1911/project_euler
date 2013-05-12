import math
import time
a=[]
b=[]

start=time.time()
for i in range(10,100):
	for j in range(i+1,100):
		rem1=i%10
		rem2=j%10
		tens1=i/10
		tens2=j/10
		if(rem1==rem2 and rem1!=0):
			if((float(tens1)/tens2)==(float(i)/j)):
				a.append(tens1)
				b.append(tens2)
		if(rem1==tens2  and rem2!=0):
			if((float(tens1)/rem2)==(float(i)/j)):
                                a.append(tens1)
                                b.append(rem2)

		if(tens1==rem2):
			if((float(rem1)/tens2)==(float(i)/j)):
                                a.append(rem1)
                                b.append(tens2)

		if(tens1==tens2 and rem2!=0):
			if((float(rem1)/rem2)==(float(i)/j)):
                                a.append(rem1)
                                b.append(rem2)


num=a[0]*a[1]*a[2]*a[3]
den=b[0]*b[1]*b[2]*b[3]
limit=int(math.ceil(math.sqrt(num)))

for i in range(2,limit):
	while(num%i==0 and den%i==0):
		num=num/i
		den=den/i

elapsed=time.time()-start

print den	
print "time taken to find the result is %s seconds"%elapsed

