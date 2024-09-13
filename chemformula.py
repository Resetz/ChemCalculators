from importptable import ptable_asymtomass
mass = ptable_asymtomass()

def toelem(elem, mult):
    return (elem, int(mult) if len(mult) > 0 else 1)

def parsemolformula(formula):
    cur = []
    m = 0
    elem = ""
    mult = ""
    while (pos < len(formula) and formula[pos].isalnum()):
        if (formula[pos].isupper()):
            if (len(elem) != 0):
                cur.append(toelem(elem, mult))
            else:
                m = int(mult)

            elem = ""
            mult = ""

        if (formula[pos].isalpha()):
            elem = elem + formula[pos]
        if (formula[pos].isdigit()):
            mult = mult + formula[pos]
        pos += 1
    return compound(m, cur)

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
        ret = 0
        for x in self.comp:
            ret += x.tomass()
        return ret * self.mult

    def __str__(self):
        ret = str(self.mult) if (self.mult > 1) else ""
        for x in self.comp:
            if (isinstance(x,compound)):
                ret = ret + "(" + x.compstr() + ")" + ("" if (x.mult == 1) else str(x.mult))
            elif (isinstance(x,element)):
                ret = ret + str(x)
        return ret
