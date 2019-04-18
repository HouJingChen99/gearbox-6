#формирование выборки с использование стандартных возможностей языка Python
from numpy import linspace, arange, sin, pi
from matplotlib.pyplot import plot, show, grid
f = 1
N = 100
dt = 1/N
t_mod = 2
signal = dict()

for k in range(0, N * t_mod + 1):
    signal[k*dt] = sin(2 * pi * f * (k*dt))

print(signal)