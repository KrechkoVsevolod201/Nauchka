import matplotlib.pyplot as plt
import numpy as np
import scipy as scr
from scipy import fft as FFT
from scipy import integrate as integr
import cmath
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
    # warnings.filterwarnings('ignore')
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
    hz = (700 - 100)/100
    k = 10000.
    wl = 0.0005

    list1 = []
    x = np.linspace(a1, b1, num=N)
    zed = np.linspace(100, 1000, num=N)
    rad = 5.
    r_axis = x*np.cos(alpha)
    # x2 = lambda rad: np.exp(1j*(((-2*np.pi/wl * b * rad*np.cos(alpha)) ** 2) + (2*np.pi/wl * c * rad*np.cos(alpha))))*(1j*2*np.pi/(wl*z))*np.exp(1j*2*np.pi/wl*z)*np.exp(1j*2*np.pi/wl*(rad**2)/(2*z))*rad
    x3 = lambda x: np.cos(x)
    x4 = lambda r: np.exp(1j*(((-2*np.pi/wl * b * r*np.cos(alpha)) ** 2) + (2*np.pi/wl * c * r*np.cos(alpha))))
    while(z < 700):
        '''
        x2 = lambda rad: np.exp(
            1j * (((-2 * np.pi / wl * b * rad * np.cos(alpha)) ** 2) + (2 * np.pi / wl * c * rad * np.cos(alpha)))) * np.exp(
            1j * 2 * np.pi / wl * (rad ** 2) / (2 * z)) * rad * (
                                     1j * 2 * np.pi / (wl * z)) * np.exp(1j * 2 * np.pi / wl * z)
        '''
        x2 = lambda rad: np.sin(rad+z)/(rad + z)
        #while(b2 < b1):
        f, err = integr.quad(x2, 1, np.inf)
        list1.append(f)
            #b2 = b2 + h
        z = z + hz
    list2 = x4(x)
    print(len(list1))
    plt.subplot(121)
    plt.plot(x, np.abs(list2))
    plt.grid()
    plt.subplot(122)
    res = np.abs(list1)
    plt.plot(zed, res)
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_vector('PyCharm')
    hank()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
