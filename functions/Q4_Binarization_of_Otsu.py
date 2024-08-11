import cv2
import numpy as np

def Q4_Binarization_of_Otsu(img):
    # Grayscale
    out = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # out = 0.2126 * img[..., 2] + 0.7152 * img[..., 1] + 0.0722 * img[..., 0]
    # out = out.astype(np.uint8)

    # Use OpenCV's Otsu's binarization
    _, out = cv2.threshold(out, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return out
