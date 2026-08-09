import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

from common import load_demo_image

image = load_demo_image()

def adjust_contrast(img, alpha, beta):
    result = alpha * img + beta
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)


if __name__ == "__main__":
    low_contrast = adjust_contrast(image, 0.5, 0)
    normal_contrast = adjust_contrast(image, 1, 0)
    high_contrast = adjust_contrast(image, 2, 0)

    plt.figure(figsize=(12,4))

    plt.subplot(1,3,1)
    plt.imshow(low_contrast)
    plt.title("Low Contrast")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(normal_contrast)
    plt.title("Normal")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(high_contrast)
    plt.title("High Contrast")
    plt.axis("off")

    plt.show()

def contrast_slider(alpha, beta):
    return adjust_contrast(image, alpha, beta)


def contrast_tab():

    gr.Markdown("## Contrast Adjustment")

    alpha = gr.Slider(
        0.1,
        3.0,
        value=1,
        step=0.1,
        label="Alpha (Contrast)"
    )

    beta = gr.Slider(
        -100,
        100,
        value=0,
        step=1,
        label="Beta (Brightness)"
    )

    output = gr.Image(label="Contrast Adjusted Image")

    button = gr.Button("Apply Contrast")

    button.click(
        fn=contrast_slider,
        inputs=[alpha, beta],
        outputs=output
    )