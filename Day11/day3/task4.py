import cv2
import matplotlib.pyplot as plt
image = cv2.imread(r"C:\mlb internship\day3\flower.jpg")
if image is None:
    print("Image not found")
    exit()
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_red = (0, 120, 70)
upper_red = (10, 255, 255)
mask = cv2.inRange(hsv, lower_red, upper_red)
result = cv2.bitwise_and(rgb, rgb, mask=mask)
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(result)
plt.title("Segmented Output")
plt.axis("off")

plt.tight_layout()
plt.show()