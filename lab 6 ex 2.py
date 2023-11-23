import numpy as np
from numpy.fft import fft, ifft

def multiply_polynomials_direct(p_coeff, q_coeff):
    return np.convolve(p_coeff, q_coeff, mode='full')

def multiply_polynomials_fft(p_coeff, q_coeff):
    N = len(p_coeff) + len(q_coeff) - 2
    p_fft = fft(np.pad(p_coeff, (0, N), 'constant'))
    q_fft = fft(np.pad(q_coeff, (0, N), 'constant'))
    r_fft = ifft(p_fft * q_fft).real.round().astype(int)
    return r_fft

N = 5
p_coeff = np.random.randint(-10, 10, N+1)
q_coeff = np.random.randint(-10, 10, N+1)

r_direct = multiply_polynomials_direct(p_coeff, q_coeff)
r_fft = multiply_polynomials_fft(p_coeff, q_coeff)

print("Coeficienții polinomului p(x):", p_coeff)
print("Coeficienții polinomului q(x):", q_coeff)
print("Coeficienții polinomului r(x) (direct):", r_direct)
print("Coeficienții polinomului r(x) (FFT):", r_fft)
