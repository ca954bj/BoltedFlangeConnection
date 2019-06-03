# This program for calculating capacity of C1
# Plate Thickness
tp=8
# Plate ultimate stress
fu=453
# Plate bending capacity
mp=0.25*fu*tp*tp
# Distances
b=25.0
a=30.0
s2=54.0
s1=(80.0-54.0)/2
U = 8*(((b/a)*(b/a+1)*((s1/a)**2-2*(s1/a)+8)**0.5-s1/a*(b/a-0.5)+b/a+s2/a+1))
Pp=U*mp
print(Pp)