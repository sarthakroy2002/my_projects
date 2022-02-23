/*
*
* Write a program in C to find out
* (A,H,G)Mean, Median, Mode
* 
* author: Sarthak Roy <sarthakroy2002@gmail.com>
*
*/ 
#include<stdio.h>
int main()
{
	int n,a[100],tmp;
	printf("\n Enter the value of n:");
	scanf("%d", n);
	printf("\n Enter the values of the elements:");
	for(int i=0; i<n;n++)
	{
		scanf("%d", a[i]);
	}

    for(int l=1;l<=n-1;l++) // For Sorting
    {
        for(int b=1;b<=n-l;b++)
        {
            if(a[b]<=a[b+1])
            {
                tmp=a[b];
                a[b]=a[b+1];
                a[b+1]=tmp;
            }
        }
    }
	
	int am=0, k=0; // For Arithmetric Mean
	for(int j=0;j<n;j++)
	{
	    k=k+a[i];
	}
	am=k/n;
	printf("\n The Arithmetric Mean of the elements: %d", am);
	
	int y=0, hm=0; // For Harmonic Mean
	for(int o=0; o<n; o++)
	{
	    o=o+1/a[i];
	}
	hm=n/o;
	printf("\n The Harmonic Mean of the elements: %d", hm);
	
	int median=0; // For Median
	if (n%2==0)
	{
	    median=(a[n/2]+a[n/2+1]/2);
	}
	else
	{
	    median=a[n/2-1];
	}
	printf("\n The Median of the elements: %d", median);
	return 0;
}
