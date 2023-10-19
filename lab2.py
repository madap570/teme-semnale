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


