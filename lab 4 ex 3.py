#lab 4 ex 3
import numpy as np
import matplotlib.pyplot as plt

frecventa_sursa = 10
frecventa_esantionare = 24
durata = 1
amplitudine = 1

t = np.linspace(0, durata, 1000)
semnal_sursa = amplitudine * np.sin(2 * np.pi * frecventa_sursa * t)

t_esantionat = np.arange(0, durata, 1 / frecventa_esantionare)
semnal_esantionat = amplitudine * np.sin(2 * np.pi * frecventa_sursa * t_esantionat)

frecventa1 = 8
semnal1 = amplitudine * np.sin(2 * np.pi * frecventa1 * t_esantionat)

frecventa2 = 14
semnal2 = amplitudine * np.sin(2 * np.pi * frecventa2 * t_esantionat)

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(t, semnal_sursa)
plt.title("Semnalul sursa")

plt.subplot(2, 2, 2)
plt.plot(t_esantionat, semnal_esantionat)
plt.title("Semnal esantionat cu frecventa mai mare decat Nyquist")

plt.subplot(2, 2, 3)
plt.plot(t_esantionat, semnal1)
plt.title("Semnal cu frecventa diferita 1")

plt.subplot(2, 2, 4)
plt.plot(t_esantionat, semnal2)
plt.title("Semnal cu frecventa diferita 2")

plt.tight_layout()
plt.show()
