import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
image_path = os.path.join(os.path.dirname(__file__), "flower.jpg")

image = mpimg.imread(image_path)
black=0
white=0
greater=0
totalpix=image.shape[0]*image.shape[1]


for row in image:
    for pixel in row:
        if pixel==0:
            black+=1


        if pixel==255:
             white+=1
            
        if pixel>200:
            greater+=1

print(" Total pixel",totalpix)
print(" Total black",black)
print(" Total whitel",white)
print(" Pixel >200 ",greater)




