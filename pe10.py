a=[]
b=[]
for i in range(0,2000000):
        if(i==0 | i==1):
                a.append(0);
        else:
                a.append(1);

for i in range (2,2000000):
        if(a[i]==1):
                b.append(i);
		for j in range(2,1000000):
			z=i*j;
			if(z<2000000 ):
				a[z]=0;
			else:
				break;

total=0;
for i in range(2,2000000):
	if(a[i]==1):
		total=total+i;
	
print total


