import cv2
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr
image = cv2.imread("flower.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def salt_noise(img, amount=0.05):
    noisy = img.copy()
    total_pixels = img.shape[0] * img.shape[1]
    number = int(total_pixels * amount)
    for _ in range(number):
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        noisy[x, y] = 255
    return noisy
def pepper_noise(img, amount=0.05):
    noisy = img.copy()
    total_pixels = img.shape[0] * img.shape[1]
    number = int(total_pixels * amount)
    for _ in range(number):
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        noisy[x, y] = 0
    return noisy
def salt_pepper_noise(img, amount=0.05):
    noisy = img.copy()
    total_pixels = img.shape[0] * img.shape[1]
    number = int(total_pixels * amount)
    for _ in range(number):
        x = np.random.randint(0, img.shape[0])
        y = np.random.randint(0, img.shape[1])
        if np.random.random() < 0.5:
            noisy[x, y] = 255
        else:
            noisy[x, y] = 0

    return noisy
def gaussian_noise(img, mean=0, sigma=25):
    noise = np.random.normal(mean, sigma, img.shape)

    noisy = img.astype(np.float32) + noise

    noisy = np.clip(noisy, 0, 255)

    return noisy.astype(np.uint8)
salt = salt_noise(image)
pepper = pepper_noise(image)
salt_pepper = salt_pepper_noise(image)
gaussian = gaussian_noise(image)
plt.figure(figsize=(12,8))
plt.subplot(2,3,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")
plt.subplot(2,3,2)
plt.imshow(salt)
plt.title("Salt Noise")
plt.axis("off")
plt.subplot(2,3,3)
plt.imshow(pepper)
plt.title("Pepper Noise")
plt.axis("off")
plt.subplot(2,3,4)
plt.imshow(salt_pepper)
plt.title("Salt & Pepper")
plt.axis("off")
plt.subplot(2,3,5)
plt.imshow(gaussian)
plt.title("Gaussian Noise")
plt.axis("off")
plt.show()
def add_noise(noise_type):

    if noise_type == "Salt":
        return salt_noise(image)
    elif noise_type == "Pepper":
        return pepper_noise(image)
    elif noise_type == "Salt & Pepper":
        return salt_pepper_noise(image)
    elif noise_type == "Gaussian":
        return gaussian_noise(image)
demo = gr.Interface(
    fn=add_noise,
    inputs=gr.Dropdown(
        choices=[
            "Salt",
            "Pepper",
            "Salt & Pepper",
            "Gaussian"
        ],
        label="Select Noise Type"
    ),
    outputs=gr.Image(label="Noisy Image"),
    title="Noise Generation",
    description="Manual Noise Generation using NumPy"
)
demo.launch()