import re
from molarmass import parsemolformula
s = input("Enter a chemical equation -> ").strip()

for x in re.findall("((\d)*([a-zA-Z0-9])+|->|\+)", s):
    chemicalformula = x[0]
    print("found", chemicalformula)
    #regex again yayy
    y = re.findall("((\d)+|([A-Z][a-z]*\d*))", chemicalformula)
    for z in y:
        print("token (element/coefficient): ", z[0])
        

