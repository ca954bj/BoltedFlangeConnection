execfile('Curvesetup.py')

fn = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/Bolts4Strains.txt"
data = dict()
data["FE"] = dict()
data["Exp"] = dict()
label = []

content = open(fn, 'r')
for line in content:
	splited = line.split()
	if len(splited) > 0:
		att = splited[0]
		name = splited[1]
		kind = splited[2]
		if name not in data[att].keys():
			data[att][name] = dict()
		data[att][name][kind] = []
		for i in splited[3:-1]:
			data[att][name][kind].append(float(i))
			
plt.figure(figsize=(11, 9))

FirstGraph = ["G1", "G2"]
SecondGraph = ["G3", "G4", "G5"]

ax1 = plt.subplot(2, 2, 1)
plt.grid(linestyle='--')

plt.xlim(-0.02,0.02)
plt.ylim(0, 200)
plt.xticks([-0.02, -0.01, 0, 0.01, 0.02],('-2%','-1%','0','1%','2%'), fontproperties=fontprop)
plt.yticks([0, 50, 100, 150, 200], ('0', '50', '100', '150', '200'), fontproperties=fontprop)

p1 = dict()
for att, value1 in data.iteritems():
	if att == "FE":
		thelinestyle = '--'
	elif att == "Exp":
		thelinestyle = '-'
	for name, value2 in value1.iteritems():
		if name in FirstGraph:
			thelabel = att + " " + name
			length = min(len(data[att][name]['Strain']), len(data[att][name]['Load']))
			plt.plot(data[att][name]['Strain'][0:length], data[att][name]["Load"][0:length], color='0', linestyle = thelinestyle, label=thelabel)

ax2 = plt.subplot(2, 2, 2)
plt.grid(linestyle='--')

plt.xlim(-0.02,0.02)
plt.ylim(0, 200)
plt.xticks([-0.02, -0.01, 0, 0.01, 0.02],('-2%','-1%','0','1%','2%'), fontproperties=fontprop)
plt.yticks([0, 50, 100, 150, 200], ('0', '50', '100', '150', '200'), fontproperties=fontprop)

p2 = dict()
for att, value1 in data.iteritems():
	if att == "FE":
		thelinestyle = '--'
	elif att == "Exp":
		thelinestyle = '-'
	for name, value2 in value1.iteritems():
		if name in SecondGraph:
			thelabel = att + " " + name
			length = min(len(data[att][name]['Strain']), len(data[att][name]['Load']))
			plt.plot(data[att][name]["Strain"][0:length], data[att][name]["Load"][0:length], color='0', linestyle = thelinestyle, label=thelabel)

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.3, bottom=0.1, top=0.95)	
print("Done")
plt.show()
