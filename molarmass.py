
from importptable import ptable_asymtomass
mass = ptable_asymtomass()
from chemformula import parsemolformula

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

if __name__ == "__main__":
    formula = input("Enter molecular formulas (seperated by space) -> ")
    formula = formula.split(" ")
    for x in formula:
        comp = parsemolformula(x)
        print(f"{str(comp)} has molar mass of {comp.tomass()} g/mol")

        

