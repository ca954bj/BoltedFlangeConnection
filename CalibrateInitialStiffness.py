from sympy import *
import matplotlib as mpl
import matplotlib.pyplot as plt

x = Symbol('x')

def findfunctions(x1, y1, k1, x2, y2, k2):
	minb = min(x1, x2)
	maxb = max(x1, x2)
	a1, b1, c1, d1, e1, x = symbols('a1, b1, c1, d1, e1, x')
	fun1 = a1*ln(b1*x + c1) + d1
	dfun1 = diff(fun1, x)
	ddfun1 = diff(dfun1, x)
	eq1 = fun1.subs({x:x1})-y1
	eq2 = dfun1.subs({x:x1})-k1
	eq3 = fun1.subs({x:x2}) - y2
	eq4 = dfun1.subs({x:x2}) - k2
	sol = list(linsolve([eq1, eq2, eq3, eq4], (a1, b1, c1, d1)))
	a1s = sol[0][0]
	b1s = sol[0][1]
	c1s = sol[0][2]
	d1s = sol[0][3]
	#while a1s>0 or a2s>0:
	return lambdify(x, fun1.subs({a1:a10, b1:b1s, c1:c1s, d1:d1s, e1:e1s}))
		
		
fun = findfunctions(1.0, 100.0, 100.0, 2.0, 150.0, 1.2)
xlist = [0.01*x for x in range(0, 500)]
ylist = []
for obj in xlist:
	if obj <= 1:
		ylist.append(100*obj)
	elif obj <= 2:
		ylist.append(fun(obj))
	else:
		ylist.append(1.2*(obj - 2.0)+150.0)

plt.plot(xlist, ylist, color='black', label='Experiment', linestyle='-')
plt.show()
