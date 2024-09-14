
f = open("periodictable.txt", "r")
NUM_ELEMS = 111
def ptable_anumtomass(): # Atomic number to atomic mass
    f.seek(0)
    ret = [0] * NUM_ELEMS
    for x in range(1,NUM_ELEMS+1):
        line = f.readline()
        line = line.strip().split(",")
        ret[x-1] = float(line[1])
    return ret

def ptable_asymtoanum(): # Atomic symbol to atomic number
    f.seek(0)
    ret = {}
    for x in range(1,NUM_ELEMS+1):
        line = f.readline()
        line = line.strip().split(",")
        ret[line[0]] = x
    return ret

def ptable_asymtomass():
    f.seek(0)
    ret = {}
    for _ in range(1,NUM_ELEMS+1):
        line = f.readline()
        line = line.strip().split(",")
        ret[line[0]] = float(line[1])
    return ret
