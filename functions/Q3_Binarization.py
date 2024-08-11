import cv2
import numpy as np

def Q3_Binarization(img):
    # # Read image
    # img = img.astype(np.float32)
    # b = img[:, :, 0].copy()
    # g = img[:, :, 1].copy()
    # r = img[:, :, 2].copy()

    # # Grayscale
    # out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # out = out.astype(np.uint8)

    # # Binarization
    # th = 128 # 使用255/2=128作为阈值进行二值化
    # out[out < th] = 0
    # out[out >= th] = 255
    # return out

    # 使用 OpenCV 將圖像轉換成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 使用 OpenCV 進行二值化
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    return binary
