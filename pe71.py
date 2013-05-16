import time
start=time.time()
a=0.0
b=1
c=1.0
d=1
x=0
y=0
j=1
while j<=10:
	temp1=x
	temp2=y
	x=a+c
	y=b+d
	if(y>1000000):
		break

	if(x==3.0 and y==7):
		c=x
		d=y

	if(x/y >3.0/7):
		c=x
		d=y
		
	if(x/y<3.0/7):
		a=x
		b=y
		


elapsed=time.time()-start
print "Ans = ",int(temp1)
print "Time taken to find the result = %s seconds"%elapsed
