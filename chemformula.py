from importptable import ptable_asymtomass, ptable_asymtoanum, ptable_anumtomass, NUM_ELEMS
import re
import numpy as np
mass = ptable_asymtomass()
ANUMTOMASS = np.array(ptable_anumtomass())
ASYMTONUM = ptable_asymtoanum()

def toelem(elem, mult):
    return (elem, int(mult) if len(mult) > 0 else 1)

def parsemolformula(chemicalformula):
    y = [z[0] for z in re.findall("((\d)+|([A-Z][a-z]*\d*)|\)(\d)*|\()", chemicalformula)]
    
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

class element:
    mult = 0
    elem = ""
    def __init__(self, elem, mult):
        self.mult = mult
        self.elem = elem
    
    def tomass(self):
        return mass[self.elem] * self.mult
    
    def compstr(self):
        return self.elem + ("" if (self.mult == 1) else str(self.mult))

    def getelem(self):
        ret = np.zeros((NUM_ELEMS, 1))
        ret[ASYMTONUM[self.elem]-1] += self.mult
        return ret

    def __str__(self):
        ret = self.compstr()
        return ret

class compound(element):
    comp = []
    def __init__(self, mult, comp):
        element.__init__(self, "", mult)
        self.comp = comp

    def addelem(self, elem):
        self.comp.append(elem)

    def compstr(self):
        ret = ""
        for x in self.comp:
            ret = ret + str(x)
        return ret
    
    def tomass(self):
        return float(ANUMTOMASS@(self.getelem())) # lol
    
    def getelem(self):
        ret = np.zeros((NUM_ELEMS, 1))
        for x in self.comp:
            ret += x.getelem()
        return ret * self.mult

    def __str__(self):
        ret = str(self.mult) if (self.mult > 1) else ""
        for x in self.comp:
            if (isinstance(x,compound)):
                ret = ret + "(" + x.compstr() + ")" + ("" if (x.mult == 1) else str(x.mult))
            elif (isinstance(x,element)):
                ret = ret + str(x)
        return ret
