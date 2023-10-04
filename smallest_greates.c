/*Smallest number greater than 'n' with exactly 1 bit difference in binary form*/
#include<stdio.h>
int main()
{
	int a;
	scanf("%d",&a);
	printf("%d",a | a+1);
}
