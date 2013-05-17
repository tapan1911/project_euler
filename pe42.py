import time
start=time.time()
triangle = set(n*(n+1)/2 for n in range(1,3000))
f=open("words.txt",'r')

for x in f:
	data=x

y=len(data)
j=0
count=0
flag=0
total=0

while 1:
	if(x[j]=="\""):
		if(flag==0):
			flag+=1
		if(flag==1):
			flag=0
			if(total in  triangle):
				count+=1
			total=0
	
	if(ord(x[j])-ord('A')>=0 and ord(x[j])-ord('A')<=26):
		total+= ord(x[j]) - ord('A') + 1
	
	j+=1
	if(j==y):
		break
elapsed=time.time()-start
print "Ans = ",count		
print "Time taken to find the result = %s seconds",elapsed
			
