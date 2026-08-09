import  numpy as np
import matplotlib.image as mpimg

image = mpimg.imread("flower.jpg")

height = image.shape[0]
width = image.shape[1]
channel = image.shape[2]
datatype = image.dtype
total_pix = height * width

print("Height:", height)
print("Width:", width)
print("No of channels:", channel)
print("Data type:", datatype)
print("Total no of pixels:", total_pix)

