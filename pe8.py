f = open('pe8_data', 'r')      # file pointer to read the file

z=f.read()
data=""
for i in z:
	if(i!='\n'):
		data+=i

largest=0
for i in range(0,995):
	temp=data[i:i+5]
	total=1
	for j in temp:
		total*=int(j)
	if(total>largest):
		largest=total

print largest

f.close()
