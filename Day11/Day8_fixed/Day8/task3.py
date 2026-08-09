import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from common import load_demo_image, cap_image_size

image = load_demo_image()

def convolution(img, kernel):
    height, width, channels = img.shape

    padded = np.pad(img, ((1,1), (1,1), (0,0)), mode="edge")

    output = np.zeros_like(img)

    for c in range(channels):
        for i in range(height):
            for j in range(width):
                region = padded[i:i+3, j:j+3, c]
                output[i, j, c] = np.sum(region * kernel)

    output = np.clip(output, 0, 255)

    return output.astype(np.uint8)


sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

if __name__ == "__main__":
    sharpened = convolution(image, sharpen_kernel)

    plt.figure(figsize=(10,4))

    plt.subplot(1,2,1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1,2,2)
    plt.imshow(sharpened)
    plt.title("Sharpened Image")
    plt.axis("off")

    plt.show()


def sharpen_image(img):
    img = cap_image_size(img)
    return convolution(img, sharpen_kernel)


def sharpening_tab():

    gr.Markdown("## Image Sharpening")

    input_image = gr.Image(
        type="numpy",
        label="Upload Image"
    )

    output_image = gr.Image(
        label="Sharpened Image"
    )

    button = gr.Button("Sharpen Image")

    button.click(
        fn=sharpen_image,
        inputs=input_image,
        outputs=output_image
    )