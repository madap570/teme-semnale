#lab 3 ex 1
import numpy as np
import matplotlib.pyplot as plt

N = 8

F = np.zeros((N, N), dtype=complex)
for i in range(N):
    for j in range(N):
        F[i][j] = np.exp(-2j * np.pi * i * j / N)

is_unitary = np.allclose(np.eye(N), np.conj(F).T @ F)
print("Matricea Fourier este unitară:", is_unitary)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(np.real(F), cmap='hot', interpolation='none', extent=[0, N, 0, N])
plt.title("Partea Reală")

plt.subplot(1, 2, 2)
plt.imshow(np.imag(F), cmap='hot', interpolation='none', extent=[0, N, 0, N])
plt.title("Partea Imaginară")

plt.show()
