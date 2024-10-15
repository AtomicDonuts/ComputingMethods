#include <stdio.h>

int main(void){

    int pino = 63;   // 0011 1111
    int mask = 64;   // 0100 0000 
    int c;
    c = pino & mask;
    printf("%d",c);
    return 0;
}