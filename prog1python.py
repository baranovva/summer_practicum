k = 1.4
u = 700
E = 10e-8
R = 8.314463
m = 29*10e-3
M_start=float(input('M_start  '))
M_end=float(input('M_end    '))
k1 = 2/(k+1)
k2 = k-1
k3 = k1*k2

def A(x): 
    return 0.98 * abs(x**(1/3)) + 0.05
A1 = A(0)
A2 = A(1)

def mpd(f,a,b):
    global E
    while abs(b-a)>E:
        c = (a + b)/2
        if f(a)*f(c) < 0:
            b = c
        elif f(b)*f(c) < 0:
            a = c
        elif f(c) == 0:
            return c
        if abs(b-a) <= E:
            return c
    return c

f = lambda M2: (M2*(A2/A1))**k3 /k1 - (k2/2)*M2**2 - 1
M2 = mpd(f,M_start,M_end)
a2 = u/M2
T2 = a2**2 *m/(k*R)
T0 = (1+ (k2/2)*(M2**2))*T2
print('M2 = ', "%.2f" % M2)
print('a2 = ',"%.2f" % a2,'m/c')
print('T2 = ',"%.2f" %T2,'K')
print('T0 = ',"%.2f" % T0,'K')
