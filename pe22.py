import sys
a=[][]
f=open('names.txt','r')
total=0

while(1):
	c=f.read(1)
	if(c=="\""):
		ch=f.read(1)
		while(ch!="\""):
			a.append(ch)


	if(c==EOF):
		sys.exit(0)	
