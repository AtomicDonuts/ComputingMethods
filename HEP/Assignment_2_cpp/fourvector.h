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
    FourVector();
    FourVector(double E, double Px, double Py, double Pz){
        double m_E  =  E;
        double m_Px = Px;
        double m_Py = Py;
        double m_Pz = Pz;
    }
    // Accessors
    double get_E (){return m_E ;}
    double get_Px(){return m_Px;}
    double get_Py(){return m_Py;}
    double get_Pz(){return m_Pz;}
    void set_E (double f_input){m_E =  f_input; }
    void set_Px(double f_input){m_Px = f_input; }
    void set_Py(double f_input){m_Py = f_input; }
    void set_Pz(double f_input){m_Pz = f_input; }
    
    // Functions
    double norm2(){
        return m_Px * m_Px + m_Py * m_Py + m_Pz * m_Pz;
    }

    double invariantMass(){
        return m_E*m_E - norm2();
    } 

    double transferMoment(){
        return sqrt(m_Px * m_Px + m_Py * m_Py);
    }

};
#endif