# Importing library
import qrcode
import numpy as np
# Data to encode
def trapesium(f, a, b, n):
    h = float(b - a) / n
    s = 0.0
    s += f(a)/2.0
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    return s * h
f = lambda x: (3*x**2)*(x**3+2)**2

print(trapesium(f, 0, 2, 4))
