import numpy as np
from scipy.fft import dctn, idctn
import matplotlib.pyplot as plt
from scipy import misc
import cv2
import time

#punctul 1

X = misc.ascent()

Q_jpeg = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                   [12, 12, 14, 19, 26, 28, 60, 55],
                   [14, 13, 16, 24, 40, 57, 69, 56],
                   [14, 17, 22, 29, 51, 87, 80, 62],
                   [18, 22, 37, 56, 68, 109, 103, 77],
                   [24, 35, 55, 64, 81, 104, 113, 92],
                   [49, 64, 78, 87, 103, 121, 120, 101],
                   [72, 92, 95, 98, 112, 100, 103, 99]])

Q_down = 10
block_size = 8

rows, cols = X.shape

plt.subplot(121).imshow(X, cmap=plt.cm.gray)
plt.title('Original')
X_jpeg = Q_down * np.round(X / Q_down)
plt.subplot(122).imshow(X_jpeg, cmap=plt.cm.gray)
plt.title('Down-sampled')
plt.show()

for row in range(0, rows, block_size):
    for col in range(0, cols, block_size):
        block = X[row:row + block_size, col:col + block_size]

        block_dct = dctn(block)

        block_quantized = np.round(block_dct / Q_jpeg)

        block_dequantized = block_quantized * Q_jpeg

        block_idct = idctn(block_dequantized)

        X_jpeg[row:row + block_size, col:col + block_size] = block_idct

plt.imshow(X_jpeg, cmap=plt.cm.gray)
plt.title('Compressed JPEG')
plt.show()


#punctul 2

def rgb_to_ycbcr(rgb_image):
    r = rgb_image[:, :, 0]
    g = rgb_image[:, :, 1]
    b = rgb_image[:, :, 2]

    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = -0.1687 * r - 0.3313 * g + 0.5 * b + 128
    cr = 0.5 * r - 0.4187 * g - 0.0813 * b + 128

    ycbcr_image = np.stack([y, cb, cr], axis=-1)
    return ycbcr_image

def ycbcr_to_rgb(ycbcr_image):
    y = ycbcr_image[:, :, 0]
    cb = ycbcr_image[:, :, 1] - 128
    cr = ycbcr_image[:, :, 2] - 128

    r = y + 1.402 * cr
    g = y - 0.344136 * cb - 0.714136 * cr
    b = y + 1.772 * cb

    rgb_image = np.stack([r, g, b], axis=-1)
    rgb_image = np.clip(rgb_image, 0, 255).astype(np.uint8)
    return rgb_image

face = misc.face()
plt.imshow(face)
plt.title('Original RGB Image')
plt.show()

ycbcr_face = rgb_to_ycbcr(face)

Q_down = 10
block_size = 8

for ch in range(3):
    for row in range(0, face.shape[0], block_size):
        for col in range(0, face.shape[1], block_size):

            block = ycbcr_face[row:row + block_size, col:col + block_size, ch]

            block_dct = dctn(block)

            block_quantized = np.round(block_dct / Q_down)

            block_dequantized = block_quantized * Q_down

            block_idct = idctn(block_dequantized)

            ycbcr_face[row:row + block_size, col:col + block_size, ch] = block_idct

compressed_face = ycbcr_to_rgb(ycbcr_face)

plt.imshow(compressed_face)
plt.title('Compressed JPEG Image')
plt.show()

#punctul 3

def rgb_to_ycbcr(rgb_image):
    r = rgb_image[:, :, 0]
    g = rgb_image[:, :, 1]
    b = rgb_image[:, :, 2]

    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = -0.1687 * r - 0.3313 * g + 0.5 * b + 128
    cr = 0.5 * r - 0.4187 * g - 0.0813 * b + 128

    ycbcr_image = np.stack([y, cb, cr], axis=-1)
    return ycbcr_image

def ycbcr_to_rgb(ycbcr_image):
    y = ycbcr_image[:, :, 0]
    cb = ycbcr_image[:, :, 1] - 128
    cr = ycbcr_image[:, :, 2] - 128

    r = y + 1.402 * cr
    g = y - 0.344136 * cb - 0.714136 * cr
    b = y + 1.772 * cb

    rgb_image = np.stack([r, g, b], axis=-1)
    rgb_image = np.clip(rgb_image, 0, 255).astype(np.uint8)
    return rgb_image

def calculate_mse(original, compressed):
    return np.mean((original - compressed) ** 2)

face = misc.face()
plt.imshow(face)
plt.title('Original RGB Image')
plt.show()

ycbcr_face = rgb_to_ycbcr(face)

Q_down = 10
block_size = 8
mse_threshold = 30

iteration = 1
while True:
    for ch in range(3):
        for row in range(0, face.shape[0], block_size):
            for col in range(0, face.shape[1], block_size):

                block = ycbcr_face[row:row + block_size, col:col + block_size, ch]

                block_dct = dctn(block)

                block_quantized = np.round(block_dct / Q_down)

                block_dequantized = block_quantized * Q_down

                block_idct = idctn(block_dequantized)

                ycbcr_face[row:row + block_size, col:col + block_size, ch] = block_idct

    compressed_face = ycbcr_to_rgb(ycbcr_face)

    current_mse = calculate_mse(face, compressed_face)

    print(f'Iteration {iteration}, MSE: {current_mse}')

    if current_mse < mse_threshold:
        break

    iteration += 1

plt.imshow(compressed_face)
plt.title('Compressed JPEG Image')
plt.show()

#punctul 4

def rgb_to_ycbcr(rgb_image):
    r = rgb_image[:, :, 0]
    g = rgb_image[:, :, 1]
    b = rgb_image[:, :, 2]

    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = -0.1687 * r - 0.3313 * g + 0.5 * b + 128
    cr = 0.5 * r - 0.4187 * g - 0.0813 * b + 128

    ycbcr_image = np.stack([y, cb, cr], axis=-1)
    return ycbcr_image

def ycbcr_to_rgb(ycbcr_image):
    y = ycbcr_image[:, :, 0]
    cb = ycbcr_image[:, :, 1] - 128
    cr = ycbcr_image[:, :, 2] - 128

    r = y + 1.402 * cr
    g = y - 0.344136 * cb - 0.714136 * cr
    b = y + 1.772 * cb

    rgb_image = np.stack([r, g, b], axis=-1)
    rgb_image = np.clip(rgb_image, 0, 255).astype(np.uint8)
    return rgb_image

def calculate_mse(original, compressed):
    return np.mean((original - compressed) ** 2)

def compress_each_frame(input_path, output_path, Q_down=10, block_size=16):
    cap = cv2.VideoCapture(input_path)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'wmv2')
    compressed_video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        ycbcr_frame = rgb_to_ycbcr(frame)

        for ch in range(3):
            for row in range(0, height, block_size):
                for col in range(0, width, block_size):
                    block = ycbcr_frame[row:row + block_size, col:col + block_size, ch]
                    block_dct = dctn(block, type=2)
                    block_quantized = np.round(block_dct / Q_down)
                    block_dequantized = block_quantized * Q_down
                    block_idct = idctn(block_dequantized, type=2)
                    ycbcr_frame[row:row + block_size, col:col + block_size, ch] = block_idct

        compressed_frame = ycbcr_to_rgb(ycbcr_frame)
        compressed_video_writer.write(compressed_frame)

    cap.release()
    compressed_video_writer.release()

    print(f'Comprimare video finalizată. Rezultatul salvat în "compressed_jellyfish.wmv"')

input_video_path = 'jellyfish.mp4'
output_video_path = 'compressed_jellyfish.wmv'

compress_each_frame(input_video_path, output_video_path)


