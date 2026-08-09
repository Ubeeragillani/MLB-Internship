import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from common import load_demo_image

image = load_demo_image()

def adjust_brightness(img, value):
    result = img.astype(np.int16) + value
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)


if __name__ == "__main__":
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


def brightness_tab():

    gr.Markdown("## Brightness Adjustment")

    slider = gr.Slider(
        -100,
        100,
        value=0,
        step=1,
        label="Brightness"
    )

    output = gr.Image(label="Output Image")

    slider.change(
        fn=brightness_slider,
        inputs=slider,
        outputs=output
    )