import numpy as np
from matplotlib import pyplot as plt
f1 = 1
f2 = 50
A = 1
N = 16000
dt = 1/N
t_mod = 1
t = np.arange(0, t_mod + dt, dt)
s1 = A * np.sin(2 * np.pi * f1 * t)
s2 = A * np.cos(2 * np.pi * f2 * t)
s = (s1 * s2)
plt.plot(t, s)
plt.show()
spectr = 2 * np.abs(np.fft.fft(s)) / N
n = s.size
freq = np.fft.fftfreq(n, dt)

print(len(s))
print(len(freq))
print(len(spectr))

plt.plot(freq, spectr)
plt.show()

print('Project done!')