#ifndef FOURVECTOR_H
#define FOURVECTOR_H
#include <math.h>

template <class T>
class FourVector
{
public:
    FourVector() {}
    FourVector(T px, T py, T pz, T e) : m_px(px), m_py(py), m_pz(pz), m_e(e) {}
    // getters
    T px() const { return m_px; }
    T py() const { return m_py; }
    T pz() const { return m_pz; }
    T e() const { return m_e; }
    T pt() const { return sqrt(m_px * m_px + m_py * m_py); }
    T m() const { return sqrt(m_e * m_e - (m_px * m_px + m_py * m_py + m_pz * m_pz)); }

    template <class OT>
        .FourVector operator+(const OT &other) const
    {
        FourVector ret(m_px + other.m_px, m_py + other.m_py, m_pz + other.m_pz, m_e + other.m_e);
        return ret;
    }
    FourVector operator*(OT scalar)
    {
        FourVector ret(m_px*scalar,m_py * scalar, m_pz * scalar,m_e * scalar);
        return ret;
    }
    // setters
    void setPx(T px) { m_px = px; }
    void setPy(T py) { m_py = py; }
    void setPz(T pz) { m_pz = pz; }
    void setE(T e) { m_e = e; }

private:
    T m_px;
    T m_py;
    T m_pz;
    T m_e;
};
#endif