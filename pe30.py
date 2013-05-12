'''
Main problem is to decide how far we go in loop
1 < 4 digit no < 9^5*4=236196 possible
1 < 5 digit no < 9^5*5=295245 possible
1 < 6 digit no < 9^5*6=354294 only uptil here will we go
1 < 7 digit no < 9^5*7=413343 not possible
'''

ans=0
for i in range(2,354294):
	total=0
	j=i
	while(j!=0):
		rem=j%10
		total=total+pow(rem,5)
		j=j/10
	if(total==i):
		ans=ans+total

print ans

