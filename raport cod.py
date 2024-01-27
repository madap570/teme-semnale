import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(image_path, grayscale=True):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE if grayscale else cv2.IMREAD_COLOR)

def apply_sobel_filter(image):
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
    sobel = np.sqrt(sobelx**2 + sobely**2)
    return np.uint8(sobel)

def apply_canny(image):
    return cv2.Canny(image, 100, 200)

def calculate_error(detected_edges, ground_truth):
    mse = np.mean((detected_edges - ground_truth) ** 2)
    mae = np.mean(np.abs(detected_edges - ground_truth))
    return mse, mae

def calculate_accuracy(mse):
    max_mse = 255**2
    accuracy = max(0, (1 - mse / max_mse)) * 100
    return accuracy

original_image = load_image('puffins.jpg')
ground_truth = load_image('puffin_contur.jpg')

sobel_edges = apply_sobel_filter(original_image)
canny_edges = apply_canny(original_image)

sobel_mse, sobel_mae = calculate_error(sobel_edges, ground_truth)
canny_mse, canny_mae = calculate_error(canny_edges, ground_truth)
sobel_accuracy = calculate_accuracy(sobel_mse)
canny_accuracy = calculate_accuracy(canny_mse)

print(f"Sobel - Acuratețe: {sobel_accuracy}% (MSE: {sobel_mse}, MAE: {sobel_mae})")
print(f"Canny - Acuratețe: {canny_accuracy}% (MSE: {canny_mse}, MAE: {canny_mae})")

plt.figure(figsize=(20, 5))

plt.subplot(1, 2, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Imagine Originală')

plt.subplot(1, 2, 2)
plt.imshow(ground_truth, cmap='gray')
plt.title('Contur Manual')

plt.figure(figsize=(20, 5))

plt.subplot(1, 2, 1)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Filtrul Sobel')

plt.subplot(1, 2, 2)
plt.imshow(canny_edges, cmap='gray')
plt.title('Detectarea Marginilor Canny')



plt.show()
