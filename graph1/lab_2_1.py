
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def f(x, a, c):
    return a*x + c



V = [50, 60, 70, 80, 90, 100, 110, 120]
p1 = [0.00613,
0.00671,
0.00772,
0.00884,
0.00995,
0.01099,
0.01224,
0.01342]
p2 = [0.00592,
0.00651,
0.00753,
0.00852,
0.00958,
0.01068,
0.01177,
0.01296]
p3 = [0.00581,
0.0064,
0.0074,
0.00839,
0.00938,
0.01038,
0.01149,
0.01256]
p4 = [0.00561,
0.00621,
0.00717,
0.00816,
0.00916,
0.01007,
0.01111,
0.01219]
p5 = [0.00553,
0.00607,
0.00705,
0.00802,
0.00892,
0.00992,
0.01084,
0.01185]


params1, _ = curve_fit(f, p1, V)
params2, _ = curve_fit(f, p2, V)
params3, _ = curve_fit(f, p3, V)
params4, _ = curve_fit(f, p4, V)
params5, _ = curve_fit(f, p5, V)

print(*params1)
print(*params2)
print(*params3)
print(*params4)
print(*params5)

V1 = []
for x in p1:
    V1.append(f(x, *params1))
V2 = []
for x in p2:
    V2.append(f(x, *params2))
V3 = []
for x in p3:
    V3.append(f(x, *params3))
V4 = []
for x in p4:
    V4.append(f(x, *params4))
V5 = []
for x in p5:
    V5.append(f(x, *params5))






line1 = plt.plot(p1, V, 'd',  label='', markersize=10)
plt.xlabel('1/p, 1/кПа')
plt.ylabel('$V, мл$')
plt.minorticks_on()
plt.tick_params(axis='both', which='major',
                   direction='out',
                   labelsize=10)
#plt.ylim(7.2, 31)
#plt.xlim(0.66, 2.44)

# Plot the fitted function
line2 = plt.plot(p1, V1, '-', label='$t_1 = 23.3 C$', lw=2)
plt.legend(framealpha=0.35, fontsize=12, loc='upper left')

line3 = plt.plot(p2, V, 'd',  label='', markersize=10)
plt.xlabel('1/p, 1/кПа')
plt.ylabel('$V, мл$')
plt.minorticks_on()
plt.tick_params(axis='both', which='major',
                   direction='out',
                   labelsize=10)
#plt.ylim(7.2, 31)
#plt.xlim(0.66, 2.44)

# Plot the fitted function
line4 = plt.plot(p2, V2, '-', label='$t_2 = 35.6 C$', lw=2)
plt.legend(framealpha=0.35, fontsize=12, loc='upper left')

line5 = plt.plot(p3, V, 'd',  label='', markersize=10)
plt.xlabel('1/p, 1/кПа')
plt.ylabel('$V, мл$')
plt.minorticks_on()
plt.tick_params(axis='both', which='major',
                   direction='out',
                   labelsize=10)
#plt.ylim(7.2, 31)
#plt.xlim(0.66, 2.44)

# Plot the fitted function
line6 = plt.plot(p3, V3, '-', label='$t_3 = 44.5 C$', lw=2)
plt.legend(framealpha=0.35, fontsize=12, loc='upper left')

line7 = plt.plot(p4, V, 'd',  label='', markersize=10)
plt.xlabel('1/p, 1/кПа')
plt.ylabel('$V, мл$')
plt.minorticks_on()
plt.tick_params(axis='both', which='major',
                   direction='out',
                   labelsize=10)
#plt.ylim(7.2, 31)
#plt.xlim(0.66, 2.44)

# Plot the fitted function
line8 = plt.plot(p4, V4, '-', label='$t_4 = 54.7 C$', lw=2)
plt.legend(framealpha=0.35, fontsize=12, loc='upper left')

line9 = plt.plot(p5, V, 'd',  label='', markersize=10)
plt.xlabel('1/p, 1/кПа')
plt.ylabel('$V, мл$')
plt.minorticks_on()
plt.tick_params(axis='both', which='major',
                   direction='out',
                   labelsize=10)
#plt.ylim(7.2, 31)
#plt.xlim(0.66, 2.44)

# Plot the fitted function
line10 = plt.plot(p5, V5, '-', label='$t_5 = 62.4 C$', lw=2)
plt.legend(framealpha=0.35, fontsize=12, loc='upper left')

plt.tight_layout()
plt.show()