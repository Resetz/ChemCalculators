
from importptable import ptable_asymtomass
mass = ptable_asymtomass()
def toelem(elem, mult):
    return (elem, int(mult) if len(mult) > 0 else 1)

def comptostr(comp):
    ret = ""
    for x in comp:
        ret = ret + x[0] + ("" if (x[1] == 1) else str(x[1]))
    return ret

def comptomass(comp):
    ret = 0
    for x in comp:
        ret += mass[x[0]] * x[1]
    return ret 

def parsemolformula(formula):
    cur = []
    elem = ""
    mult = ""
    while (pos < len(formula) and formula[pos].isalnum()):
        if (len(elem) > 0 and formula[pos].isupper()):
                cur.append(toelem(elem, mult))
                elem = ""
                mult = ""
        if (formula[pos].isalpha()):
            elem = elem + formula[pos]
        if (formula[pos].isdigit()):
            mult = mult + formula[pos]
        pos += 1
    return cur

if __name__ == "__main__":
    formula = input("Enter molecular formulas (seperated by space) -> ")
    formula = formula
    pos = 0
    while (pos < len(formula)):
        while (pos < len(formula) and not formula[pos].isalpha()):
            pos+=1

        cur = []
        elem = ""
        mult = ""
        while (pos < len(formula) and formula[pos].isalnum()):
            if (len(elem) > 0 and formula[pos].isupper()):
                    cur.append(toelem(elem, mult))
                    elem = ""
                    mult = ""
            if (formula[pos].isalpha()):
                elem = elem + formula[pos]
            if (formula[pos].isdigit()):
                mult = mult + formula[pos]
            pos += 1

        cur.append(toelem(elem, mult))

        if (len(cur) > 0):
            print(comptostr(cur), "has a mass of", comptomass(cur), "g/mol")

        

