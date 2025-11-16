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
    FourVector(double E, double Px, double Py, double Pz);
    // Operators
    FourVector operator+(FourVector const &pino) const;
    // Accessors
    double get_E() const;
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

class Particle : public FourVector
{
private:
    int m_pid;
    double m_tau;

public:
    Particle(int id, double E, double Px, double Py, double Pz, double tau);
    Particle(const FourVector &particle1,int id,double tau);
    int pid() const;
    double tau() const;
    void set_id(int f_input);
    void set_tau(double f_input);
};

class TwoBodiesDecayedParticle : public Particle
{
    private:
    Particle m_p1;
    Particle m_p2;
    
    public:
        TwoBodiesDecayedParticle(const Particle &p1, const Particle &p2, int pid = 0, double tau = 0.);
        void infos();
};
#endif