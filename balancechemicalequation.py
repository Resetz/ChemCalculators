import re
import numpy as np
from scipy.linalg import null_space
from chemformula import parsemolformula

#from molarmass import parsemolformula
s = input("Enter a chemical equation -> ").strip()

A = None

left = []
right = []

foundarrow = False

for x in re.findall("((\d)*([a-zA-Z0-9\(\)])+|->|\+)", s):
    token = x[0]
    #regex again yayy
    if (token == "->"):
        foundarrow = True
    elif (token == "+"):
        continue
    else:
        comp = parsemolformula(token)
        compcol = comp.getelem() * (-1 if foundarrow else 1)

        if (len(left) == 0):
            A = compcol
        else:
            A = np.concat((A, compcol), axis = 1)

        if (foundarrow):
            right.append(comp)
        else:
            left.append(comp)
    #y = re.findall("((\d)+|([A-Z][a-z]*\d*)|\)(\d)+|\()", chemicalformula)
    #for z in y:
    #    print("token (element/coefficient): ", z[0])

sol = np.absolute(null_space(A))
sol = sol / sol.min()

while True:
    print("Current solution = ")
    print(sol)
    n = float(input("Scale elements by constant? (-1 to exit) -> "))
    if (n == -1):
        break

    sol = sol * n

print("Solution")
print()
for x in range(len(left)):
    comp = left[x]
    comp.mult = int(float(sol[x][0])+0.5)
    print(str(comp) + (" + " if x != len(left)-1 else " "), end = "")

print("-> ", end = "")
for x in range(len(right)):
    comp = right[x]
    comp.mult = int(float(sol[x+len(left)][0])+0.5)
    print(str(comp) + (" + " if x != len(right)-1 else "\n"), end = "")

print()