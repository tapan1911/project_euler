from itertools import *
from math import *
from operator import *
import time

start=time.time()
pentagonals = set(n*(3*n-1)/2 for n in range(1, 3000))
c = combinations(pentagonals, 2)
for p in c:
	if add(*p) in pentagonals and abs(sub(*p)) in pentagonals:
        	print abs(sub(*p))

elapsed=time.time()-start
print "Time taken to find the result = %s seconds"%elapsed

