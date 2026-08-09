import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from common import load_demo_image, cap_image_size

image = load_demo_image()

def convolution(img, kernel):

    h, w, c = img.shape

    kh, kw = kernel.shape

    pad_h = kh // 2
    pad_w = kw // 2

    padded = np.pad(
        img,
        ((pad_h, pad_h), (pad_w, pad_w), (0, 0)),
        mode="edge"
    )

    output = np.zeros_like(img)

    for channel in range(c):
        for i in range(h):
            for j in range(w):

                region = padded[i:i+kh, j:j+kw, channel]

                output[i, j, channel] = np.sum(region * kernel)

    output = np.clip(output, 0, 255)

    return output.astype(np.uint8)


blur_kernel = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
])

blur_kernel = blur_kernel / 9


sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])


if __name__ == "__main__":
    blurred_image = convolution(image, blur_kernel)

    restored_image = convolution(
        blurred_image,
        sharpen_kernel
    )

    plt.figure(figsize=(12,4))

    plt.subplot(1,3,1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(blurred_image)
    plt.title("Blurred Image")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(restored_image)
    plt.title("Restored Image")
    plt.axis("off")

    plt.show()


def deblur(img):
    img = cap_image_size(img)
    blur = convolution(img, blur_kernel)

    restore = convolution(
        blur,
        sharpen_kernel
    )

    return restore


def deblur_tab():

    gr.Markdown("## Deblurring Basics")

    input_image = gr.Image(
        type="numpy",
        label="Upload Image"
    )

    output_image = gr.Image(
        label="Restored Image"
    )

    button = gr.Button("Restore Image")

    button.click(
        fn=deblur,
        inputs=input_image,
        outputs=output_image
    )