from PIL import Image
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
image_path = os.path.join(os.path.dirname(__file__), "flower.jpg")

img = Image.open(image_path)
image = np.array(img)

total = 0
count = 0
minimum = 255
maximum = 0

for row in image:
    for pixel in row:
        for value in pixel:
            total +=int(value)
            count += 1
            if value < minimum:
                minimum = value
            if value > maximum:
                maximum = value

mean = total / count

print("mean pixel intensity", mean)
print("minimum pixel value", minimum)
print("maximum pixel value", maximum)





