import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from common import load_demo_image

image = load_demo_image()

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


if __name__ == "__main__":
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


def noise_tab():

    gr.Markdown("## Noise Generation")

    noise = gr.Dropdown(
        choices=[
            "Salt",
            "Pepper",
            "Salt & Pepper",
            "Gaussian"
        ],
        label="Select Noise Type"
    )

    output = gr.Image(label="Noisy Image")

    button = gr.Button("Add Noise")

    button.click(
        fn=add_noise,
        inputs=noise,
        outputs=output
    )