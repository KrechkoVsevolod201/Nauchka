import matplotlib.pyplot as plt
import numpy as np
import scipy as scr
from scipy import fft as FFT
from scipy import integrate as integr
import cmath
import warnings


def hank():
    N = 100
    a1 = -0.00005
    b1 = 0.00005
    b2 = a1
    h = (b1 - a1)/N
    a = 0.
    foc = 300
    b = 1/(2*foc)
    c = 5.
    alpha = 2*np.pi
    z = 100
    hz = (500 - 100)/20
    k = 10000.
    wl = 0.0005

    list1 = []
    x = np.linspace(a1, b1, num=N)
    zed = np.linspace(100, 500, num=20)
    rad = 5.
    r_axis = x*np.cos(alpha)
    x4 = lambda r: np.exp(1j*(((-2*np.pi/wl * b * r*np.cos(alpha)) ** 2) + (2*np.pi/wl * c * r*np.cos(alpha))))
    while(z < 500):
        x2 = lambda r: (1j*k/z)*np.exp(1j*k*z)*np.exp(1j*((k*a*r)**3+(k*b*r)**2 + k*c*r))*np.exp(1j*k*(r)**2/(2*z))*r
        f, err = integr.quad(x2, 0, np.inf)
        list1.append(f)
        z = z + hz
    list2 = x4(x)
    print(len(list1))
    plt.subplot(131)
    plt.plot(x, (list2))
    plt.grid()
    plt.subplot(132)
    res = np.abs(list1)
    plt.plot(zed, res)
    plt.grid()
    plt.subplot(133)
    plt.plot(zed, list1)
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hank()

