#include "phonebook.cpp"

int main(){
    Entry a;
    a.set_name("Pascal");
    a.set_number("3822094356");
    a.set_mail("Pascal98@hotmai.it");
    a.print();
    std::string s1 = "Poscal";
    std::string s2 = "382282";
    std::string s3 = "dhjhd@djdhdh";
    Entry b(s1,s2,s3);
    b.print();

}