inputfile1 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1-1ExpLoadDisp.txt"
inputfile12 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C1-2ExpLoadDisp.txt"
inputfile1f = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/NoSFfem.txt"
inputfile2 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-1ExpLoadDisp.txt"
inputfile22 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C2-2ExpLoadDisp.txt"
inputfile2f = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/sf1fem.txt"
inputfile3 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-1ExpLoadDisp.txt"
inputfile32 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/C3-2ExpLoadDisp.txt"
inputfile3f = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt4/sf2fem.txt"

inputfile4 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/NoSF.txt"
inputfile42 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C4-2ExpLoadDisp.txt"
inputfile4f = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/NoSFfem.txt"
inputfile5 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/sf81.txt"
inputfile5f = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/sf81fem.txt"
inputfile52 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C5-2ExpLoadDisp.txt"
inputfile6 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/sf82.txt"
inputfile62 = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/C6-2ExpLoadDisp.txt"
inputfile6f = "/media/chenting/Work/Structural Engineering/Bolt Analysis/Bolt8/sf82fem.txt"

style = 'BlackWithoutMarker'
#style = 'Color'


execfile('Curvesetup.py')
difflimit = 50
data1 = readfile(inputfile1, difflimit)
data12 = readfile(inputfile12, difflimit)
data1f = readfile(inputfile1f, difflimit)
data2 = readfile(inputfile2, difflimit)
data22 = readfile(inputfile22, difflimit)
data2f = readfile(inputfile2f, difflimit)
data3 = readfile(inputfile3, difflimit)
data32 = readfile(inputfile32, difflimit)
data3f = readfile(inputfile3f, difflimit)
data4 = readfile(inputfile4, difflimit)
data42 = readfile(inputfile42, difflimit)
data4f = readfile(inputfile4f, difflimit)
data5 = readfile(inputfile5, difflimit)
data52 = readfile(inputfile52, difflimit)
data5f = readfile(inputfile5f, difflimit)
data6 = readfile(inputfile6, difflimit)
data62 = readfile(inputfile62, difflimit)
data6f = readfile(inputfile6f, difflimit)

plt.figure(figsize=(11, 5))
ax1 = plt.subplot(1, 2, 1)
#plt.plot(Uy1[0:-180], Fy1[0:-180])

if style == 'Color':
	p1, = plt.plot(data1.Uy1, data1.Fy1, color='b', label='C1')
	p1r, = plt.plot(data1f.Uy1, data1f.Fy1, color='b', label='C1', linestyle='--')
	p2, = plt.plot(data2.Uy1, data2.Fy1, color='g', label='C2')
	p2r, = plt.plot(data2f.Uy1, data2f.Fy1, color='g', label='C2', linestyle='--')
	p3, = plt.plot(data3.Uy1, data3.Fy1, color='r', label='C3')
	p3r, = plt.plot(data3f.Uy1, data3f.Fy1, color='r', label='C3', linestyle='--')
elif style == 'BlackWithMarker':
	p1, = plt.plot(data1.Uy1, data1.Fy1, color='black', label='C1', marker='^', markersize=10, markevery=(40, 20))
	p12, = plt.plot(data12.Uy1, data12.Fy1, color='black', label='C1', linestyle='-.', marker='^', markersize=10, markevery=(40, 20))
	p1r, = plt.plot(data1f.Uy1, data1f.Fy1, color='black', label='C1', linestyle='--', marker='^', markersize=10, markevery=(12, 7))
	p2, = plt.plot(data2.Uy1, data2.Fy1, color='black', label='C2', marker='v', markersize=10, markevery=(300, 300))
	p22, = plt.plot(data22.Uy1, data22.Fy1, color='black', label='C2', linestyle='-.', marker='v', markersize=10, markevery=(300, 300))
	p2r, = plt.plot(data2f.Uy1, data2f.Fy1, color='black', label='C2', linestyle='--', marker='v', markersize=10, markevery=(12, 5))
	p3, = plt.plot(data3.Uy1, data3.Fy1, color='black', label='C3', marker='o', markersize=10, markevery=(35, 200))
	p32, = plt.plot(data32.Uy1, data32.Fy1, color='black', label='C3', linestyle='-.', marker='o', markersize=10, markevery=(35, 200))
	p3r, = plt.plot(data3f.Uy1, data3f.Fy1, color='black', label='C3', linestyle='--', marker='o', markersize=10, markevery=(11, 5))
	
	firstlegend = plt.legend(handles=[p1, p2, p3], loc=1, bbox_to_anchor=(0.514, 0.38), prop=fontprop, title='Exp1:', frameon=False)
	thirdlegend = plt.legend(handles=[p12, p22, p32], loc=1, bbox_to_anchor=(0.757, 0.38), prop=fontprop, title='Exp2:', frameon=False)
	secondlegend = plt.legend(handles=[p1r, p2r, p3r], loc=1, bbox_to_anchor=(1.0, 0.38), prop=fontprop, title='FEM:', frameon=False)
	plt.gca().add_artist(firstlegend)
	plt.gca().add_artist(secondlegend)
	plt.gca().add_artist(thirdlegend)
	
elif style == 'BlackWithoutMarker':
	p1, = plt.plot(data1.Uy1, data1.Fy1, color='black', label='Exp1')
	p12, = plt.plot(data12.Uy1, data12.Fy1, color='black', label='Exp2', linestyle='-.')
	p1r, = plt.plot(data1f.Uy1, data1f.Fy1, color='black', label='FEM', linestyle='--')
	p2, = plt.plot(data2.Uy1, data2.Fy1, color='black', label='C2')
	p22, = plt.plot(data22.Uy1, data22.Fy1, color='black', label='C2', linestyle='-.')
	p2r, = plt.plot(data2f.Uy1, data2f.Fy1, color='black', label='C2', linestyle='--')
	p3, = plt.plot(data3.Uy1, data3.Fy1, color='black', label='C3')
	p32, = plt.plot(data32.Uy1, data32.Fy1, color='black', label='C3', linestyle='-.')
	p3r, = plt.plot(data3f.Uy1, data3f.Fy1, color='black', label='C3', linestyle='--')
	
	firstlegend = plt.legend(handles=[p1, p12, p1r], loc=1, bbox_to_anchor=(1.0, 0.3), prop=fontprop, frameon=False)
	plt.gca().add_artist(firstlegend)

plt.grid(linestyle='--')
plt.ylim(0, 200)
plt.xlim(0, 4)
plt.xticks([0, 1, 2, 3, 4], fontproperties=fontprop)
plt.yticks([0, 50, 100, 150, 200], fontproperties=fontprop)
plt.xlabel('Axial Extension (mm)', fontproperties=fontprop)
plt.ylabel('Axial Force (kN)', fontproperties=fontprop)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# The second pic


ax2 = plt.subplot(1, 2, 2)
#plt.plot(Uy2[0:-200], Fy2[0:-200])

if style == 'Color':
	p4, = plt.plot(data4.Uy1, data4.Fy1, color='b', label='C4')
	p4r, = plt.plot(data4f.Uy1, data4f.Fy1, color='b', label='C4', linestyle='--')
	p5, = plt.plot(data5.Uy1, data5.Fy1, color='g', label='C5')
	p5r, = plt.plot(data5f.Uy1, data5f.Fy1, color='g', label='C5', linestyle='--')
	p6, = plt.plot(data6.Uy1, data6.Fy1, color='r', label='C6')
	p6r, = plt.plot(data6f.Uy1, data6f.Fy1, color='r', label='C6', linestyle='--')
	
elif style == 'BlackWithMarker':
	p4, = plt.plot(data4.Uy1, data4.Fy1, color='black', label='C4', marker='^', markersize=10, markevery=(70, 100))
	p4r, = plt.plot(data4f.Uy1, data4f.Fy1, color='black', label='C4', linestyle='--', marker='^', markersize=10, markevery=(14, 5))
	p5, = plt.plot(data5.Uy1, data5.Fy1, color='black', label='C5', marker='v', markersize=10, markevery=(650, 500))
	p5r, = plt.plot(data5f.Uy1, data5f.Fy1, color='black', label='C5', linestyle='--', marker='v', markersize=10, markevery=(14, 5))
	p6, = plt.plot(data6.Uy1, data6.Fy1, color='black', label='C6', marker='o', markersize=10, markevery=(25, 20))
	p6r, = plt.plot(data6f.Uy1, data6f.Fy1, color='black', label='C6', linestyle='--', marker='o', markersize=10, markevery=(11, 5))

	fourthlegend = plt.legend(handles=[p4, p5, p6], loc=1, bbox_to_anchor=(0.757, 0.38), prop=fontprop, title='Exp:', frameon=False)
	fifthlegend = plt.legend(handles=[p4r, p5r, p6r], loc=1, bbox_to_anchor=(1.0, 0.38), prop=fontprop, title='FEM:', frameon=False)

	plt.gca().add_artist(fourthlegend)
	plt.gca().add_artist(fifthlegend)

elif style == 'BlackWithoutMarker':
	p4, = plt.plot(data4.Uy1, data4.Fy1, color='black', label='Exp1')
	p42, = plt.plot(data42.Uy1, data42.Fy1, color='black', label='Exp2', linestyle='-.')
	p4r, = plt.plot(data4f.Uy1, data4f.Fy1, color='black', label='FEM', linestyle='--')
	p5, = plt.plot(data5.Uy1, data5.Fy1, color='black', label='Exp1')
	p52, = plt.plot(data52.Uy1, data52.Fy1, color='black', label='Exp2', linestyle='-.')
	p5r, = plt.plot(data5f.Uy1, data5f.Fy1, color='black', label='FE', linestyle='--')
	p6, = plt.plot(data6.Uy1, data6.Fy1, color='black', label='C6')
	p62, = plt.plot(data62.Uy1, data62.Fy1, color='black', label='C6', linestyle='-.')
	p6r, = plt.plot(data6f.Uy1, data6f.Fy1, color='black', label='C6', linestyle='--')

	fourthlegend = plt.legend(handles=[p5, p52, p5r], loc=1, bbox_to_anchor=(1.0, 0.3), prop=fontprop, frameon=False)
	plt.gca().add_artist(fourthlegend)

plt.grid(linestyle='--')
plt.ylim(0, 500)
plt.xlim(0, 4)
#plt.xlim(0, 180)
plt.xticks([0, 1, 2, 3, 4], fontproperties=fontprop)
plt.yticks([0, 100, 200, 300, 400, 500], fontproperties=fontprop)
plt.xlabel('Axial Extension (mm)', fontproperties=fontprop)
plt.ylabel('Axial Force (kN)', fontproperties=fontprop)
ax2.yaxis.set_label_coords(-0.12, 0.5)

plt.subplots_adjust(left=0.08, right=0.98, wspace=0.22, hspace=0.1, bottom=0.12, top=0.95)

plt.show()

