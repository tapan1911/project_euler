import time
start= time.time()
a = []
flag=0
n = 30  #tested up to n = 220
for b in range(2, 600):
	for e in range(2, 50):
     		p = b**e
		x=str(p)
		sumod=0
		for y in x:
			sumod=sumod+int(y)

     		if sumod == b: 
			a.append(p); 
     	
		if len(a)>n*1.5: 
			flag=1
			break
	
	if(flag==1):
		break
a.sort()
elapsed=time.time()-start
print "Ans = ",a[n-1]
print "Time taken to find the result = %s seconds"%elapsed
