import time
start=time.time() 
list = []
for a in range(2, 101):
        for b in range(2, 101):
                product = a ** b
                list.append(product)
list.sort()
newlist = set(list)
elapsed=time.time()-start
print "Ans = ",len(newlist)
print "Time taken to find the result = %s seconds"%elapsed

