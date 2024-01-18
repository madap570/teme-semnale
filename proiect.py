import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'butterfly.jpg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

contour_image = cv2.filter2D(image_rgb, -1, kernel)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Imagine Originală')

plt.subplot(1, 2, 2)
plt.imshow(contour_image, cmap='gray')
plt.title('Imagine cu Contururi')

plt.show()
