#include <stdio.h>

int main(void){
    float a = 1.f + 1e-10f;
    float b = 1.f - 1e-10f;
    float c = 1.f/(a-b);

    printf("%f\n",c);

    double a1 = 1. + 1e-10;
    double b1 = 1. - 1e-10;
    double c1 = 1./(a1-b1);

    printf("%f\n",c1);

    for(double epsilon = 1.; epsilon > 1.e-20; epsilon/=10){
        float a = 1.;
        float b = 1.;
        double c = 1.;
        double d = 1.;
        printf("a: %f \t b: %f \t c: %f \t: %f",a,b,c,d);

    }
    return 0;
}