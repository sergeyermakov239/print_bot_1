import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

fig, ax=plt.subplots()
t=np.array([
0.5,
1,
2,
3
])
gamma=np.array([1.323667964,
1.258036106,
1.212451082,
1.186931543
])
terr=np.array([0.5]*4)
gammaerr=np.array([0.008,
0.005,
0.01,
0.002
])
ax.errorbar(t,gamma,yerr=gammaerr,xerr=terr,fmt='o',ecolor='b',capsize=4,label='$\gamma_{э}(t)$')
arr=np.arange(0,4,0.005)
def f(x,a,b,c):
    return a+b*2.71828**(-c*x)
params,_=curve_fit(f,t,gamma)
params1=(1.17,0.22546,0.8588)
ax.plot(arr,f(arr,*params1),'--r', label='$\gamma=1,17+0,225\cdot e^{-0,86 t}$')
print(*params)
ax.legend()
ax.set_title('$\gamma(t)$')
ax.set_xlabel('t, c')
#plt.savefig('graph1_lab_2_02.pdf')
plt.show()