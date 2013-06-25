import time

start = time.time()
min = 99999
for i in range(40,2000):
	for j in range(1,50):
		temp = 2000000 - (i*j*(i+1)*(j+1))/4
		temp1 = i*j
		if(temp<min and temp >0):
			min = temp
			mina = temp1

elapsed = time.time() - start
print "Ans = ",mina
print "Time taken to find the result = %s seconds"%elapsed
