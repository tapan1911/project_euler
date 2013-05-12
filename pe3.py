number =600851475143
max=0
i=2
while number!=1:
	if number%i==0:
		if i>max:
			max=i;
		number=number/i
	else:
		i=i+1	

print max				
