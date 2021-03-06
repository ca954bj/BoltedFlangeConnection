execfile('Curvesetup.py')
difflimit = 50

Fnx = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C5-2FEStrainG15xAvg.txt"
Fny = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C5-2FEStrainG15yAvg.txt"
Fnxy ="/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C5-2FEStrainG15xyAvg.txt"

Fnw = open("/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C5-2FEStrainG15Avg.txt", 'w')

Stressx = readfile(Fnx, difflimit)
Stressy = readfile(Fny, difflimit)
Stressxy = readfile(Fnxy, difflimit)

length = len(Stressx.Fy1)
Stress = []

for i in range(0, length):
	temp = 0.5*(Stressx.Fy1[i] + Stressy.Fy1[i])-Stressxy.Fy1[i]/2
	Stress.append(temp)
	Fnw.write("%f %f\n" % (Stressx.Uy1[i], temp))

Fnw.close()
