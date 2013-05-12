import time
start=time.time()
count=1
for i in range(0,201,100):
	for j in range(0,201,50):
		if(i+j>200):
			break
		for k in range(0,201,20):
			if(i+j+k>200):
        	                break
	
			for l in range(0,201,10):
				if(i+j+k+l>200):
        		                break
	
				for m in range(0,201,5):
					if(i+j+k+l+m>200):
        			                break
	
					for n in range(0,201,2):
						if(i+j++k+l+m+n>200):
        				                break
	
						if(i+j+k+l+m+n<=200):
							count+=1

elapsed=time.time()-start
print count
print "time taken to find the result is %s seconds"%elapsed
