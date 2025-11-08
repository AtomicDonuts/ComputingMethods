#include <math.h>

#ifndef FOURVECTOR
#define FOURVECTOR

class FourVector
{
private:
    double m_E;
    double m_Px;
    double m_Py;
    double m_Pz;
public:
    // Constructors
    FourVector(double E, double Px, double Py, double Pz);
    // Operators
    FourVector operator + (FourVector const &pino);
    // Accessors
    double get_E()  const;
    double get_Px() const;
    double get_Py() const;
    double get_Pz() const;
    void set_E(double f_input);
    void set_Px(double f_input);
    void set_Py(double f_input);
    void set_Pz(double f_input);
    // Functions
    double p3Squared();
    double invariantMass();
    double transferMoment();
};
#endif