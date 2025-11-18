import ROOT

cpp_code = """
int stringcheck(std::string stringa){
    return stringa.size() ;
}
"""

ROOT.gInterpreter.ProcessLine(cpp_code)

ROOT.stringcheck("123456789")
