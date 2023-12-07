from scipy import fftpack, misc
import numpy as np
import matplotlib.pyplot as plt

X = misc.face(gray=True)

Y = np.fft.fft2(X)
freq_db = 20 * np.log10(np.abs(Y))

freq_cutoff = 120

Y_cutoff = Y.copy()
Y_cutoff[freq_db > freq_cutoff] = 0

X_cutoff = np.fft.ifft2(Y_cutoff)
X_cutoff = np.real(X_cutoff)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.title('Spectrul de frecventa')
plt.imshow(freq_db, cmap='viridis')
plt.colorbar()

plt.subplot(1, 2, 2)
plt.title('Imaginea comprimata')
plt.imshow(X_cutoff, cmap='gray')

plt.show()
