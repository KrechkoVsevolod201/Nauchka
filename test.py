import matplotlib.pyplot as plt
import numpy as np
import scipy as scr
from scipy import fft as FFT
from scipy import integrate as integr
import cmath
import warnings


def hank():
    N = 100
    a1 = 0.
    b1 = 0.00005
    foc = 100
    b = 1/(2*foc)
    c = 1.
    z = 50.
    hz = (500 - 50.)/500
    #print(hz)
    k = 10000.
    #wl = 0.0005

    list1 = []
    x = np.linspace(a1, b1, num=N)
    zed = np.linspace(50., 500, num=501)
    x4 = lambda r: np.exp(1j * k * r * ((-b) * r + c))
    #x4 = lambda r: np.sinc((-k*r*r*b + k*r*c))
    while(z < 500):
        x2 = lambda r: (1j*k/z)*np.exp(1j*k*z)*np.exp(1j * k * r * ((-b) * r + c))*np.exp(1j*k*r*r/(2*z))*r
        #x2 = lambda r: (1j * k / z) * np.exp(1j * k * z) * np.sinc((-k*r*r*b + k*r*c)) * np.exp(1j * k * r * r / (2 * z)) * r
        f, err = integr.quad(x2, 0., 1)
        list1.append(f)
        z = z + hz
    list2 = x4(x)
    print(len(list1))
    plt.subplot(131)
    plt.plot(x, np.angle(list2))
    plt.title("Фаза входного поля")
    plt.grid()
    plt.subplot(132)
    res = np.abs(list1)
    res2 = np.fft.fftshift(res)
    plt.plot(zed, res)
    plt.title("Амплитуда преобразования")
    plt.grid()
    plt.subplot(133)
    plt.plot(zed, np.angle(list1))
    plt.title("Фаза преобразования")
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hank()

