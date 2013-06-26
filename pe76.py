import time

start = time.time()
ways = [1]+[0]*100
 
for n in range(1,100):
  for i in range(n, 101):
    ways[i] += ways[i-n]
 
elapsed = time.time() - start
print "Ans = ", ways[100]
print "Time taken to find the result = %s seconds"%elapsed

