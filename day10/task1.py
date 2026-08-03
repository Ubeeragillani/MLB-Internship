import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg", 0)

gx_kernel = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
])

gy_kernel = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

rows, cols = image.shape

gx = np.zeros((rows, cols), dtype=np.float32)
gy = np.zeros((rows, cols), dtype=np.float32)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):
        region = image[i-1:i+2, j-1:j+2]

        gx[i, j] = np.sum(region * gx_kernel)
        gy[i, j] = np.sum(region * gy_kernel)

magnitude = np.sqrt(gx**2 + gy**2)
direction = np.arctan2(gy, gx)

gx_display = cv2.convertScaleAbs(gx)
gy_display = cv2.convertScaleAbs(gy)
magnitude_display = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
magnitude_display = magnitude_display.astype(np.uint8)

direction_display = cv2.normalize(direction, None, 0, 255, cv2.NORM_MINMAX)
direction_display = direction_display.astype(np.uint8)

plt.figure(figsize=(12, 8))

plt.subplot(2,3,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(2,3,2)
plt.imshow(gx_display, cmap="gray")
plt.title("Gradient X (Gx)")
plt.axis("off")

plt.subplot(2,3,3)
plt.imshow(gy_display, cmap="gray")
plt.title("Gradient Y (Gy)")
plt.axis("off")

plt.subplot(2,3,5)
plt.imshow(magnitude_display, cmap="gray")
plt.title("Gradient Magnitude")
plt.axis("off")

plt.subplot(2,3,6)
plt.imshow(direction_display, cmap="gray")
plt.title("Gradient Direction")
plt.axis("off")

plt.tight_layout()
plt.show()