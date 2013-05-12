import sys

a=[1000000]
a={0}
count=1
for i in range(100000,1000000):
	while(i!=1):
		if(i%2==0):
			i=i/2
			count+=1

		else:
			i=3*i+1
			count+=1
	a[i]=count
	count=1

z=max(a)
for i in range(100000,1000000):
	if(a[i]==z):
		print i
		sys.exit()


