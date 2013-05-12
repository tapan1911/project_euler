import math
i=1
product=1
const=9
while (1):
	j=i
	count=1
	digit=1
	
	while(1):
		j=j-count*const*digit
		if(j<0):
			j=j+count*const*digit
			break
		count=count*10
		digit=digit+1
	
	print "j=",j
	temp=(digit-1)*10
	qo=j/digit
	temp=temp+qo
	rem=j%digit
	print "rem=",rem
	temp=temp/pow(10,digit-rem-1)
	temp=temp%10
	product=product*temp
	print product
	if(i==1000000):
		break
	i=i*10
	

print product
