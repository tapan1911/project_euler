sum1=0
a=[1]
a[0]=2
count=1
for i in range(3,200000):
	flag=0
	for j in range(0,count):
		if(i%a[j]==0):
			flag=1
			break
	
	if(flag==0):
		a.append(i)
		count+=1
	
	if(count==10001):
		print a[10000]
		break		

