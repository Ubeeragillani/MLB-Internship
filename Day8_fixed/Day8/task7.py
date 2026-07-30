import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from common import load_demo_image

image = load_demo_image()


def brightness(img, value=50):
    result = img.astype(np.int16) + value
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)


def contrast(img, alpha=1.5, beta=0):
    result = alpha * img + beta
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)


def convolution(img, kernel):

    h, w, c = img.shape

    padded = np.pad(
        img,
        ((1,1),(1,1),(0,0)),
        mode="edge"
    )

    output = np.zeros_like(img)

    for channel in range(c):
        for i in range(h):
            for j in range(w):

                region = padded[i:i+3, j:j+3, channel]

                output[i,j,channel] = np.sum(region * kernel)

    output = np.clip(output,0,255)

    return output.astype(np.uint8)


sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])


def sharpen(img):
    return convolution(img, sharpen_kernel)


def mean_filter(img):

    size = 3
    pad = 1

    padded = np.pad(
        img,
        ((pad,pad),(pad,pad),(0,0)),
        mode="edge"
    )

    output = np.zeros_like(img)

    for c in range(img.shape[2]):
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):

                region = padded[i:i+size, j:j+size, c]

                output[i,j,c] = np.mean(region)

    return output.astype(np.uint8)


low_quality = brightness(image, -70)


if __name__ == "__main__":
    bright_image = brightness(low_quality, 70)
    contrast_image = contrast(low_quality, 1.8, 0)
    sharp_image = sharpen(low_quality)
    denoise_image = mean_filter(low_quality)

    plt.figure(figsize=(12,8))

    plt.subplot(2,3,1)
    plt.imshow(low_quality)
    plt.title("Low Quality")
    plt.axis("off")

    plt.subplot(2,3,2)
    plt.imshow(bright_image)
    plt.title("Brightness")
    plt.axis("off")

    plt.subplot(2,3,3)
    plt.imshow(contrast_image)
    plt.title("Contrast")
    plt.axis("off")

    plt.subplot(2,3,4)
    plt.imshow(sharp_image)
    plt.title("Sharpening")
    plt.axis("off")

    plt.subplot(2,3,5)
    plt.imshow(denoise_image)
    plt.title("Denoising")
    plt.axis("off")

    plt.show()


def enhancement(option):
    # Computed on demand, not at import: sharpen()/mean_filter() are
    # pixel-loop functions, no reason to pay that cost for every option
    # on every app startup when the user only ever picks one at a time.
    if option == "Brightness":
        return brightness(low_quality, 70)

    elif option == "Contrast":
        return contrast(low_quality, 1.8, 0)

    elif option == "Sharpening":
        return sharpen(low_quality)

    elif option == "Denoising":
        return mean_filter(low_quality)


def enhancement_tab():

    gr.Markdown("## Image Enhancement Comparison")

    option = gr.Dropdown(
        choices=[
            "Brightness",
            "Contrast",
            "Sharpening",
            "Denoising"
        ],
        label="Select Enhancement"
    )

    output = gr.Image(label="Enhanced Image")

    button = gr.Button("Apply Enhancement")

    button.click(
        fn=enhancement,
        inputs=option,
        outputs=output
    )