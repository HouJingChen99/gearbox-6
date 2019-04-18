from matplotlib import pyplot as plt
import numpy as np

#rpm = 60 #скорость вращения ротора
f = 1 #оборотная частота
A = 0.1 #амплитуда колебания
k = 6 #число зубьев в зубчатой передаче
fz = k*f #частота зацепления
fm = 100 #частота вторичной модуляции
fn = 44000 #частота дискретизации
t_mod = 1 #время моделирования в секундах
t = np.linspace(0, t_mod, t_mod * fn) #формирование временного вектора
y1 = A*np.sin(2*np.pi*fz*t) #формирование НЧ модулирующего сигнала
plt.plot(t, y1)
plt.xlabel('время, $c$')
plt.ylabel('виброускорение, $мм/с^2$')
#plt.show()
y2 = np.cos(2*np.pi*fm*t) #формирование ВЧ модулилируемого сигнала
plt.plot(t, y2)
plt.xlabel('время, $c$')
plt.ylabel('виброускорение, $мм/с^2$')
plt.show()
y = y1 * y2 #формироавние промодулированного колебания
plt.plot(t, y)
plt.show()

y = list(y)
print(len(y))Т