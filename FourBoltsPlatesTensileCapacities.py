# This program for calculating capacity of C1
# Plate Thickness
tp=6.0
# Plate ultimate stress
fu=453.0
# Plate bending capacity
mp=0.25*fu*tp*tp
# Plate edge distance
e=35.0
# Plate center distance
m=20.0
# Tube width
B=80.0
# distances
l8=m+2*e
l9=1.1132*m+1.6906*e
# Tensile capacity
Pk8=4*mp*l8/m*2
Pk9=4*mp*l9/m*2
from sympy import *
alpha=Symbol('alpha')
l10=1/(2*(sin(alpha)+cos(alpha)))*(B/2*cos(alpha)+m*(1/cos(alpha)+sin(alpha))+e*(2/cos(alpha)+1/(sin(alpha))+sin(alpha)))
print('l10:')
maxnum = 100000000
for i in [j*3.1415926/400 for j in range(1, 200)]:
  nump=l10.evalf(subs={alpha:i})
  if nump < maxnum:
    maxnum = nump
    angle = i
print('angle = %f' % (angle/3.1415926*180))
l10=l10.evalf(subs={alpha:angle})
Pk10=4*mp*l10/m*2
print("For thickness of 6mm", Pk8,Pk9,Pk10)
Pk8 = Pk8/36*64
Pk9 = Pk9/36*64
Pk10 = Pk10/36*64
print("For thickness of 8mm", Pk8,Pk9,Pk10)