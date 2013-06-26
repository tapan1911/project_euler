import time

start = time.time()
a = [1,2,5,10,20,50,100,200]
b = [1] + [0]*200
for n in a:
        for i in range(n,201):
                b[i]+= b[i-n]

elapsed = time.time() - start
print "Ans = ",b[200]
print "Time taken to find the result = %s seconds"%elapsed
