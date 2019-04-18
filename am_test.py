import numpy as np
from matplotlib import pyplot as plt
f1 = 2
f2 = 8
fd = 8000
t_mod = 0.5
t = np.linspace(0, t_mod, t_mod * fd)
A = 1
s1 = np.sin(2*np.pi*f1*t)
s2 = np.sin(2*np.pi*f2*t)
s = s1 + s2
y_sp = np.abs(np.fft.fft(s))
fd = np.linspace(0, fd, fd)
print(len(fd))
plt.plot(fd, y_sp)
plt.show()