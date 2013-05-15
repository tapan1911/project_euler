import time
start=time.time()
a=2
temp=a
for i in range(1,7830457):
	temp=(temp*a)%10000000000
	
temp=(temp*28433)%10000000000
temp+=1

elapsed=time.time()-start
print "Ans = ",temp
print "Time taken to find the result = %s seconds"%elapsed

