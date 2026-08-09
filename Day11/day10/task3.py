import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg", 0)

laplacian_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

rows, cols = image.shape

laplacian = np.zeros((rows, cols), dtype=np.float32)
gx = np.zeros((rows, cols), dtype=np.float32)
gy = np.zeros((rows, cols), dtype=np.float32)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = image[i-1:i+2, j-1:j+2]

        laplacian[i, j] = np.sum(region * laplacian_kernel)
        gx[i, j] = np.sum(region * sobel_x)
        gy[i, j] = np.sum(region * sobel_y)

sobel = np.sqrt(gx**2 + gy**2)

laplacian = cv2.convertScaleAbs(laplacian)

sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
sobel = sobel.astype(np.uint8)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(sobel, cmap="gray")
plt.title("Sobel")
plt.axis("off")

plt.tight_layout()
plt.show()