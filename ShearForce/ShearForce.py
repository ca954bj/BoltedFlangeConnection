fn1 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/ShearForce/C1ShearForce"
fn2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/ShearForce/Bolt4-NoSF-335MPa.inp"

con1 = open(fn1, 'r')
nodeset = []
stressset = []

frame = -1

steps = []
flag = 0
for line in con1:
	inline = line.split()
	length = len(inline)
	if length > 0:
		if inline[0] == 'X':
			for i in range(2, length+1):
				try:
					nodenum = int(inline[i])
					nodeset.append(nodenum)
				except:
					pass
		if inline[0] == '0.':
			print("Now it's zero, begin!")
			nodec = len(nodeset)
			for i in range(0, nodec):
				stressset.append([])
			flag = 1
		if flag == 1:
			step = float(inline[0])
			if step not in steps:
				steps.append(step)
				for i in range(0, nodec):
					stressset[i].append(float(inline[i+1]))
				
print('NodeSet')
print(nodeset)
print('StressSet')
print(stressset[0])
print(stressset[nodec - 1])

con1.close()

con2 = open(fn2, 'r')
flag = 0
NodeCoord = []
for i in range(0, nodec/2):
	NodeCoord.append([])
for line in con2:
	if "*Part, name=Combination" in line:
		print(line)
		flag = 1
		print("Begin to find coordinates")
	if "*Element" in line:
		flag = 0
	if flag == 1:
		co = line.split(',')
		if len(co) == 4:
			temp1 = int(co[0])
			for i in range(0, nodec):
				if nodeset[i] == temp1:
					NodeCoord[i].append(float(co[1]))
					NodeCoord[i].append(float(co[2]))
					NodeCoord[i].append(float(co[3]))
					break

print(NodeCoord)

nodec2 = nodec/2
nodec3 = nodec2/7
Labels = []

for i in range(nodec2):
	Labels.append(0)

temp1 = 1
for i in range(nodec2):
	if Labels[i] == 0:
		Selected = filter(lambda xx: NodeCoord[xx][0] == NodeCoord[i][0] and NodeCoord[xx][1] == NodeCoord[i][1], range(0, nodec2))
		for obj in Selected:
			Labels[obj] = temp1
		temp1 += 1

for i in range(1, nodec3 + 1):
	Selected = filter(lambda xx: Labels[xx] == i, range(0, nodec2))
	Selected = map(lambda xx: NodeCoord[xx], Selected)
	Selected = sorted(Selected, key=lambda xx: xx[2])
	print(i, Selected)
