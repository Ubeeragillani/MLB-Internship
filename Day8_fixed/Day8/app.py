"""
Day 8 - Image Processing Lab (Gradio app)

Combines all 7 task modules into a single tabbed interface.

Architecture notes (read before you deploy this anywhere public):
- matplotlib backend is forced to Agg BEFORE any task module is imported.
  Every task file calls plt.show() in its __main__ demo block; without Agg,
  that call tries to open a GUI window and hangs/crashes on any headless
  server (your own machine has a display so you wouldn't have seen this,
  but any VPS, container, or CI box will).
- Each task module's demo plotting code only runs when that file is executed
  directly (`if __name__ == "__main__":`), not on import. Importing 7 modules
  that each pop a matplotlib figure would be pointless GUI-blocking overhead
  bundled into every app startup.
- The working image is capped to 320px (see common.py). The nested Python
  loops in tasks 3/5/6/7 are O(h*w*9) per filter pass -- on the original
  9216x6912 source that's 190M+ iterations per click. Capping resolution is
  what makes this interactive instead of frozen.
- Uploads to task3 (sharpen) and task6 (deblur) are size-capped in the
  callback itself (cap_image_size), since those two tabs accept arbitrary
  user images, not just the bundled demo image.
"""

import matplotlib
matplotlib.use("Agg")

import gradio as gr

import task1
import task2
import task3
import task4
import task5
import task6
import task7


with gr.Blocks(title="Day 8 - Image Processing Lab") as demo:
    gr.Markdown("# Image Processing Lab — Day 8")
    gr.Markdown(
        "Demo image is capped to 320px on the long edge so the manual "
        "pixel-loop filters (sharpen, denoise, deblur) respond in under a "
        "couple seconds instead of hanging on the full-resolution source."
    )

    with gr.Tab("1. Brightness"):
        task1.brightness_tab()

    with gr.Tab("2. Contrast"):
        task2.contrast_tab()

    with gr.Tab("3. Sharpening"):
        task3.sharpening_tab()

    with gr.Tab("4. Noise Generation"):
        task4.noise_tab()

    with gr.Tab("5. Noise Reduction"):
        task5.denoise_tab()

    with gr.Tab("6. Deblurring"):
        task6.deblur_tab()

    with gr.Tab("7. Enhancement Comparison"):
        task7.enhancement_tab()


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
