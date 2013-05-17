import time
start=time.time()
f=open("names.txt",'r')
 
for x in f:
	data=x

j=0
y=len(data)
flag=0
b=[]
txt=''
while 1:
	if(data[j]=="\""):
		if(flag==0):
			flag+=1
		else:
			b.append(txt)
			flag=0
			txt=''
	
	if(ord(x[j])-ord('A')>=0 and ord(x[j])-ord('A')<=26):
		txt=txt+x[j]	

	j+=1
	if(j==y):
		break


b.sort()
y=len(b)
total=0
for i in range(0,y):
	x=b[i]
	sum=0
	for z in x:
		sum=sum+ord(z)-ord('A')+1
	sum=sum*(i+1)
	total=total+sum

elapsed = time.time() - start
print "Ans = ",total
print "Time taken to find the result = %s seconds"%elapsed

