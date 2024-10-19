#include <stdio.h>

void upper(char * str){
    do{
        if(*str<=122 && *str>= 97){
            *str -= 32;
        }
        printf("%c",*str);

    }
    while(*str++);
}

int main(void){
    char string[30]= "ABCdef?£[_GhI";
    upper(string);
    return 0;
}