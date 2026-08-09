import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("flower.jpg", 0)

# Gaussian noise add karo
noise = np.random.normal(0, 20, image.shape)
noisy = image + noise
noisy = np.clip(noisy, 0, 255).astype(np.uint8)

# Gaussian Blur
blur = cv2.GaussianBlur(noisy, (5, 5), 1)

# Manual Laplacian Kernel
laplacian_kernel = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
])

rows, cols = noisy.shape

laplacian = np.zeros((rows, cols), dtype=np.float32)
log = np.zeros((rows, cols), dtype=np.float32)

for i in range(1, rows - 1):
    for j in range(1, cols - 1):

        region1 = noisy[i-1:i+2, j-1:j+2]
        region2 = blur[i-1:i+2, j-1:j+2]

        laplacian[i, j] = np.sum(region1 * laplacian_kernel)
        log[i, j] = np.sum(region2 * laplacian_kernel)

laplacian = cv2.convertScaleAbs(laplacian)
log = cv2.convertScaleAbs(log)

plt.figure(figsize=(12,4))

plt.subplot(1,4,1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(noisy, cmap="gray")
plt.title("Noisy Image")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(log, cmap="gray")
plt.title("LoG")
plt.axis("off")

plt.tight_layout()
plt.show()