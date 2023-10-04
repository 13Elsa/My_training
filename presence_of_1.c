/* Check the ith bit is set or not (set means ith bit is 1 or not)
1011 ----11
0100 ----1<<2
0 ----0

1011 ---- 11
0010 ---- 1<<1
2 ---- 2

1111 ---- 15
1000 ---- 1<<3
8 ---- 8
*/
#include<stdio.h>
int main()
{
	int n,i;
	scanf("%d",&n);
	scanf("%d",&i);
	if(n&(1<<(i-1)))
	{
		printf("Yes");
	}
	else
	{
		printf("No");
	}
}
