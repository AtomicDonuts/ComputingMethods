#include "fourvector.h"
#include <iostream>

//FourVectors Definitions

FourVector::FourVector(double E, double Px, double Py, double Pz)
{
    set_E(E);
    set_Px(Px);
    set_Py(Py);
    set_Pz(Pz);
}
double FourVector::get_E() const { return m_E; }
double FourVector::get_Px() const { return m_Px; }
double FourVector::get_Py() const { return m_Py; }
double FourVector::get_Pz() const { return m_Pz; }
void FourVector::set_E(double f_input) { m_E = f_input; }
void FourVector::set_Px(double f_input) { m_Px = f_input; }
void FourVector::set_Py(double f_input) { m_Py = f_input; }
void FourVector::set_Pz(double f_input) { m_Pz = f_input; }

FourVector FourVector::operator+(const FourVector &pino) const
{
    FourVector _output(m_E + pino.get_E(), m_Px + pino.get_Px(), m_Py + pino.get_Py(), m_Pz + pino.get_Pz());
    return _output;
}

double FourVector::p3Squared() {return m_Px * m_Px + m_Py * m_Py + m_Pz * m_Pz;}
double FourVector::invariantMass(){return m_E * m_E - p3Squared();}
double FourVector::transferMoment(){return sqrt(m_Px * m_Px + m_Py * m_Py);}

//Partcle Definitions

Particle::Particle(int id, double E, double Px, double Py, double Pz, double tau)
{
    set_E(E);
    set_Px(Px);
    set_Py(Py);
    set_Pz(Pz);
    set_id(id);
    set_tau(tau);
}
/* No sbagliato, peccato mortale
Particle::Particle(FourVector &vec,int id,double tau){
    FourVector(vec);
    set_id(id);
    set_tau(tau);
}
*/
// Modo Corretto: 
// Inizializzare tutto con i due punti
Particle::Particle(const FourVector &vec, int id, double tau) : 
    FourVector(vec),
    m_pid(id),
    m_tau(tau)
    {}

int Particle::pid() const { return m_pid; }
double Particle::tau() const { return m_tau; }
void Particle::set_id(int f_input) { m_pid = f_input; }
void Particle::set_tau(double f_input) { m_tau = f_input; }

// TwoBodiesDecayedParticle

TwoBodiesDecayedParticle::TwoBodiesDecayedParticle(const Particle &p1, const Particle &p2, int pid = 0, double tau = 0.) :
 Particle(p1 + p2, pid, tau),
 m_p1(p1),
 m_p2(p2)
 {}

 void TwoBodiesDecayedParticle::infos()
 {
     std::cout << "Combined pt and mass" << std::endl;
     std::cout << transferMoment() << " " << invariantMass() << std::endl;
     std::cout << "Particle 1" << std::endl;
     std::cout << m_p1.transferMoment() << " " << m_p1.invariantMass() << " " << m_p1.pid() << std::endl;
     std::cout << "Particle 2" << std::endl;
     std::cout << m_p2.transferMoment() << " " << m_p2.invariantMass() << " " << m_p2.pid() << std::endl;
 }
