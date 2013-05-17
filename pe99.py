from math import log
from time import time

mv,ml,ln = 0,0,0
start = time()

for line in file('base_exp.txt'):
	ln+=1
	b,e = line.split(',')
	v = int(e) * log(int(b))
	if(v>mv):
		mv,ml = v,ln

elapsed = time() - start
print "Ans = ",ml
print "Time taken to find the result = %s seconds"%elapsed
 
