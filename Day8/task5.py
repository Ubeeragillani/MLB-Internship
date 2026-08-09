import cv2
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr


image = cv2.imread("flower.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def add_salt_pepper_noise(img, amount=0.05):
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


noisy_image = add_salt_pepper_noise(image)


def mean_filter(img, size=3):

    pad = size // 2
    padded = np.pad(img, ((pad,pad),(pad,pad),(0,0)), mode="edge")

    output = np.zeros_like(img)

    for c in range(img.shape[2]):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):

                region = padded[i:i+size, j:j+size, c]
                output[i,j,c] = np.mean(region)

    return output.astype(np.uint8)



def median_filter(img, size=3):

    pad = size // 2
    padded = np.pad(img, ((pad,pad),(pad,pad),(0,0)), mode="edge")

    output = np.zeros_like(img)

    for c in range(img.shape[2]):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):

                region = padded[i:i+size, j:j+size, c]
                output[i,j,c] = np.median(region)

    return output.astype(np.uint8)



def gaussian_filter(img):

    kernel = np.array([
        [1,2,1],
        [2,4,2],
        [1,2,1]
    ])

    kernel = kernel / np.sum(kernel)

    pad_img = np.pad(img, ((1,1),(1,1),(0,0)), mode="edge")

    output = np.zeros_like(img)


    for c in range(img.shape[2]):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):

                region = pad_img[i:i+3, j:j+3, c]

                output[i,j,c] = np.sum(region * kernel)


    return output.astype(np.uint8)



mean_result = mean_filter(noisy_image)
median_result = median_filter(noisy_image)
gaussian_result = gaussian_filter(noisy_image)



plt.figure(figsize=(12,8))


plt.subplot(2,3,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")


plt.subplot(2,3,2)
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis("off")


plt.subplot(2,3,3)
plt.imshow(mean_result)
plt.title("Mean Filter")
plt.axis("off")


plt.subplot(2,3,4)
plt.imshow(median_result)
plt.title("Median Filter")
plt.axis("off")


plt.subplot(2,3,5)
plt.imshow(gaussian_result)
plt.title("Gaussian Filter")
plt.axis("off")


plt.show()



def remove_noise(filter_type):

    if filter_type == "Mean":
        return mean_filter(noisy_image)

    elif filter_type == "Median":
        return median_filter(noisy_image)

    elif filter_type == "Gaussian":
        return gaussian_filter(noisy_image)



demo = gr.Interface(
    fn=remove_noise,
    inputs=gr.Dropdown(
        choices=[
            "Mean",
            "Median",
            "Gaussian"
        ],
        label="Select Filter"
    ),
    outputs=gr.Image(label="Denoised Image"),
    title="Noise Reduction",
    description="Manual Mean, Median and Gaussian Filtering using NumPy"
)


demo.launch()