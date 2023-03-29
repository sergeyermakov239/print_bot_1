import math

import numpy as np
import matplotlib.pyplot as plt

xx='10.2009	10.2592	10.305	10.29164	10.3508	10.3578	10.3761	10.3944	10.42185	10.4493	10.47444	10.49037	10.50863	10.55184	10.5469	10.5676	10.6015	10.61712	10.6119	10.63004	10.63911	10.6609	10.6672	'

yy='0.12078346	0.122270742	0.122816594	0.123194748	0.123362445	0.123715847	0.123934426	0.124153005	0.124480874	0.124808743	0.125382932	0.12584885	0.126067908	0.126864035	0.127362637	0.127332602	0.128021978	0.128492849	0.128996692	0.1292172	0.129327453	0.130165746	0.130530973'

x1=list(map((float),xx.split()))
y1=list(map((float),yy.split()))

x=np.array(x1)
y=np.array(y1)
x_avg=x.sum()/len(x)
y_avg=y.sum()/len(y)

#y=a+b*x

numerator=0
D=0
for i in range(len(x)):
    D= D + (x[i] - x_avg) ** 2
    numerator= numerator + (x[i] - x_avg) * (y[i] - y_avg)
b= numerator / D
a=y_avg-b*x_avg
print('y=a+b*x')
print(f'y = {a:.4f} + {b:.4f}*x')

d=0
for i in range(len(x)):
    d+=( y[i]-a-b*x[i] )**2
sigma_b=math.sqrt(d/(D*(len(x)-2)))
sigma_a=math.sqrt( (1/len(x)+x_avg/D)*d/(len(x)-2)  )

tt='12.7062047	4.3026527	3.1824463	2.7764451	2.5705818	2.4469119	2.3646243	2.3060041	2.2621572	2.2281389	2.2009852	2.1788128	2.1603687	2.1447867	2.1314495	2.1199053	2.1098156	2.100922	2.0930241	2.0859634	2.0796138	2.0738731	2.0686576	2.0638986	2.0595386	2.0555294	2.0518305	2.0484071	2.0452296	2.0422725	2.0395134	2.0369333	2.0345153	2.0322445	2.0301079	2.028094	2.0261925	2.0243942	2.0226909	2.0210754	2.019541	2.0180817	2.0166922	2.0153676	2.0141034	2.0128956	2.0117405	2.0106348	2.0095752	2.0085591'
t1=list(map((float),tt.split()))
t=np.array(t1)

delta_a=t[len(x)-2]*sigma_a/math.sqrt(len(x))
delta_b=t[len(x)-2]*sigma_b/math.sqrt(len(x))

print(f'Delta_a={delta_a:.4f}, Delta_b={delta_b:.6f}')

def f(x):
    return a+b*x

fig,ax=plt.subplots()

line,=ax.plot(x,f(x),'-r')
marker,=ax.plot(x,y,'ob',linewidth=1)
ax.legend([(line,marker)],['$R=-0.077+0.019\cdot P$'])
ax.set_title('$R(P)$')
ax.set_xlabel('$P, Вт$')



#plt.show()
plt.savefig('graph1_lab_2_09.pdf')