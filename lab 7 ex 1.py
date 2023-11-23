from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

N = 200

# n1, n2 = np.indices((N, N))
#
# x1 = np.sin(2*np.pi*n1 + 3*np.pi*n2)
# plt.imshow(x1, cmap=plt.cm.gray)
# plt.show()
#
# y1 = np.fft.fft2(x1)
# plt.imshow(20*np.log10(np.abs(y1)))
# plt.colorbar()
# plt.show()

# x2 = np.sin(4*np.pi*n1) + np.cos(6*np.pi*n2)
# plt.imshow(x2, cmap=plt.cm.gray)
# plt.show()
#
# y2 = np.fft.fft2(x2)
# plt.imshow(20*np.log10(np.abs(y2)))
# plt.colorbar()
# plt.show()
# def functieY1(N):
#     Y = np.zeros((N, N), dtype=np.uint16)
#     Y[0, [5, N-5]] = 1
#     for m1 in range(1, N):
#         for m2 in range(N):
#             if m2 < 5 or m2 > N-5 or (m1 == 0 and (m2 == 5 or m2 == N-5)):
#                 Y[m1, m2] = 0
#             else:
#                 Y[m1, m2] = 1
#
#     return Y
#
# Y1 = functieY1(N)
# plt.imshow(Y1, cmap=plt.cm.gray)
# plt.show()
#
# y3 = np.fft.fft2(Y1)
# plt.imshow(20*np.log10(np.abs(y3)))
# plt.colorbar()
# plt.show()

def functieY2(N):
    Y = np.zeros((N, N), dtype=np.uint16)
    Y[5, 0] = Y[N - 5, 0] = 1
    for m1 in range(N):
        for m2 in range(N):
            if m1 not in [0, 5, N - 5] and m2 not in [0, 5, N - 5]:
                Y[m1, m2] = 0

    return Y

Y2 = functieY2(N)
plt.imshow(Y2, cmap=plt.cm.gray)
plt.show()

y4 = np.fft.fft2(Y2)
plt.imshow(20*np.log10(np.abs(y4)))
plt.colorbar()
plt.show()