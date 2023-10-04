#include<stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	if(n&1==1)   //if n=14 i.e,binary equivalent of 14 is 1110 perform AND with 0001 then we get 0000 which is 0. So, answer is EVEN
	{
		printf("ODD");
	}
	else
	{
		printf("EVEN");
	}
}
