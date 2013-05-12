import math
global a
global b
b=[]
a=[]
def swap (x,y):
	temp =a[x]
    	a[x] = a[y]
    	a[y] = temp

def permute(a,i,n):
	if (i == n):
		data=""
		for k in range(0,10):
			data+=str(a[k])
		z=int(data)
		b.append(z)
	#	for k in range(0,10):
	#		print a[k],	
	#	print "\n"	
	else:
        	for j in range (i,n+1):
  			swap(i,j)
          		permute(a, i+1, n)
          		swap(i,j)


for i in range(0,10):
	a.append(i)

permute(a, 0, 9)
print b[1]


