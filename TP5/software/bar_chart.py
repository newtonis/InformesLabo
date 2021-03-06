import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log10

def formula_cuadrada(n):
    if n % 2 == 0:
        return 0
    else:
        xn = 2 * (0.125 / 2) / (np.pi * n)

        power = 2*xn**2/50
        return int(10*log10((power*1000.0))*10)/10


arr = [-11.4, -21.4, -26.6, -30.2, -33.3, -35, - 37, -44]
calc_dbm = [formula_cuadrada(i) for i in range(1, len(arr)*2+1, 2)]
print(arr)
print(calc_dbm)

men_means, men_std = arr, [0]*len(arr)
women_means, women_std = calc_dbm, [0]*len(arr)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                color='SkyBlue', label='Medido')
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                color='IndianRed', label='Teórico')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Potencia (dBm)')
ax.set_title('Señal cuadrada DC 50%, potencia de cada armónico')
ax.set_xticks(ind)
ax.set_xticklabels(('1', '3', '5', '7', '9', '11', '13', '15'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.
    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()