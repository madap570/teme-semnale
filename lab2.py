#lab2
#ex1
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


amplitudine = 1.0
frecventa = 1
faza = np.pi / 4

timp = np.linspace(0, 2, 1000)

semnal_sinus = amplitudine * np.sin(2 * np.pi * frecventa * timp + faza)

semnal_cosinus = amplitudine * np.cos(2 * np.pi * frecventa * timp + faza)

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(timp, semnal_sinus, label='Sinus')
plt.title('Semnal Sinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(timp, semnal_cosinus, label='Cosinus', color='r')
plt.title('Semnal Cosinusoidal')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')
plt.legend()

plt.tight_layout()
plt.show()

#ex 4
amplitudine_sinus = 1.0
frecventa_sinus = 5.0
amplitudine_sawtooth = 0.5
frecventa_sawtooth = 2.0
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

