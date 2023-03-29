import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

v=np.array([
0.02,
0.016666667,
0.014285714,
0.0125,
0.011111111,
0.01,
0.009090909,
0.008333333
])
t=np.array([
-401.6,
-381,
-354,
-354.7,
-351.9,
-346.9,
-343.2,
-327.6
])

def f(x,a,b):
    return a+b*x
params,_=curve_fit(f,v,t)
print(params)
arr=np.arange(0.007,0.021,0.00005)

fig,ax=plt.subplots()
line,=ax.plot(arr,f(arr,*params),'-r')
marker,=ax.plot(v,t,'ob')
ax.legend([(line,marker)],['$\widetilde{t}_*=-286.8-5550.5\dfrac{1}{V_{ц}}$'])
ax.set_title('$\widetilde{t}_*(1/V_{ц}),\; ^{\circ} C$')
ax.set_xlabel('$1/V_{ц}, \; мл^{-1}$')
plt.savefig('graph4_lab_2_01.pdf')