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
    Entry(std::string s_name,std::string s_phonenumber,std::string s_mail) : m_name(s_name),m_number(s_phonenumber),m_mail(s_mail) {}

    void set_name(std::string s_name) {m_name = s_name;}
    void set_number(std::string s_pn) {m_number = s_pn;}
    void set_mail(std::string s_mail) {m_mail = s_mail;}

    std::string name() const {return m_name;}
    std::string number() const {return m_number;}
    std::string mail() const {return m_mail;}

    void print(){
    std::cout <<"------"<<name()<<"------"<<std::endl;
    std::cout << number() << std::endl;
    std::cout << mail() << std::endl;
    std::cout << "---------------------"<<std::endl; 
    }

}; 

class Phonebook
{
public:
    Phonebook() {}
    std::vector<class Entry> m_book;
    void insert(class Entry & e){m_book.push_back(e);}
    
    void print() {
        for(auto x : m_book) {x.print();}
    }
};
