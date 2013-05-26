import time

start=time.time()
count=50*50*3

def gcd(i,j):		# i am keeping i to be always greater than j
	while 1:
		if(j>i):
			temp=i
			i=j
			j=temp
		temp=i%j
		if(temp==0):
			return j
		i=j
		j=temp

for i in range(1,51):
	for j in range(1,51):
		x=i
		y=j
		z=gcd(i,j)
		slopey=i/z
		slopex=j/z
		while 1:
			x=x+slopex
			y=y-slopey
			if(y>=0 and x<=50):
				count+=2
			else:
				break	
	

elapsed=time.time()- start
print "Ans = ",count	
print "Time taken to find the result = %s seconds"%elapsed
