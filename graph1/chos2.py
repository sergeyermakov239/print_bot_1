import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

pal = ['#953ac4','#8353ce','#6a70db','#548be6','#3ea5f2','#28bfff']
c1=str(pal[0])
c2=str(pal[1])
c3=str(pal[2])
c4=str(pal[3])
c5=str(pal[4])
c6=str(pal[5])

sns.set(rc={'axes.axisbelow': False,'axes.edgecolor': 'black',
 'axes.facecolor': 'white',
 'axes.grid': False,
 'axes.labelcolor': 'black',
 'axes.labelsize': 18,
 'axes.spines.right': True,
 'axes.spines.top': True,
 'figure.facecolor': 'white',
 'lines.solid_capstyle': 'round',
 'patch.edgecolor': 'w',
 'patch.force_edgecolor': True,
 'text.color': 'black',
 'xtick.bottom': True,
 'xtick.color': 'black',
 'xtick.direction': 'out',
 'xtick.top': False,
 'ytick.color': 'black',
 'ytick.direction': 'out',
 'ytick.left': True,
 'axes.titlesize':22,
 "font.size":18,
 'ytick.right': False})
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams["figure.figsize"] = (8,6)

def f(x, R, b, c):
    return -R * np.cosh((x - b) / R) + c
    #return (((l**2 / 4) - H**2)/(2*H))*(np.cosh((2*H*x)/((l**2 / 4) - H**2)) - 1)

      #x_obs = [-2.05E-02,
      #-1.70E-02,
      #-1.17E-02,
      #-1.04E-02,
      #-6.73E-03,
      #-3.51E-03,
      #2.94E-03,
      #7.08E-03,
      #1.21E-02,
      #1.86E-02,
      #2.78E-02,
      #3.42E-02,
      #4.48E-02,
      #5.77E-02,
      #7.06E-02,
      #7.98E-02,
      #9.27E-02,
      #0.101,
      #0.107,
      #0.114,
      #0.118,
     # 0.124,
     # 0.131, 0.135, 0.137, 0.139, 0.141, 0.143, 0.144, 0.144, 0.146, 0.147, 0.148, 0.148, 0.148, 0.147]



x_obs = [0.632, 0.605, 0.588, 0.566, 0.546, 0.492, 0.451, 0.413, 0.373, 0.325, 0.265, 0.197, 0.124, 6.19E-02,
         -7.91E-03, -7.55E-02, -0.153, -0.238, -0.324, -0.412, -0.476, -0.524, -0.573, -0.62, -0.651]

x_obs = [x * 100 for x in x_obs]

# Observed y values
#y_obs = [0.139,
#0.155,
#0.167,
#0.178,
#0.191,
#0.204,
#0.222,
#0.232,
#0.239,
#0.247,
#0.256,
#0.261,
#0.265,
#0.267,
#0.268,
#0.265,
#0.26,
#0.252,
#0.244,
#.235,
#0.225,
#0.216,
#0.2,
#0.187,
#0.173,
#0.16,
#0.145,
#0.13,
#0.117,
#0.102,
#8.54E-02,
#6.80E-02,
#5.23E-02,
#3.35E-02,
#1.46E-02,
#-3.37E-03]


y_obs = [0.546, 0.493, 0.458, 0.422, 0.386, 0.308, 0.253, 0.209, 0.168, 0.124, 8.20E-02, 4.68E-02, 1.94E-02,
         6.48E-03, 1.44E-03, 7.91E-03, 2.37E-02, 5.97E-02, 0.113, 0.186, 0.257, 0.323, 0.404, 0.484, 0.547]

y_obs = [y * 100 for y in y_obs]

# Fit the function to the data
params, _ = curve_fit(f, x_obs, y_obs)

# Print the fitted parameters
print(*params)
import matplotlib.pyplot as plt

# Generate a range of x values to use for plotting the fitted function
x = np.linspace(x_obs[0], x_obs[-1], 100)

# Calculate the fitted y values using the fitted parameters
y = f(x, *params) + 0.25

line1 = plt.plot(x_obs, y_obs, 'd', c=c1, label='Эксперимент', markersize=10)
plt.xlabel('x, см')
plt.ylabel('y, см')
plt.minorticks_on()
plt.tick_params(axis='both', which='major',
                   direction='out',
                   labelsize=16)
#plt.ylim(7.2, 31)
#plt.xlim(0.66, 2.44)

# Plot the fitted function
#line2 = plt.plot(x, y, '-', label='Аппроксимация, $y = -3.005cosh(\dfrac{x - 3.514}{3.005}) + 24.873$', color =c3, lw=2)
line2 = plt.plot(x, y, '-', label='Аппроксимация, $y = -3.225cosh(\dfrac{x - 5.941}{3.225}) + 31.796$', color =c3, lw=2)
plt.legend(framealpha=0.35, fontsize=12, loc='lower left')
# Add a legend and show the plot
plt.tight_layout()
plt.savefig('graph_chosinus_1.pdf')