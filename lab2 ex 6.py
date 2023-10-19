import numpy as np
import matplotlib.pyplot as plt

fs = 200

durata = 1.0

timp = np.linspace(0, durata, int(fs * durata), endpoint=False)

frecventa_a = fs / 2
frecventa_b = fs / 4
frecventa_c = 0

semnal_a = np.sin(2 * np.pi * frecventa_a * timp)
semnal_b = np.sin(2 * np.pi * frecventa_b * timp)
semnal_c = np.sin(2 * np.pi * frecventa_c * timp)

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(timp, semnal_a)
plt.title('Semnal f = fs/2')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.subplot(3, 1, 2)
plt.plot(timp, semnal_b)
plt.title('Semnal f = fs/4')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.subplot(3, 1, 3)
plt.plot(timp, semnal_c)
plt.title('Semnal f = 0 Hz')
plt.xlabel('Timp (s)')
plt.ylabel('Amplitudine')

plt.tight_layout()
plt.show()
