#include<stdio.h>
int main()
{
	int n;
	int count=0;
	scanf("%d",&n);
	while(n)
	{
		count++;
		n=n&(n-1);
	}
	printf("Count set bits = %d",count);
}
