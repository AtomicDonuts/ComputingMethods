#include "fourvector.h"
#include <iostream>

FourVector::FourVector(double E, double Px, double Py, double Pz)
{
    m_E = E;
    m_Px = Px;
    m_Py = Py;
    m_Pz = Pz;
}
double FourVector::get_E()  const {  return m_E; }
double FourVector::get_Px() const { return m_Px; }
double FourVector::get_Py() const { return m_Py; }
double FourVector::get_Pz() const { return m_Pz; }
void FourVector::set_E(double f_input) { m_E = f_input; }
void FourVector::set_Px(double f_input) { m_Px = f_input; }
void FourVector::set_Py(double f_input) { m_Py = f_input; }
void FourVector::set_Pz(double f_input) { m_Pz = f_input; }

FourVector::operator +(FourVector const &pino){
    FourVector _output();
    _output.set_E(m_E + pino.get_E());
    _output.set_Px(m_Px + pino.get_Px());
    _output.set_Py(m_Py + pino.get_Py());
    _output.set_Pz(m_Pz + pino.get_Pz());
}

double FourVector::p3Squared()
{
    return m_Px * m_Px + m_Py * m_Py + m_Pz * m_Pz;
}

double FourVector::invariantMass()
{
    return m_E * m_E - p3Squared();
}

double FourVector::transferMoment()
{
    return sqrt(m_Px * m_Px + m_Py * m_Py);
}