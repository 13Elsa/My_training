#include<stdio.h>
long long int fact(long int n)
{
	if(n==1||n==0)
	{
		return 1;
	}
	else
	{
		return n*fact(n-1);
	}
}
int main()
{
	long int n;
	scanf("%ld",&n);
//	factorial=fact(n);
	printf("%lld",fact(n));
}
