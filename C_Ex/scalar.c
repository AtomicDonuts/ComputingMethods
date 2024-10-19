#include <stdio.h>

void s_mul(float * array,float scalar,int dim){
    
    for(int i = 0;i < dim;i++){
        array[i] = scalar * array[i];
    }
}

int main(void){
    float pino[4] = {1,2,3,4};
    int a = 4;
    s_mul(pino,a,4);
    for(int i=0;i<4;i++){
        printf("%f ",pino[i]);
    }

    return 0;
}