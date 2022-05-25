import matplotlib.pyplot as plt
import numpy as np
import scipy as scr
from scipy import fft as FFT
from scipy import integrate as integr
import warnings


def print_vector(name):
    n = 20
    x = np.zeros(n)
    print(x)
    i = 0
    while (i <= 10):
        x[i] = i
        i = i+1
    print(x)

def ploter():
    # suppress warnings
    #warnings.filterwarnings('ignore')
    N = 1000
    a = 0.
    b = 1 / 200
    c = 10.
    alpha = 8*np.pi
    z = 100.
    k = 10.
    x = np.linspace(1, 1.5, num=N)
    #x = np.float128(x)
    r_axis = x*np.cos(alpha)
    y = np.exp(k*c*r_axis + (k*b*r_axis)**2)
    field = np.exp((((k * b * x) ** 2) + (k * c * x)))
    f = FFT.fht(np.abs(y), dln=1., mu=1.)
    f1 = FFT.fftshift(y)
    f2 = np.abs(f1)
    plt.plot(x, f1)
    plt.grid()
    plt.show()


def hank():
    N = 1000
    a1 = -0.00005
    b1 = 0.00005
    b2 = a1
    h = (b1 - a1)/N
    a = 0.
    b = 1 / 200
    c = 5.
    alpha = 2*np.pi
    z = 100.
    k = 10000.
    wl = 0.0005
    list1 = []
    x = np.linspace(a1, b1, num=N)
    r_axis = x*np.cos(alpha)
    x2 = lambda r: np.exp(1j*(((-2*np.pi/wl * b * r*np.cos(alpha)) ** 2) + (2*np.pi/wl * c * r*np.cos(alpha))))*(1j*2*np.pi/(wl*z))*np.exp(1j*2*np.pi/wl*z)*np.exp(1j*2*np.pi/wl*(r**2)/(2*z))*r
    x3 = lambda x: np.cos(x)
    while(b2 < b1):
        f, err = integr.quad(x2, b2, b2+h)
        list1.append(np.abs(f))
        b2 = b2 + h
    list2 = x2(x)
    print(len(list1))
    plt.plot(x, np.abs(list1))
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_vector('PyCharm')
    hank()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
