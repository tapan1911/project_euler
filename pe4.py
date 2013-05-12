number=[]

for a in range (100,1000):
	for b in range(100,1000):
		z=str(a*b)
		if z==z[::-1]:
			number.append(int(z))

print (max(number))
