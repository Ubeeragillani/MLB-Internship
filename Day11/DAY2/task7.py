import matplotlib.image as mpimg
import numpy as np
import os
image_path = os.path.join(os.path.dirname(__file__), "flower.jpg")

image = mpimg.imread(image_path)

height = image.shape[0]
width = image.shape[1]
channels = image.shape[2]
bit_depth = image.dtype.itemsize * 8

total_pixels = height * width * channels
memory_bytes = total_pixels * (bit_depth // 8)
memory_mb = memory_bytes / (1024 * 1024)

print("Height:", height)
print("Width:", width)
print("Channels:", channels)
print("Bit depth:", bit_depth, "bits")
print("Memory occupied:", memory_bytes, "bytes")
print("Memory occupied:", round(memory_mb, 2), "MB")
