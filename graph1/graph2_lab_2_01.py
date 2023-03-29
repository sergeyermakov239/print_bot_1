import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

t=np.array([22.9,
35.0,
45.1,
57.0,
71.3
])
k=np.array([
9820.7,
10185.0,
10530.0,
10933.0,
11291.0
])
def f(x,a,b):
    return a+b*x
params,_=curve_fit(f,t,k)
arr=np.arange(20,75,0.05)
print(params)
fig,ax=plt.subplots()
line,=ax.plot(arr,f(arr,*params),'-r')
marker,=ax.plot(t,k,'ob')
ax.legend([(line,marker)],['$K=30.9t+9120$'])
ax.set_title('$K(t),\; Дж$')
ax.set_xlabel('$t,\; ^{\circ} C$')
plt.savefig('graph2_lab_2_01.pdf')