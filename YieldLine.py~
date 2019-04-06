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
				print("The lines are not right!")
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
				MomentSum += Moment
		self.MomentSum = MomentSum
	def MomentSum(self):
		return self.MomentSum
		
# Problem C2 103.9kN
h = Symbol('h')
A = Node(0, 35.0, 0)
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
print("For C2, the tensile capacity is %f" % (Moment/1000))

				
				
				



