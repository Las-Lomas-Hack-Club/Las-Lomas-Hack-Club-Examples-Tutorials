#include <stdio.h>
//Currency translator in C

//Made this in Sept 2018 but never posted it...
int main(void)
{
    //NEVER do this, if you name variables as badly as I did in this example I will be very dissapointed
    char c;
    printf("Hello, are here to tranlate currency?  Well you are now.  Press enter : ");
    //input equiv in C
    scanf("%c",&);
    while (c != "y")
    {
     float a;
     printf("Enter USD to get value in yuan:$");
     scanf("%f", &a);
     {
         //These symbols are NOT all unicode, so this may or may not cause errors, :P
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
/*
This is probably the worst code I've written, but C is pretty cool.  It's very versatile, and you can do high and
low level programming with it (even though high level stuff is a total pain).
Well, have fun, and keep on coding kids... Wow, I sound weird rn byeee!
*/
