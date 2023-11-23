import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.random.rand(N)

plt.figure(figsize=(12, 3))
plt.subplot(1, 4, 1)
plt.plot(x)
plt.title('Vectorul original')

for i in range(3):
    x = x * x

    plt.subplot(1, 4, i + 2)
    plt.plot(x)
    plt.title(f'Iterație {i + 1}')

plt.tight_layout()
plt.show()
