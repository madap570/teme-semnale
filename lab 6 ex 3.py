import numpy as np
import matplotlib.pyplot as plt

def construct_and_plot_windowed_sine(Nw):
    f = 100
    A = 1
    phi = 0

    t = np.arange(0, 1, 1/1000)

    x = A * np.sin(2 * np.pi * f * t + phi)

    window_rectangular = np.ones(Nw)

    window_hanning = np.hanning(Nw)

    x_rectangular = x[:Nw] * window_rectangular
    x_hanning = x[:Nw] * window_hanning

    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.plot(t[:Nw], x[:Nw])
    plt.title('Sinusoida nelimitată')

    plt.subplot(3, 1, 2)
    plt.plot(t[:Nw], x_rectangular)
    plt.title('Sinusoida cu fereastră dreptunghiulară')

    plt.subplot(3, 1, 3)
    plt.plot(t[:Nw], x_hanning)
    plt.title('Sinusoida cu fereastră Hanning')

    plt.tight_layout()
    plt.show()

Nw = 200

construct_and_plot_windowed_sine(Nw)
