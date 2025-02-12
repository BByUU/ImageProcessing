import cv2
import numpy as np

def Q10_Median_Filter(img, k_size=3):
    """使用中值濾波去除雜訊"""
    if len(img.shape) == 3:
        out = cv2.medianBlur(img, k_size)
    else:
        out = cv2.medianBlur(img[:, :, np.newaxis], k_size)[:, :, 0]

    return out
