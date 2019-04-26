#include <stdio.h>

int main(void)
{
    char c;
    printf("Hello, are here to tranlate currency?  Well you are now.  Press enter : ");
    scanf("%c",&c);
    while (c != "y")
    {
     float a;
     printf("Enter USD to get value in yuan:$");
     scanf("%f", &a);
     {
         printf("$%f US Dollars = %f Chinese Yuan\n",a, (a) * 6.83);
     }
     float b;
     printf("Enter USD to get value in Japanese Yen:$");
     scanf("%f", &b);
     {
         printf("$%f US Dollars = %f Yen\n",b,(b)*111.61);
     }
    char o;
    printf("Do you want to end the program? y/n \n");
    scanf("%c",&o);
    {
     if(o == "n")
     break;
    } 
}
    return 0;
}

