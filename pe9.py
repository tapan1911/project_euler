for a in range(1,1000):
	for b in range(a,1000):
		c=1000-a-b
		z=a*a+b*b
		if (z==c*c):
			print a,b,c
			p=a*b*c
			print p
