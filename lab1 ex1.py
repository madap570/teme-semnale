import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 0.03, 0.0005)

x= np.cos(520*np.pi*t + np.pi/3)
y= np.cos(280*np.pi*t - np.pi/3)
z= np.cos(120*np.pi*t + np.pi/3)

plt.figure()
plt.plot(t,x, label="axa x")
plt.plot(t,y, label="axa y")
plt.plot(t,z, label="axa z")
plt.xlabel('semnalul x')
plt.ylabel('semnalul y')
plt.legend()
plt.grid(True)
plt.show()

fig, axs = plt.subplots(3, 1, figsize=(8,6))

axs[0].plot(t, x, 'b')
axs[0].set_title('Semnal x')
axs[0].set_ylabel('Amplitudine')
axs[0].grid(True)

axs[1].plot(t, y, 'g')
axs[1].set_title('Semnal y')
axs[1].set_ylabel('Amplitudine')
axs[1].grid(True)

axs[2].plot(t, z, 'r')
axs[2].set_title('Semnal z')
axs[2].set_ylabel('Amplitudine')
axs[2].grid(True)

plt.show()

fs=200
Ts=2*np.pi/fs
t_s=np.arange(0, 0.03+0.0005, Ts)

xs= np.cos(520*np.pi*t_s + np.pi/3)
ys= np.cos(280*np.pi*t_s - np.pi/3)
zs= np.cos(120*np.pi*t_s + np.pi/3)

fig2, axs = plt.subplots(3, 1, figsize=(8,6))

axs[0].stem(t_s, xs, 'b')
axs[0].set_title('Semnal x[n]')
axs[0].set_ylabel('Amplitudine')
axs[0].grid(True)

axs[1].stem(t_s, ys, 'g')
axs[1].set_title('Semnal y[n]')
axs[1].set_ylabel('Amplitudine')
axs[1].grid(True)

axs[2].stem(t_s, zs, 'r')
axs[2].set_title('Semnal z[n]')
axs[2].set_ylabel('Amplitudine')
axs[2].grid(True)

plt.tight_layout()
plt.show()