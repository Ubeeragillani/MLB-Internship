import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os

image_path = os.path.join(os.path.dirname(__file__), "flower.jpg")
image = mpimg.imread(image_path)
height = image.shape[0]
width = image.shape[1]

red = np.zeros((height, width), dtype=np.uint8)
green = np.zeros((height, width), dtype=np.uint8)
blue = np.zeros((height, width), dtype=np.uint8)
for i in range(height):
    for j in range(width):
        red[i][j] = image[i][j][0]
        green[i][j] = image[i][j][1]

    
        blue[i][j] = image[i][j][2]

plt.imsave("red_channel.jpg", red, cmap="Reds")
plt.imsave("green_channel.jpg", green, cmap="Greens")
plt.imsave("blue_channel.jpg", blue, cmap="Blues")

print("Red channel saved")
print("Green channel saved")
print("Blue channel saved")