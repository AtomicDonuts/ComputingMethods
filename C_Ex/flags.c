#include <stdio.h>
#include <stdbool.h>
#define BYTE 8

void int2bit(int write_binary, int numb_of_byte)
/* Write on screen the bit rappresentation of a intger number
*/
{
    for (int i = numb_of_byte * BYTE; i > 0; i--)
    {
        if (!(i % 4))
            printf(" ");
        printf("%u", (write_binary >> (i - 1)) & 1);
    }
}

int main(void)
{
    int flags = 63; // 0011 1111
    int mask = 64;  // 0100 0000
    bool isValidData;
    isValidData = flags & mask;
    printf(isValidData ? "True\n\n" : "False\n\n");
    int numb_of_byte = 4;
    int max = __INT32_MAX__;
    printf("%d", max);
    for (int bin = 1; bin < max;bin = bin * 2)
    {
        printf("\n%d\n", bin);
        int2bit(bin, numb_of_byte);
        if (bin == 0) break;
    }
    return 0;
}