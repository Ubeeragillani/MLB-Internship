import cv2
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

image = cv2.imread("flower.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def adjust_brightness(img, value):
    result = img.astype(np.int16) + value
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)

brighter = adjust_brightness(image, 50)
darker = adjust_brightness(image, -50)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(brighter)
plt.title("Brighter")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(darker)
plt.title("Darker")
plt.axis("off")

plt.show()

def brightness_slider(value):
    return adjust_brightness(image, value)

interface = gr.Interface(
    fn=brightness_slider,
    inputs=gr.Slider(-100, 100, value=0, step=1, label="Brightness"),
    outputs=gr.Image(label="Output Image"),
    title="Brightness Adjustment",
    description="Adjust image brightness using NumPy."
)

interface.launch()