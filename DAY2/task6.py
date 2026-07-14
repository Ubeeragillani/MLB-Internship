import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
image_path = os.path.join(os.path.dirname(__file__), "flower.jpg")

image = mpimg.imread(image_path)

height = image.shape[0]
width = image.shape[1]

gray_image = np.zeros((height, width), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        r = int(image[y, x, 0])
        g = int(image[y, x, 1])
        b = int(image[y, x, 2])
        gray_value = int(0.2989 * r + 0.5870 * g + 0.1140 * b)
        gray_image[y, x] = gray_value

gray_path = os.path.join(os.path.dirname(__file__), "grayscale_flower.jpg")
plt.imsave(gray_path, gray_image, cmap="gray")

print("Grayscale image saved as grayscale_flower.jpg")
