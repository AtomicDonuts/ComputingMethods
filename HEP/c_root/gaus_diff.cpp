// g++ gaus_diff.cpp -o gaus_diff.exe $(root-config --cflags --libs)
#include <vector>
#include <iostream>
#include <math.h>
#include "TMath.h"

double hand_gaus(double x)
{
    return exp(-x * x * 0.5);
}

int main()
{
    std::vector<float> values = {0., 1., 10., 20.};
    for (auto i : values)
    {
        std::cout << i << " " << abs(hand_gaus(i) - TMath::Gaus(i)) << std::endl;
    }
}
