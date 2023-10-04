//find the lonely integers in the given array
#include<stdio.h>
int main()
{
	int n,res=0,i;                                       
	scanf("%d",&n);
	int a[n];
	for(i=1;i<=n;i++)
	{
		scanf("%d",&a[i]);
	}
	for(i=1;i<=n;i++)
	{
		res=res^a[i];
	}
	printf("%d",res);
}
