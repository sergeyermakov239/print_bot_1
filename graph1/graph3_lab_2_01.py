import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

t=np.array([
22.9,
35,
45.1,
57,
71.3
])
p5=np.array([
179.5,
184,
188.85,
193.35,
199.9
])
p9=np.array([
104.4,
108,
110.55,
113.75,
118.05
])
p12=np.array([
78.55,
81.35,
83.4,
86.75,
89.2
])

def f(x,a,b):
    return a+b*x
params5,_=curve_fit(f,t,p5)
params9,_=curve_fit(f,t,p9)
params12,_=curve_fit(f,t,p12)
arr=np.arange(20,75,0.005)
fig,ax=plt.subplots()
ax.plot(arr,f(arr,*params5),'-r',label='$V_ц=50\; мл$')
ax.plot(t,p5,'o',color='darkred')
ax.plot(arr,f(arr,*params9),'-b',label='$V_ц=90\; мл$')
ax.plot(t,p9,'^',color='darkblue')
ax.plot(arr,f(arr,*params12),'-g',label='$V_ц=120\; мл$')
ax.plot(t,p12,'s',color='darkgreen')
ax.legend()
ax.set_title('$p(t),\; кПа$')
ax.set_xlabel('$t, \; ^{\circ} C$')
plt.savefig('graph3_lab_2_01.pdf')