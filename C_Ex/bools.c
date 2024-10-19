#include <stdio.h>
#include <stdbool.h>

int main(void){

    int flags = 65;   // 0011 1111
    int mask = 64;    // 0100 0000 
    bool isValidData;
    isValidData = flags & mask;
    printf(isValidData?"True\n\n":"False\n\n");
    int write_binary = 107;
    for(int i = 0; i < 8;i++){
        printf("%u\n",write_binary>>i);
    }
    return 0;
}