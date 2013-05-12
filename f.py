#import itertools
#print list(itertools.permutations([1,2,3,4], 4))
import math
from itertools import islice, permutations
b=[]
for i in range(0,math.factorial(
print ''.join(next(islice(permutations(map(str, range(10))),1, None)))
