# There are 20 * 30^(n-1) 2n-digit solutions,
# No 4n+1-digit solutions,
# And 5 * 20** (25*20)**n 4n+3-digit solutions.


import time
start=time.time()

count=0
for i in range(1,10):
	if i%2==0:
  		count+=(20*(30**((i/2)-1)))
	
	elif i%4==3:
  		count+=(5*20*((25*20)**(i/4)))


elapsed=time.time()-start
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed
