import time
start=time.time()

b=[]
def main():
	for i in range(12,99):
		for j in range(102,988):
			if(i*j<9999):
				x=str(i)
				data=''
				if(int(x[0])!=int(x[1])):
					data+=x
					x=str(j)
					if(int(x[0])!=int(x[1]) and int(x[0])!=int(x[2]) and int(x[1])!=int(x[2])):
						data+=x
						temp=i*j
						x=str(temp)
						if(int(x[0])!=int(x[1]) and int(x[0])!=int(x[2]) and int(x[0])!=int(x[3]) and int(x[1])!=int(x[2]) and int(x[1])!=int(x[3]) and  int(x[2])!=int(x[3])):
							data+=x
							z=sorted(data)
							data=''
							for k in z:
								data+=k
			
							if(data=='123456789'):
								if(x not in b):
									b.append(x)



	for i in range(2,10):
		for j in range(1023,4988):
			if(i*j>9999):
				break	
			
			data=''
			x=str(j)
			data+=x+str(i)
                        if(int(x[0])!=int(x[1]) and int(x[0])!=int(x[2]) and int(x[0])!=int(x[3]) and int(x[1])!=int(x[2]) and int(x[1])!=int(x[3]) and  int(x[2])!=int(x[3])):
                        	temp=i*j
				x=str(temp)
				if(int(x[0])!=int(x[1]) and int(x[0])!=int(x[2]) and int(x[0])!=int(x[3]) and int(x[1])!=int(x[2]) and int(x[1])!=int(x[3]) and  int(x[2])!=int(x[3])):
					data+=x
                                       	z=sorted(data)
                                        data=''
                                      	for k in z:
                                        	data+=k

                                       	if(data=='123456789'):
                                        	if(x not in b):
                                                	b.append(x)

if __name__=='__main__':
	main()

sum=0
for a in b:
	sum+=int(a)

elapsed=time.time()-start
print "Ans = ",sum
print "Time taken to find the result is %s seconds"%elapsed
								
								
