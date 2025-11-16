#include "fourvector.h"
#include <iostream>

int main()
{
    FourVector Muon(5.2, 3.2, 2.2, 1.2);
    std::cout << "Vector E : " << Muon.get_E() << std::endl;
    std::cout << "Vector Px: " << Muon.get_Px() << std::endl;
    std::cout << "Vector Py: " << Muon.get_Py() << std::endl;
    std::cout << "Vector Pz: " << Muon.get_Pz() << std::endl;
    std::cout << "Massa Invariante: " << Muon.invariantMass() << std::endl;
    std::cout << "Momento Transverso: " << Muon.transferMoment() << std::endl;
    std::cout << "Cambio Coordinate" << std::endl;
    Muon.set_E(3.2);
    Muon.set_Px(1.4);
    Muon.set_Py(7.6);
    Muon.set_Pz(2.0);
    std::cout << "Vector E : " << Muon.get_E() << std::endl;
    std::cout << "Vector Px: " << Muon.get_Px() << std::endl;
    std::cout << "Vector Py: " << Muon.get_Py() << std::endl;
    std::cout << "Vector Pz: " << Muon.get_Pz() << std::endl;
    std::cout << "Massa Invariante: " << Muon.invariantMass() << std::endl;
    std::cout << "Momento Transverso: " << Muon.transferMoment() << std::endl;
    FourVector Electron1(1,2,3,4);
    FourVector Electron2(4,3,2,1);
    std::cout << "Massa Invariante di Electron1 + Electron 2 " << (Electron1 + Electron2).invariantMass() << std::endl;
    std::cout << "Momento Trasverso di Electron1 + Electron 2 " << (Electron1 + Electron2).transferMoment() << std::endl;
    return 0;
    }
