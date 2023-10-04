//Determine a number is power of 2 or not
#include<stdio.h>
int main()
{
	int count=0,n;
	scanf("%d",&n);
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	if(count==1)
	{
		printf("True");
	}
	else
	{
		printf("False");
	}
}
