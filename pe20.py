import math
z=math.factorial(100)

total=0
while z!=0:
	total=total+z%10
	z=z/10

print total
