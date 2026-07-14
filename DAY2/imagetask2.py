import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
image_path = os.path.join(os.path.dirname(__file__), "flower.jpg")

image = mpimg.imread(image_path)

image = image.copy()

image[600, 200] = [255, 0,0]
image[200, 300] = [255, 0, 0]    
image[400, 444] = [255, 0, 0]     
image[300, 333] = [0, 0, 0]      
image[500, 500] = [0, 0, 0]     
output_path = os.path.join(os.path.dirname(__file__), "modified_flower.jpg")
plt.imsave(output_path, image)

print("Image modified and saved successfully!")