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

#ex 2

def exponential_average(series, alpha):
    result = [series[0]]
    for t in range(1, len(series)):
        result.append(alpha * series[t] + (1 - alpha) * result[t-1])
    return result

alpha = 0.2

rezultat = exponential_average(time_series, alpha)

plt.figure(figsize=(12, 6))
plt.plot(time, time_series, label='Seria de timp originala')
plt.plot(time, rezultat, label=f'Mediere exponentiala')
plt.legend()
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.show()

#ex 3

mc = 0
q = 5

epsilon = np.random.randn(N)

ma_series = np.full_like(time_series, mc)

for t in range(q, N):
    ma_series[t] = mc + np.dot(np.flipud(epsilon[t-q:t]), np.arange(1, q+1))

plt.figure(figsize=(12, 6))
plt.plot(time, time_series, label='Seria de timp originala', alpha=0.7)
plt.plot(time, ma_series, label=f'Model MA')
plt.legend()
plt.xlabel('Timp')
plt.ylabel('Valoare')
plt.show()