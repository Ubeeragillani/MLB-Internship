import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\mlb internship\day3\flower.jpg")
if image is None:
    print("Image not found")
    exit()
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
height = lab.shape[0]
width = lab.shape[1]
L = np.zeros((height, width), dtype=np.uint8)
A = np.zeros((height, width), dtype=np.uint8)
B = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        L[i, j] = lab[i, j, 0]
        A[i, j] = lab[i, j, 1]
        B[i, j] = lab[i, j, 2]
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(L, cmap="gray")
plt.title("L Channel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(A, cmap="gray")
plt.title("A Channel")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(B, cmap="gray")
plt.title("B Channel")
plt.axis("off")

plt.tight_layout()
plt.show()