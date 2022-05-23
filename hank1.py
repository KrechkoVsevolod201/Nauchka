import numpy as np
import matplotlib.pyplot as plt

from Hankel_qDHT import Hankel_qDHT
a = 0.
b = 1/200
c = 10.
z = 100.
k = 10000.
N = 4096 # points
ht = Hankel_qDHT(N)
r_axis = ht.r   # the generated ratial axis, r is almost equally spaced,
                # corresponding to the positive-zeros of 0-order Bessel
                # function J_0(x)
# field before 0-order Hankel Transform:
field =  np.exp(1j*(((k*a*r_axis)**3)-((k*b*r_axis)**2)+(k*c*r_axis)))
# field after the transform, lives still on ht.r axis:
field_H0 = ht.transform(field) #

plt.plot(r_axis, np.abs(field), "b-")
plt.plot(r_axis, np.abs(field_H0), "r--")
plt.xlabel("r")
plt.ylabel("abs. field")
plt.show()