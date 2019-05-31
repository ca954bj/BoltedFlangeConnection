# Determine the ultimate tensile capacity of bolted flanged connections

from sympy import *

class Operation:
	def __init__(self):
		pass
	class DotProduct():
		def __init__(self, a, b):
			self.value = simplify(a[0]*b[0] + a[1]*b[1] + a[2]*b[2])
		def value(self):
			return self.value
	class CrossProduct():
		def __init__(self, a, b):
			self.value = [simplify(a[1]*b[2] - a[2]*b[1]), simplify(a[2]*b[0] - a[0]*b[2]), simplify(a[0]*b[1] - a[1]*b[0])]
		def value(self):
			return self.value
	class Length3D():
		def __init__(self, a):
			self.value = sqrt(a[0]**2 + a[1]**2 + a[2]**2)
		def value(self):
			return self.value
	class Length2D():
		def __init__(self, a):
			self.value = sqrt(a[0]**2 + a[1]**2)
		def value(self):
			return self.value
			
class Node:
	Counter = 0
	instances = []
	def __init__(self, x, y, z):
		Node.Counter += 1
		Node.instances.append(self)
		self.x = x
		self.y = y
		self.z = z
	def x(self):
		return self.x
	def y(self):
		return self.y
	def z(self):
		return self.z
		
class Line:
	Counter = 0
	instances = []
	def __init__(self, node1, node2):
		Line.Counter += 1
		Line.instances.append(self)
		self.node1 = node1
		self.node2 = node2
		self.direction = [node2.x - node1.x, node2.y - node1.y, node2.z - node1.z]
		print('Direction', self.direction)
	def node1(self):
		return self.node1
	def node2(self):
		return self.node2
	def direction(self):
		return self.direction

class Plane:
	Counter = 0
	instances = []
	def __init__(self, lineset):
		Plane.Counter += 1
		Plane.instances.append(self)
		self.lineset = lineset
		linenum = len(lineset)
		self.NormalVector = Operation.CrossProduct(lineset[0].direction, lineset[1].direction).value
		if self.NormalVector[0] == 0 and self.NormalVector[1] == 0 and self.NormalVector[2] == 0:
			self.NormalVector = Operation.CrossProduct(lineset[0].direction, lineset[2].direction).value
		print("NormalVector", self.NormalVector)
	
	def lineset(self):
		return self.lineset
	def NormalVector(self):
		return self.NormalVector
		
class YieldLines:
	def __init__(self, lineset, mp, h):
		linenum = len(lineset)
		angleset = []
		MomentSum = 0
		for i, obj in enumerate(lineset):
			planeset = []
			for obj2 in Plane.instances:
				if obj in obj2.lineset:
					planeset.append(obj2)
			if len(planeset) > 2 or len(planeset) == 0:
				print("The lines are not right! Error %d" % (len(planeset)))
			elif len(planeset) == 2:
				v1 = planeset[0].NormalVector
				v2 = planeset[1].NormalVector
				temp1 = Operation.CrossProduct(v1, v2).value
				temp2 = Operation.Length3D(temp1).value
				temp3 = Operation.DotProduct(v1, v2).value
				angle = temp2/temp3
				dangle = diff(angle, h)
				angleset.append(dangle)
				linelength = Operation.Length2D(obj.direction).value
				Moment = dangle*linelength*mp
				if Moment.evalf(subs={h:2}) < 0:
					Moment = -Moment
				print('Moment', Moment)
				MomentSum += Moment
			elif len(planeset) == 1:
				v1 = planeset[0].NormalVector
				v2 = [0, 0, 1]
				temp1 = Operation.CrossProduct(v1, v2).value
				temp2 = Operation.Length3D(temp1).value
				temp3 = Operation.DotProduct(v1, v2).value
				angle = temp2/temp3
				dangle = diff(angle, h)
				angleset.append(dangle)
				linelength = Operation.Length2D(obj.direction).value
				Moment = dangle*linelength*mp
				if Moment.evalf(subs={h:2}) < 0:
					Moment = -Moment
				print('Moment', Moment)
				MomentSum += Moment
		self.MomentSum = MomentSum
	def MomentSum(self):
		return self.MomentSum
		
h = Symbol('h')

# For check
'''A = Node(61.0, 49.0, h)
B = Node(28.25, 16.33, h)
C = Node(28.25, 0, h)
D = Node(68.0, 25.0, 0)
E = Node(68.0, 0, 0)
F = Node(95.0, 0, 0)
G = Node(95.0, 25.0, 0)
H = Node(95.0, 49.0, h)

print('BC')
BC = Line(B, C)
print('BD')
BD = Line(B, D)
print('DE')
DE = Line(D, E)
print('AB')
AB = Line(A, B)
print('AD')
AD = Line(A, D)
print('EF')
EF = Line(E, F)
print('DG')
DG = Line(D, G)
print('AH')
AH = Line(A, H)

print('ABD')
ABD = Plane([AB, BD, AD])
print('BCDE')
BCDE = Plane([BC, BD, DE])
print('ADGH')
ADGH = Plane([AH, AD, DG])
print('DEFG')
DEFG = Plane([DE, DG])

Moment = 8*YieldLines([BC, BD, DE, AB, AD, AH, DG], 2996.1, h).MomentSum
Moment = Moment.evalf(subs={h:4.0})
print("For test, the tensile capacity is %f" % (Moment/1000))'''

# Problem C1
'''A = Node(0, 0, 0)
B = Node(35.0, 0, 0)
C = Node(35.0, 35.0, 0)
D = Node(0, 35.0, 0)
E = Node(55.0, 55.0, h)
F = Node(55.0, 95.0, h)
G = Node(0, 95.0, 0)
H = Node(95.0, 55.0, h)
I = Node(55.0, 0, 0)

BC = Line(B, C)
CD = Line(C, D)
CE = Line(C, E)
CF = Line(C, F)
CH = Line(C, H)
BH = Line(B, H)
DF = Line(D, F)
EF = Line(E, F)
EH = Line(E, H)
FG = Line(F, G)
BI = Line(B, I)

CEF = Plane([CE, EF, CF])
CDF = Plane([CD, DF, CF])
CEH = Plane([CE, EH, CH])
BCH = Plane([BC, CH, BH])
DFG = Plane([DF, FG])
BHI = Plane([BH, BI])

Moment = 4*YieldLines([CD, BC, CE, CF, CH, DF, BH, EF, EH], 2996.1, h).MomentSum
Moment = Moment.evalf(subs={h:4.0})
print("For C1, the tensile capacity is %f" % (Moment/1000))'''

# Problem C2 103.9kN
'''A = Node(0, 35.0, 0)
B = Node(35.0, 0, 0)
C = Node(35.0, 35.0, 0)
E = Node(17.5, 92.5, h)
F = Node(92.5, 17.5, h)
G = Node(0, 92.5, h)
H = Node(92.5, 0, h)
O = Node(0, 0, 0)

AC = Line(A, C)
BC = Line(B, C)
CE = Line(C, E)
CF = Line(C, F)
EF = Line(E, F)
EG = Line(E, G)
FH = Line(F, H)

OABC = Plane([AC, BC])
ACEG = Plane([AC, CE, EG])
CEF = Plane([CE, EF, CF])
BCFH = Plane([BC, CF, FH])

Moment = 4*YieldLines([AC, BC, CE, CF, EG, EF, FH], 2996.1, h).MomentSum
print(Moment)

Moment = Moment.evalf(subs={h:4.0})
print("For C2, the tensile capacity is %f" % (Moment/1000))'''

# Problem C3 Case1 141.3kN
A = Node(0, 0, 0)
D = Node(35.0, 35.0, 0)
E = Node(0, 35.0, 0)
B = Node(35.0, 0, 0)
F = Node(0, 55.0, h)
G = Node(55.0, 55.0, h)
C = Node(95.0, 55.0, h)

BD = Line(B, D)
DE = Line(D, E)
DG = Line(D, G)
FG = Line(F, G)
CG = Line(C, G)
CD = Line(C, D)
BC = Line(B, C)

ABDE = Plane([BD, DE])
BCD = Plane([BC, CD, BD])
CDG = Plane([CD, DG, CG])
EDFG = Plane([DE, DG, FG])

Moment = 4*YieldLines([DE, BD, DG, FG, CD, CG, BC], 2996.1, h).MomentSum
print(Moment)
Moment = Moment.evalf(subs={h:4.0})
print("For C3, the tensile capacity is %f" % (Moment/1000))



# Problem C3 Case2 163.6kN

'''A = Node(0, 0, 0)
D = Node(35.0, 35.0, 0)
E = Node(0, 35.0, 0)
B = Node(35.0, 0, 0)
F = Node(0, 55.0, h)
G = Node(55.0, 55.0, h)
C = Node(95.0, 55.0, h)

BD = Line(B, D)
DE = Line(D, E)
DG = Line(D, G)
FG = Line(F, G)
CG = Line(C, G)
BG = Line(B, G)
BC = Line(B, C)

ABDE = Plane([BD, DE])
BCG = Plane([BC, CG, BG])
BDG = Plane([BD, DG, BG])
EDFG = Plane([DE, DG, FG])

Moment = 4*YieldLines([DE, BD, DG, FG, BG, CG, BC], 2996.1, h).MomentSum
print(Moment)
Moment = Moment.evalf(subs={h:4.0})
print("For C3, the tensile capacity is %f" % (Moment/1000))'''

# Problem C5 242.9
'''A = Node(0, 0, 0)
B = Node(68.0, 0, 0)
C = Node(92.5, 0, h)
D = Node(0, 68.0, 0)
E = Node(0, 92.5, h)
F = Node(68.0, 25.0, 0)
G = Node(25.0, 68.0, 0)
H = Node(92.5, 110-92.5, h)
I = Node(110-92.5, 92.5, h)

BF = Line(B, F)
FG = Line(F, G)
DG = Line(D, G)
CH = Line(C, H)
EI = Line(E, I)
FH = Line(F, H)
GI = Line(G, I)
HI = Line(H, I)

BCFH = Plane([CH, FH, BF])
FGHI = Plane([FG, FH, HI, GI])
DEGI = Plane([DG, GI, EI])

Moment = 4*YieldLines([BF, FH, CH, FG, HI, GI, DG, EI], 2996.1, h).MomentSum
Moment = Moment.evalf(subs={h:4.0})
print("For C5, the tensile capacity is %f" % (Moment/1000))'''

# Problem C6 184.6
'''A = Node(2.5/sqrt(2), 0, h)
B = Node(68.0, 0, 0)
C = Node(190-68.0, 0, 0)
D = Node(190-2.5/sqrt(2), 0, h)
E = Node(68.0, 25.0, 0)
F = Node(190-68.0, 25.0, 0)
G = Node(55.0, 55.0, h)
H = Node(55.0+80, 55.0, h)

AG = Line(A, G)
AE = Line(A, E)
BE = Line(B, E)
EG = Line(E, G)
EF = Line(E, F)
GH = Line(G, H)
CF = Line(C, F)
FH = Line(F, H)
DF = Line(D, F)
DH = Line(D, H)

AEG = Plane([AE, EG, AG])
ABE = Plane([AE, BE])
BCEF = Plane([BE, EF, CF])
EFGH = Plane([EF, FH, GH, EG])
CDF = Plane([CF, DF])
DFH = Plane([DF, FH, DH])

Moment = 4*YieldLines([AE, BE, EG, AG, EF, GH, CF, FH, DF, DH], 2996.1, h).MomentSum
Moment = Moment.evalf(subs={h:4.0})
print("For C6, the tensile capacity is %f" % (Moment/1000))'''
				
				



