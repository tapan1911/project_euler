#include<stdio.h>
#include<stdlib.h>

int main()
{
	int i,j,temp,b[1000001],maxi;
	float a[1000001],max;
	for(i=0;i<1000001;i++)
		a[i] = i;
	
	b[0] = 0;
 	b[1] = 0; 	
	for(i=2;i<1000001;i++)
		b[i] = 1;
	
	for(i=2;i<1000001;i++)
	{
		if(b[i]==1)
		{
			j = 1;
			while (1)
			{
				temp = j*i;
				if(temp>1000000)
					break;
				a[temp]-=a[temp]/i;
				b[temp] = 0;
				j+=1;
			}
		}	

	}
	
	max = 0;
	i = 6; 
	while(i<1000001)
	{
		a[i] = i/a[i];
		if(a[i]>max)
		{
			max = a[i];
			maxi = i;
		} 
		i+=6;
	}
	printf("%d\n",maxi);

	return 0;
}
