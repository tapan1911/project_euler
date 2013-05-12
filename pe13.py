
f=open("numbers.txt","r")
string=f.read()
string=string.split("\n")
total=0
for i in range (0,100):
	total+=int(string[i])

print total
z=str(total)
for i in range(0,10):
	print z[i],

