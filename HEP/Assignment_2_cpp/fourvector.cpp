#include "fourvector.h"
#include <iostream>

FourVector::FourVector(double E, double Px, double Py, double Pz)
{
    m_E = E;
    m_Px = Px;
    m_Py = Py;
    m_Pz = Pz;
}
double FourVector::get_E() {  return m_E; }
double FourVector::get_Px() { return m_Px; }
double FourVector::get_Py() { return m_Py; }
double FourVector::get_Pz() { return m_Pz; }
void FourVector::set_E(double f_input) { m_E = f_input; }
void FourVector::set_Px(double f_input) { m_Px = f_input; }
void FourVector::set_Py(double f_input) { m_Py = f_input; }
void FourVector::set_Pz(double f_input) { m_Pz = f_input; }

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