#include <string>
#include <vector>
#include <map>
#include <iostream>
//using namespace std;

class Entry
{
private:
    /* data */
    std::string m_name;
    std::string m_number;
    std::string m_mail;

public:
    Entry() {}
    Entry(std::string s_name,std::string s_phonenumber) : set_name(s_name),set_number(s_phonenumber) {}

    void set_name(std::string s_name) {m_name = s_name;}
    void set_number(std::string s_pn) {m_number = s_pn;}
    void set_mail(std::string s_mail) {m_mail = s_mail;}

    std::string name() const {return m_name;}
    std::string number() const {return m_number;}
    std::string mail() const {return m_mail;}

    void print(){
    std::cout << name() << std::endl;
    std::cout << number() << std::endl;
    std::cout << mail() << std::endl;
    }

}; 
/*
class phonebook
{
public:
    phonebook();
    std::vector<typename Entry> m_book;


};
*/