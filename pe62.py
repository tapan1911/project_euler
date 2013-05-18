from collections import defaultdict
import time

def cube(x): return x**3

start=time.time()
cubes = defaultdict(list)
for i in range(10000):
	c = cube(i)
        digits = ''.join(sorted([d for d in str(c)]))
	cubes[digits].append(c)
    
print "Ans = ",min([min(v) for  k,v in cubes.items() if len(v) == 5])
elapsed=time.time()-start
print "Time taken to find the result = %s seconds"%elapsed

