import time
start=time.time()

a=[]
b=[]
max=918273645
i=91
j=100
while i<j:
	k=1
	flag=0
	while(len(a)!=9):
		temp=i*k
		x=str(temp)
		for y in x:
			if(int(y)==0):
                        	flag=1
                               	break

			if(y not in a):
				a.append(y)
			else:	
				flag=1
				break
		
		if(flag==1):
			break
		
		k+=1
	
	if(flag==0):
		data=''
		for k in range(0,9):
			data+=a[k]
		b.append(int(data))
	a=[]
	i+=1


i=912
j=988
while i<j:
        k=1
        flag=0
        while(len(a)!=9):
                temp=i*k
                x=str(temp)
                for y in x:
			if(int(y)==0):
				flag=1
				break
                        if(y not in a):
                                a.append(y)
                        else:
                                flag=1
                                break

                if(flag==1):
                        break

                k+=1

        if(flag==0):
                data=''
                for k in range(0,9):
                        data+=a[k]
                b.append(int(data))
        a=[]
        i+=1


i=9123
j=9877
while i<j:
        k=1
        flag=0
        while(len(a)!=9):
                temp=i*k
                x=str(temp)
                for y in x:
			if(int(y)==0):
                                flag=1
                                break

                        if(y not in a):
                                a.append(y)
                        else:
                                flag=1
                                break

                if(flag==1):
                        break

                k+=1

        if(flag==0):
                data=''
                for k in range(0,9):
                        data+=a[k]
                b.append(int(data))
        a=[]
        i+=1


for x in b:
	if(x>max):
		max=x

elapsed=time.time()-start
print "Ans = ",max
print "Time taken to find the result = %s seconds"%elapsed
		

