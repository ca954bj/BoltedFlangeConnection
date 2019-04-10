execfile('Curvesetup.py')
difflimit = 50

inputfile1 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts8SF2StrainG7Avg.txt"
inputfile1exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts8SF2StrainG7Exp.txt"

inputfile2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-2FEStrainG12Avg.txt"
inputfile2exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts4SF2StrainG17Exp.txt"
inputfile2exp2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-2ExpStrainG12.txt"

inputfile3 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-1FEStrainG1Avg.txt"
inputfile3exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Strain/Bolts4SF2StrainG1Exp.txt"

inputfile4 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2FEStrainG14Avg.txt"
inputfile4exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2ExpStrainG14.txt"
inputfile4exp2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-1ExpStrainG14.txt"

inputfile5 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1FEStrainG3.txt"
inputfile5exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1-1ExpStrainG3.txt"
inputfile5exp2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1-2ExpStrainG3.txt"

inputfile6 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1FEStrainG5.txt"
inputfile6exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1-1ExpStrainG5.txt"

inputfile7 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2FEStrainG2Avg.txt"
inputfile7exp = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2ExpStrainG2.txt"

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
data4exp2 = readfile(inputfile4exp2, difflimit)

data5 = readfile(inputfile5, difflimit)
data5exp = readfile(inputfile5exp, difflimit)
data5exp2 = readfile(inputfile5exp2, difflimit)

data6 = readfile(inputfile6, difflimit)
data6exp = readfile(inputfile6exp, difflimit)

data7 = readfile(inputfile7, difflimit)
data7exp = readfile(inputfile7exp, difflimit)

data1load = readfile(inputfile1load, difflimit)
data2load = readfile(inputfile2load, difflimit)
data3load = readfile(inputfile3load, difflimit)

plt.figure(figsize=(11, 11))
ax1 = plt.subplot(2, 2, 1)
plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.3, bottom=0.1, top=0.95)

# C3-1 G17 & C3-2 G12
p2, = plt.plot(data2.Fy1, data2load.Fy1, color='0.4', linestyle = '--', label='C3 G12 FEM')
#p2e, = plt.plot(data2exp.Uy1, data2exp.Fy1, color='black', linestyle = '-.', label='EXP1')
p2e2, = plt.plot(data2exp2.Uy1, data2exp2.Fy1, color='0.4', label='C3-2 G12 EXP')

# C2-2 G14 & C2-1 G14
p4, = plt.plot(data4.Fy1, data3load.Fy1, color='0.65', linestyle = '--', label='C2 G14 FEM')
#p4e, = plt.plot(data4exp.Uy1, data4exp.Fy1, color='black', linestyle = '-.', label='C2 EXP1')
p4e2, = plt.plot(data4exp2.Uy1[0:-350], data4exp2.Fy1[0:-350], color='0.65', label='C2-2 G14 EXP')

# C1-1 G3 & C1-2 G3
p5, = plt.plot(data5.Uy1, data5.Fy1, color='black', linestyle = '--', label='C1 G3 FEM')
p5e, = plt.plot(data5exp.Uy1, data5exp.Fy1, color='black', linestyle = '-', label='C1-1 G3 EXP1')
#p5e2, = plt.plot(data5exp2.Uy1, data5exp2.Fy1, color='black', label='C1 EXP2')

plt.xlim(-0.015,0.005)
plt.ylim(0, 200)
plt.xlabel('Strain', fontproperties=fontprop)
plt.ylabel('Load (kN)', fontproperties=fontprop)
plt.xticks([-0.015,-0.01,-0.005,0,0.005],('-1.5%','-1.0%','-0.5%','0','0.5%'))
plt.grid(linestyle='--')
plt.legend(handles=[p2, p2e2, p4, p4e2, p5, p5e], loc=1, bbox_to_anchor=(0.53, 0.55), prop=fontprop, frameon=False)

ax2 = plt.subplot(2, 2, 3)

p1, = plt.plot(data1.Fy1, data1load.Fy1, color='black', linestyle = '--', label='Bolts8 G7,FEM')
p1e, = plt.plot(data1exp.Uy1, data1exp.Fy1, color='black', label='Bolts8 G7,EXP')

plt.xlim(-0.015,0.015)
plt.ylim(0, 400)
plt.xticks([-0.015,-0.01,-0.005,0,0.005,0.01,0.015],('-1.5%','-1.0%','-0.5%','0','0.5%','1.0%','1.5%'))
plt.grid(linestyle='--')
plt.xlabel('Strain', fontproperties=fontprop)
plt.ylabel('Load (kN)', fontproperties=fontprop)

ax1 = plt.subplot(2, 2, 2)

# C1-1 G5
p6, = plt.plot(data6.Uy1, data6.Fy1, color='0.65', linestyle = '--', label='C1 G5 FEM')
p6e, = plt.plot(data6exp.Uy1, data6exp.Fy1, color='0.65', linestyle = '-', label='C1-1 G5 EXP')

# C2-2 G2
p7, = plt.plot(data7.Fy1, data3load.Fy1, color='black', linestyle = '--', label='C2 G2 FEM')
temp1 = [-i for i in data7exp.Uy1]
p7e, = plt.plot(temp1[0:-410], data7exp.Fy1[0:-410], color='black', linestyle = '-', label='C2-2 G2 EXP')

p3, = plt.plot(data3.Fy1[0:-10], data2load.Fy1[0:-10], color='0.4', linestyle = '--', label='C3 G1 FEM')
p3e, = plt.plot(data3exp.Uy1, data3exp.Fy1, color='0.4', label='C3-2 G1 EXP')

plt.legend(handles=[p6, p6e, p7, p7e, p3, p3e], loc=1, bbox_to_anchor=(0.5, 0.55), prop=fontprop, frameon=False)

plt.xlim(-0.01)
plt.ylim(0, 200)
plt.xlabel('Strain', fontproperties=fontprop)
plt.ylabel('Load (kN)', fontproperties=fontprop)
plt.xticks([-0.01,-0.008,-0.006,-0.004,-0.002,0],('-1%','-0.8%','-0.6%','-0.4%', '-0.2%', '0'))
plt.grid(linestyle='--')

plt.show()
