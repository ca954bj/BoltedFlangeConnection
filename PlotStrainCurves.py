execfile('Curvesetup.py')
difflimit = 50

inputfile1 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts8SF2StrainG7Avg.txt"
inputfile1exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts8SF2StrainG7Exp.txt"

inputfile2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-2FEStrainG12Avg.txt"
inputfile2exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts4SF2StrainG17Exp.txt"
inputfile2exp2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-2ExpStrainG12.txt"

inputfile3 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts4SF2StrainG1Avg.txt"
inputfile3exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts4SF2StrainG1Exp.txt"

inputfile4 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2FEStrainG14Avg.txt"
inputfile4exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2ExpStrainG14.txt"

inputfile1load = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/sf82fem.txt"
inputfile2load = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/sf2fem.txt"
inputfile3load = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/sf1fem.txt"

data1 = readfile(inputfile1, difflimit)
data1exp = readfile(inputfile1exp, difflimit)

data2 = readfile(inputfile2, difflimit)
data2exp = readfile(inputfile2exp, difflimit)
data2exp2 = readfile(inputfile2exp2, difflimit)

data3 = readfile(inputfile3, difflimit)
data3exp = readfile(inputfile3exp, difflimit)

data4 = readfile(inputfile4, difflimit)
data4exp = readfile(inputfile4exp, difflimit)

data1load = readfile(inputfile1load, difflimit)
data2load = readfile(inputfile2load, difflimit)
data3load = readfile(inputfile3load, difflimit)

plt.figure(figsize=(11, 5))
ax1 = plt.subplot(1, 2, 1)

p2, = plt.plot(data2.Fy1, data2load.Fy1, color='black', linestyle = '--', label='C3-2 G17,FEM')
p2e, = plt.plot(data2exp.Uy1, data2exp.Fy1, color='black', label='C3-1 G17,EXP')
p2e2, = plt.plot(data2exp2.Uy1, data2exp2.Fy1, color='black', label='C3-2 G12,EXP')

#p3, = plt.plot(data3.Fy1, data2load.Fy1, color='black', linestyle = '--', label='C3-2 G1,FEM')
#p3e, = plt.plot(data3exp.Uy1, data3exp.Fy1, color='black', label='Bolts4 G1,EXP')

p4, = plt.plot(data4.Fy1, data3load.Fy1, color='black', linestyle = '--', label='C2-2 G14,FEM')
p4e, = plt.plot(data4exp.Uy1, data4exp.Fy1, color='black', label='C2-2 G14,EXP')

plt.xlim(-0.01,0.01)
plt.ylim(0, 200)

ax2 = plt.subplot(1, 2, 2)

p1, = plt.plot(data1.Fy1, data1load.Fy1, color='black', linestyle = '--', label='Bolts8 G7,FEM')
p1e, = plt.plot(data1exp.Uy1, data1exp.Fy1, color='black', label='Bolts8 G7,EXP')

plt.xlim(-0.01,0.01)
plt.ylim(0, 400)

plt.show()
