import numpy as np
from scipy import fft as FFT
import matplotlib.pyplot as plt

π = np.pi

σx = 0.05
σy = 0.02
R = 1.5
N = 1024
k = 10000
a = 0.
b = 1/200
c = 10.
z = 100.
D = 2*R/N
s = np.linspace(0.5*D-R, R-0.5*D, num = N)
f = FFT.fftshift(FFT.fftfreq(N, d = D))
x,y = np.meshgrid(s,s)
u,v = np.meshgrid(f,f)
J = 2*np.sinc(2*(u**2 + v**2)**0.5)*np.exp(-2*π*π*((σx*u)**2 + (σy*v)**2))
J2 = np.exp(1j*(((k*a*u + k*a*v)**3)-((k*b*u + k*b*v)**2)+(k*c*u + k*c*v)))*1j*k/z*np.exp(1j*k*z)*np.exp((1j*k*u**2+1j*k*v**2)/(2*z))
g = np.abs(FFT.ifftshift(FFT.irfft2(J2, s=[N,N], workers=-1, norm='forward')))

plt.figure(figsize=(16, 9))

levels = np.linspace(J2.min(), J2.max(), 16)
plt.subplot(121)
plt.contourf(u, v, np.real(J2), levels)
plt.colorbar(); plt.title('Фурье образ')
plt.xlim(-5,5); plt.xlabel('u, [1/см]')
plt.ylim(-5,5); plt.ylabel('v, [1/см]')
plt.subplot(122)
levels = np.linspace(g.min(), g.max(), 16)
plt.contourf(x, y, g, levels)
plt.colorbar(); plt.title('Результат свёртки')
plt.xlabel('x, [см]')
plt.ylabel('y, [см]')
plt.show()