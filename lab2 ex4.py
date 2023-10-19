#ex 4
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


amplitudine_sinus = 1.0
frecventa_sinus = 2
amplitudine_sawtooth = 0.5
frecventa_sawtooth = 0.5
n = np.arange(0, 1000)

semnal_sinus = amplitudine_sinus * np.sin(2 * np.pi * frecventa_sinus * n)

semnal_sawtooth = amplitudine_sawtooth * signal.sawtooth(2 * np.pi * frecventa_sawtooth * n)

suma_semnalelor = semnal_sinus + semnal_sawtooth

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(n, semnal_sinus)
plt.title('Semnal Sinusoidal')
plt.xlabel('Eșantionare')
plt.ylabel('Amplitudine')

plt.subplot(3, 1, 2)
plt.plot(n, semnal_sawtooth)
plt.title('Semnal de Tip Sawtooth')
plt.xlabel('Eșantionare')
plt.ylabel('Amplitudine')

plt.subplot(3, 1, 3)
plt.plot(n, suma_semnalelor)
plt.title('Suma Semnalelor')
plt.xlabel('Eșantionare')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()
