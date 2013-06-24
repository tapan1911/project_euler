import time

n, d, i = 2, 1, 100
start = time.time()
while i>0:
  	c = 1
  	if i%3 == 0: c = 2*i/3
  	n, d, i = d, c*d+n, i-1

print "Ans = ", sum(int(i) for i in str(d))
elapsed = time.time() - start
print "Time taken to find the result = %s seconds"%elapsed
