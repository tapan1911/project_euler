i=1
j=2
sum=2           #this is done because we are starting to check from 3 so we have left 2

while 1:
	temp=i+j;
	if temp>4000000:
		break
	if(temp%2==0):
		sum=sum+temp	

	i=j
	j=temp

print sum

