import time
a=[]
a=(0,31,28,31,30,31,30,31,31,30,31,30,31)

day=2
count=0
start=time.time()
for i in range(1901,2001):
	for j in range(1,13):
		if(j==2):
			if(i%4!=0):
				day=day
					
			else:
				if(i%100==0):
					if(i%400 == 0):
						day+=1
					else:
						day=day
				else:
					day+=1

			if(day%7==0):
                                        count+=1
                                        day=0
			if(day>7):
					day=day%7

			
			
		else:
			day+=a[j]%7
			if(day%7==0):
				count+=1
				day=0
			if(day>7):
				day=day%7
					
elapsed=time.time()-start			
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed
			


