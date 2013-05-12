triangle=set((n*(n+1)/2) for n in range(40755,100000))
pentagonal=set(n*(3*n-1)/2 for n in range(165,100000))
hexagonal=set(n*(2*n-1) for n in range(143,100000))

for i in triangle:
	if(i in pentagonal and i in hexagonal):
		print "Ans= ",i
		break
		
