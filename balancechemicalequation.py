import re
from chemformula import compound,element
#from molarmass import parsemolformula
s = input("Enter a chemical equation -> ").strip()

def parsemolformula(chemicalformula):
    y = [z[0] for z in re.findall("((\d)+|([A-Z][a-z]*\d*)|\)(\d)+|\()", chemicalformula)]
    
    
    cur = 0
    st = [] # stack to emulate recursion (need back referencing)
    t = 1
    if (y[0].isnumeric()):
        t = int(y[cur])
        cur = 1
    st.append(compound(t, []))
    
    while (cur < len(y)):
        token = y[cur]
        if (token == "("):
            c = compound(1, [])
            st[-1].addelem(c)
            st.append(c)
        elif (token[0] == ")"):
            if (len(token) > 1):
                st[-1].mult = int(token[1:])
            st.pop()
        else:
            elem = ""
            mult = ""
            if (len(token) >= 2 and token[:2].isalpha()):
                elem = token[:2]
                mult = token[2:]
            else:
                elem = token[:1]
                mult = token[1:]
            
            st[-1].addelem(element(elem, int(mult) if len(mult) > 0 else 1))
        cur+=1
    return st[-1]



for x in re.findall("((\d)*([a-zA-Z0-9\(\)])+|->|\+)", s):
    chemicalformula = x[0]
    print("found", chemicalformula)

    #regex again yayy
    res = parsemolformula(chemicalformula)
    print(res)
    print("Molar mass is:", res.tomass())
    #y = re.findall("((\d)+|([A-Z][a-z]*\d*)|\)(\d)+|\()", chemicalformula)
    #for z in y:
    #    print("token (element/coefficient): ", z[0])
        

