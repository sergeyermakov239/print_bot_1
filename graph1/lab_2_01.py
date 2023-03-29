import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

v=np.array([50,
60,
70,
80,
90,
100,
110,
120
])
p1=np.array([0.005571031,
0.00655308,
0.007544323,
0.00855432,
0.009578544,
0.010587612,
0.011600928,
0.012730745
])
p2=np.array([0.00543478260869565,
0.00632311097059753,
0.00730193501277839,
0.00826104915324246,
0.00925925925925926,
0.0102406554019457,
0.0112485939257593,
0.0122925629993854
])
p3=np.array([0.0052952078369076,
0.00620925178515989,
0.00716845878136201,
0.00809716599190283,
0.00904568068747173,
0.00995520159283225,
0.0109229929000546,
0.0119904076738609
])
p4=np.array([0.00517196793379881,
0.00600600600600601,
0.00691562932226833,
0.00785854616895874,
0.00879120879120879,
0.00971817298347911,
0.0106044538706257,
0.0115273775216138
])
p5=np.array([0.00500250125062531,
0.00584966364434045,
0.00668672684720829,
0.00756715853197124,
0.00847098686997035,
0.00934579439252336,
0.0102564102564103,
0.0112107623318386
])

def f(x,a,b):
    return a+b*x
params1,_=curve_fit(f,p1,v)
print(params1)
params2,_=curve_fit(f,p2,v)
print(params1)
params3,_=curve_fit(f,p3,v)
print(params1)
params4,_=curve_fit(f,p4,v)
print(params1)
params5,_=curve_fit(f,p5,v)
arr=np.arange(0.0049,0.0129,0.00005)
fig,ax=plt.subplots()
ax.plot(p1,f(p1,*params1),'-r',linewidth=1,label='$t_1=22,9\;^{\circ} C$')
ax.plot(p1,v,'.', color='darkred')
ax.plot(p2,f(p2,*params2),'-b',linewidth=1,label='$t_2=35\;^{\circ} C$')
ax.plot(p2,v,'.', color='darkblue')
ax.plot(p3,f(p3,*params3),'-g',linewidth=1,label='$t_3=45,1\;^{\circ} C$')
ax.plot(p3,v,'.', color='darkgreen')
ax.plot(p4,f(p4,*params4),'-m',linewidth=1,label='$t_4=57\;^{\circ} C$')
ax.plot(p4,v,'.', color='darkmagenta')
ax.plot(p5,f(p5,*params5),'-c',linewidth=1,label='$t_5=71,3\;^{\circ} C$')
ax.plot(p5,v,'.', color='darkcyan')
ax.set_title('$V_{ц}(1/p),\; мл$')
ax.set_xlabel('$1/p,\; кПа^{-1}$')
ax.legend()
plt.savefig('graph1_lab_2_01.pdf')