import cv2
import numpy as np

def Q9_Gaussian_Filter(img, k_size=3, sigma=1.3):
    """使用高斯濾波器對圖像進行平滑處理"""
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # 生成高斯核
    K1D = cv2.getGaussianKernel(k_size, sigma)
    K2D = np.outer(K1D, K1D)  # 計算 2D 高斯核

    # 使用 cv2.filter2D 進行高斯模糊
    out = np.zeros_like(img, dtype=np.float32)
    for c in range(C):
        out[..., c] = cv2.filter2D(img[..., c].astype(np.float32), -1, K2D)

    return np.clip(out, 0, 255).astype(np.uint8)
