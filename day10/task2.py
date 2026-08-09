import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg", 0)

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

gx = np.zeros((rows, cols), dtype=np.float32)
gy = np.zeros((rows, cols), dtype=np.float32)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = image[i-1:i+2, j-1:j+2]

        gx[i, j] = np.sum(region * sobel_x)
        gy[i, j] = np.sum(region * sobel_y)

edges = np.sqrt(gx**2 + gy**2)

gx = cv2.convertScaleAbs(gx)
gy = cv2.convertScaleAbs(gy)
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX)
edges = edges.astype(np.uint8)

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(gx, cmap="gray")
plt.title("Sobel X")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(gy, cmap="gray")
plt.title("Sobel Y")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(edges, cmap="gray")
plt.title("Final Edge")
plt.axis("off")

plt.tight_layout()
plt.show()