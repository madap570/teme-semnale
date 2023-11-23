import numpy as np
import matplotlib.pyplot as plt

frecventa_sursa = 10
frecventa_esantionare = 12
durata = 1
amplitudine = 1

t = np.linspace(0, durata, 1000)
semnal_sursa = amplitudine * np.sin(2 * np.pi * frecventa_sursa * t)

t_esantionat = np.arange(0, durata, 1 / frecventa_esantionare)
semnal_esantionat = amplitudine * np.sin(2 * np.pi * frecventa_sursa * t_esantionat)

frecventa1 = 5
semnal1 = amplitudine * np.sin(2 * np.pi * frecventa1 * t_esantionat)

frecventa2 = 7
semnal2 = amplitudine * np.sin(2 * np.pi * frecventa2 * t_esantionat)

puncte_aliniere = amplitudine * np.sin(2 * np.pi * frecventa_sursa * t_esantionat)

plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.plot(t, semnal_sursa)
plt.title("Semnalul sursa")

plt.subplot(2, 2, 2)
plt.plot(t, semnal_sursa)
plt.stem(t_esantionat, semnal_esantionat, 'bo-')
plt.title("Semnal esantionat cu frecventa sub-Nyquist")
plt.legend()

plt.subplot(2, 2, 3)
plt.plot(t, semnal_sursa)
plt.stem(t_esantionat, semnal1, 'go-')
plt.title("Semnal cu frecventa diferita 1")
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(t, semnal_sursa)
plt.stem(t_esantionat, semnal2, 'ro-')
plt.title("Semnal cu frecventa diferita 2")
plt.legend()

plt.tight_layout()
plt.show()
