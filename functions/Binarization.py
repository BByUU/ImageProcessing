import cv2
import numpy as np

def Binarization(img):
    # Read image
    img = img.astype(np.float32)
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()

    # Grayscale
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    out = out.astype(np.uint8)

    # Binarization
    th = 128
    out[out < th] = 0
    out[out >= th] = 255
    return out

# # Save result
# cv2.imwrite("out.jpg", out)
# cv2.imshow("result", out)
# cv2.waitKey(0)
# cv2.destroyAllWindows()