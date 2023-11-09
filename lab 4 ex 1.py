import numpy as np
import matplotlib.pyplot as plt
import time

def transformata_fourier(vector):
    N = len(vector)
    rezultat = np.zeros(N, dtype=np.complex128)

    for k in range(N):
        rezultat[k] = np.sum(vector * np.exp(-2j * np.pi * k * np.arange(N) / N))

    return rezultat

dimensiuni_vectori = [128, 256, 512, 1024, 2048, 4096, 8192]

timp_executie_propriu = []
timp_executie_numpy = []

for dimensiune in dimensiuni_vectori:
    vector = np.random.rand(dimensiune)

    start_time = time.time()
    transformata_fourier(vector)
    timp_executie_propriu.append(time.time() - start_time)

    start_time = time.time()
    np.fft.fft(vector)
    timp_executie_numpy.append(time.time() - start_time)

plt.plot(dimensiuni_vectori, timp_executie_propriu, label='Implementare Proprie')
plt.plot(dimensiuni_vectori, timp_executie_numpy, label='NumPy FFT')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Dimensiunea Vectorului')
plt.ylabel('Timp de Execuție (secunde)')
plt.legend()
plt.show()
