import time

print ""
print "################# Brute Force #####################"
start = time.time()
total=0

for a in range(3,1001):
	max=2
	if(a%2==0):
		for n in range(1,a,2):
			rem=2*a*n
			if(rem>=a*a):
				rem=rem%(a*a)
			if(rem>max):
				max=rem
	
	elif(a%2!=0):
		for n in range(1,a):
                        rem=2*a*n
                	if(rem>a*a):                            
                        	rem=rem%(a*a)
                	if(rem>max):
                        	max=rem 	
	total+=max	


elapsed=time.time()-start
print "Ans = ",total
print "Time taken to find the result is %s seconds"%elapsed

print ""
print "################ ANTERNATE SOLUTION ###################"	

# even value of n leave a remainder 2 and odd values of n leave a remainder 2*a*n for every value of a
# We have to make 2*n as close to a as possible, hence
# Rem(a is odd) = a*(a-1) ,, Rem(a is even) = a*(a-2)

start=time.time()
total=0
for a in range(3,1001):
	if(a%2==0):
		total+=a*(a-2)
	elif(a%2!=0):
		total+=a*(a-1)

elapsed=time.time()-start
print "Ans = ",total
print "Time taken to find the result is %s seconds"%elapsed

