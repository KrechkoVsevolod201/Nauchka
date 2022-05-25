import matplotlib.pyplot as plt
import numpy as np
import scipy as scr
from scipy import fft as FFT
from scipy import integrate as integr
import warnings
import decimal


def print_vector(name):
    n = 20
    x = np.zeros(n)
    print(x)
    i = 0
    while (i <= 10):
        x[i] = i
        i = i + 1
    print(x)


def ploter():
    # suppress warnings
    # warnings.filterwarnings('ignore')
    N = 1000
    a = 0.
    b = 1 / 200
    c = 10.
    alpha = 8 * np.pi
    z = 100.
    k = 10000.
    x = np.linspace(1, 1.5, num=N)
    # x = np.float128(x)
    r_axis = x * np.cos(alpha)
    y = np.exp(k * c * r_axis + (k * b * r_axis) ** 2)
    field = np.exp((((k * b * x) ** 2) + (k * c * x)))
    f = FFT.fht(np.abs(y), dln=1., mu=1.)
    f1 = FFT.fftshift(y)
    f2 = np.abs(f1)
    plt.plot(x, f1)
    plt.grid()
    plt.show()


def hank():
    N = 500
    a1 = 1.
    b1 = 5.
    b2 = a1
    h = (b1 - a1) / N
    a = 0.
    b = 1 / 200
    c = 10.
    alpha = 8 * np.pi
    z = 100.
    k = 10000.
    list1 = []
    x = np.linspace(a1, b1, num=N)
    x2 = lambda x: np.exp((((k * b * x) ** 2) + (k * c * x)))
    # y = np.exp(x)

    # ccd = np.asarray([decimal.Decimal(el) for el in x], dtype=object)
    # print(np.exp(((((-ccd) / 20) ** 2) + (1000 * (-ccd)))))
    # print(np.asarray(integr.quad(x2, 1, 10)), dtype=object)

    while (b2 < b1 - h):
         f, err = integr.quad(x2, b2, b2 + h)
         list1.append(f)
         b2 = b2 + h

    print(list1)
    plt.plot(x, list1)
    plt.grid()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_vector('PyCharm')
    hank()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
