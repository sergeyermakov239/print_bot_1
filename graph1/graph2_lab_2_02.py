import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

fig,ax=plt.subplots()
x=np.array([0.5,
1,
2,
3
])
y=np.array([-1.872961084,
-2.430008249,
-3.159402872,
-4.078576929
])

def f(x,a,b):
    return a+b*x
arr=np.arange(0,3.5,0.005)
params,_=curve_fit(f,x,y)
#print(params)
ax.plot(arr,f(arr,*params),'-r',label='$\ln(\gamma-\gamma_0)=-1.49-0.86 t$')
ax.plot(x,y,'ob', label='эксперимент')
ax.set_xlabel('t, c')
ax.set_title('$\ln(\gamma(t)-\gamma_0)$')
ax.legend()
#plt.savefig('graph2_lab_2_02.pdf')

plt.show()
