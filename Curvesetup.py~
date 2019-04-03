import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


class readfile:
    def __init__(self, infile, difflimit):
        content = open(infile)
        Uy1 = []
        Fy1 = []

        for line in content:
            words = line.split()
            if len(words) > 0:
                try:
                    temp = float(words[0])
                except:
                    temp = 'No'
                    print('Fail')
                if type(temp) == float:
                    if float(words[0]) <= 10:
                        Fy1.append(float(words[1]))
                        Uy1.append(float(words[0]))

        content.close()

        self.Uy1 = Uy1
        self.Fy1 = Fy1

    def Uy1(self):
        return self.Uy1
    def Fy1(self):
        return self.Fy1


fontpath = '/usr/share/fonts/truetype/msttcorefonts/Arial.ttf'
fontprop = fm.FontProperties(family='Arial', fname=fontpath, size=16)
mpl.rcParams.update({'font.size': 16, 'font.family': 'Arial'})

