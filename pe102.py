import time

start=time.time()
f=open('triangles.txt','r')
count=0

def area(x1,y1,x2,y2,x3,y3):
	x1=int(x1)
	y1=int(y1)
	x2=int(x2)
	y2=int(y2)
	x3=int(x3)
	y3=int(y3)
	area= abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
	return area

for lines in f:
	x1,y1,x2,y2,x3,y3=lines.split(',')
	a1=area(0,0,x1,y1,x2,y2)
	a2=area(0,0,x2,y2,x3,y3)
	a3=area(0,0,x3,y3,x1,y1)
	A=area(x1,y1,x2,y2,x3,y3)

	if(a1+a2+a3==A):
		count+=1

elapsed=time.time() -start
print "Ans = ",count
print "Time taken to find the result = %s seconds"%elapsed


