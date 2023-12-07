import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
N = 1000
time = np.arange(N)
a_trend, b_trend, c_trend = 0.0001, 0.1, 10

trend = a_trend * time**2 + b_trend * time + c_trend

freq1, freq2 = 0.01, 0.05

season = np.sin(2 * np.pi * freq1 * time) + np.sin(2 * np.pi * freq2 * time)

noise = 0.5 * np.random.randn(N)

time_series = trend + season + noise

plt.figure(figsize=(12, 6))

plt.subplot(4, 1, 1)
plt.plot(time, trend, label='Trend')
plt.legend()

plt.subplot(4, 1, 2)
plt.plot(time, season, label='Sezon')
plt.legend()

plt.subplot(4, 1, 3)
plt.plot(time, noise, label='Variabilitate mica (Zgomot)')
plt.legend()

plt.subplot(4, 1, 4)
plt.plot(time, time_series, label='Seria de timp finala')
plt.legend()

plt.tight_layout()
plt.show()

#ex2

autocorr = np.correlate(time_series, time_series, mode='full') / np.sum(time_series**2)

plt.figure(figsize=(12, 6))
plt.plot(autocorr)
plt.title('Vectorul de Autocorelatie')
plt.xlabel('Lag')
plt.ylabel('Autocorelatie')
plt.grid(True)
plt.show()