import cv2
import numpy as np
import matplotlib.pyplot as plt
import gradio as gr

image = cv2.imread("flower.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
def brightness(img, value=50):
    result = img.astype(np.int16) + value
    result = np.clip(result,0,255)
    return result.astype(np.uint8)

def contrast(img, alpha=1.5, beta=0):

    result = alpha * img + beta

    result = np.clip(result,0,255)

    return result.astype(np.uint8)

def convolution(img, kernel):
    h,w,c = img.shape

    padded = np.pad(
        img,
        ((1,1),(1,1),(0,0)),
        mode="edge"
    )

    output = np.zeros_like(img)


    for channel in range(c):

        for i in range(h):

            for j in range(w):

                region = padded[i:i+3,j:j+3,channel]

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

                region = padded[i:i+size,j:j+size,c]

                output[i,j,c] = np.mean(region)


    return output.astype(np.uint8)

low_quality = brightness(image,-70)
bright_image = brightness(low_quality,70)

contrast_image = contrast(low_quality,1.8,0)

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

    if option == "Brightness":
        return bright_image

    elif option == "Contrast":
        return contrast_image

    elif option == "Sharpening":
        return sharp_image

    elif option == "Denoising":
        return denoise_image



demo = gr.Interface(
    fn=enhancement,
    inputs=gr.Dropdown(
        choices=[
            "Brightness",
            "Contrast",
            "Sharpening",
            "Denoising"
        ],
        label="Select Enhancement"
    ),
    outputs=gr.Image(label="Enhanced Image"),
    title="Image Enhancement Comparison",
    description="Brightness, Contrast, Sharpening and Denoising comparison"
)


demo.launch()