#include<stdio.h>
struct employee
{
	long int salary,hra,da,ts;
	char name[20];
	void read() 
	{
		printf("\n enter employee name :");
		scanf("%s",&name);
		printf("\n enter salary :");
		scanf("%ld",&salary);
		hra=salary*10/100;
		printf("\n HRA : %ld",hra);
		da=salary*5/100;
		printf("\n DA : %ld",da);
		ts=salary+hra+da;
		printf("\n total salary :%ld",ts);
	}
	void line()
	{
		printf("\n-------------------------------------------------------------------------");
	}
	void title()
	{
		line();
		printf("\n salary\tname\t hra\tda\t total salary");
		line();
	}
	void show()
	{
		printf("\n%ld\t%s\t%ld\t%ld\t%ld",salary,name,hra,da,ts);
		line();
	}
};   // end of struct
int main()
{
	
	employee s[500];
	int n,i;
	printf("\n how many ");
	scanf("%ld",&n);
	for(i=0;i<n;i++)
	{
		s[i].read();
	}
	s[0].title();
	for(i=0;i<n;i++)
	{
		s[i].show();
	}
}

