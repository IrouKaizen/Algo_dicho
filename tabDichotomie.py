from cmath import cos
from math import *

def f(l) :
    f = l - 1 + (1/4)*(cos(l))
    return f


print()

a0 = 0
b0 = pi
l0 = pi/2
cpt = 0

print("------------------------------------------------------------------")
print("\tk\t|\t[ak, bk]\t\t|\tlk\t")
print("------------------------------------------------------------------")
while cpt <= 20 :
    print(f"\n\t{cpt}\t|\t[{a0:.5f}, {b0:.5f}]\t|\t{l0:.5f}\t\n")
    print("------------------------------------------------------------------")
    if f(a0)*f(l0) < 0 :
        b0 = l0
    else :
        a0 = l0
    l0 = (a0 + b0)/2 
    cpt += 1
    
    
    
print("La solution est", f(l0))
    
    

# #  k  | [ak, bk] | lk |
# #  --------------------
# #  0  | [0,pi]   | pi/2
# #  --------------------
# #  ...| .....    | ...  