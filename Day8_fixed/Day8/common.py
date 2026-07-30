import os
import cv2

# The nested-loop convolution/mean/median filters in these tasks are O(h*w*9)
# pure-Python operations. On the original 9216x6912 source image that's ~190M+
# iterations per single filter pass -- effectively hangs a Gradio callback.
# Capping the working resolution keeps every tab interactive (sub-second to
# low-seconds response) while preserving the pedagogical point of each task.
DEMO_MAX_DIM = 320


def load_demo_image(filename="flower.jpg", max_dim=DEMO_MAX_DIM):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)

    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Could not load image at: {path}")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    h, w = img.shape[:2]
    scale = max_dim / max(h, w)
    if scale < 1:
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)

    return img


def cap_image_size(img, max_dim=DEMO_MAX_DIM):
    """
    Caps any incoming image (e.g. user uploads to gr.Image) to max_dim before
    it hits a pixel-loop filter. Without this, an uploaded 4K/8K image runs the
    O(h*w*9) convolution loop for minutes and blocks the single Gradio worker
    for every other user -- an unauthenticated resource-exhaustion path on a
    public link. This is a hard cap, not a suggestion: silently downsizes
    rather than erroring, since the user just wants to see the filter work.
    """
    if img is None:
        return img
    h, w = img.shape[:2]
    scale = max_dim / max(h, w)
    if scale < 1:
        img = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
    return img
