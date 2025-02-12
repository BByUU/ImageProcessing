import cv2
import numpy as np
import matplotlib.pyplot as plt

# 讀取圖片
img = cv2.imread(r"U:\_GitHubProject\ImageProcessing\images\road.png")

# 將圖片轉換為 RGB 格式（OpenCV 預設讀取為 BGR）
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 分離 R, G, B 通道
r_channel, g_channel, b_channel = img_rgb[:, :, 0], img_rgb[:, :, 1], img_rgb[:, :, 2]

# 計算直方圖
hist_r = cv2.calcHist([r_channel], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g_channel], [0], None, [256], [0, 256])
hist_b = cv2.calcHist([b_channel], [0], None, [256], [0, 256])

# 設定亮度閾值（假設亮度高於 200 為反光區域）
brightness_threshold = 200

# 轉換為灰階圖像（計算亮度）
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 創建遮罩，過濾掉高亮區域
mask = gray_img < brightness_threshold

# 複製原圖
filtered_img = img.copy()

# 使用均值濾波來平滑圖像
smoothed_img = cv2.blur(filtered_img, (100, 100))

# 將過亮區域的像素替換為周圍9宮格的均值
filtered_img[~mask] = smoothed_img[~mask]

# 轉換為灰階圖像（計算亮度）
gray_img2 = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2GRAY)

# 高斯模糊
blurred_img = cv2.GaussianBlur(gray_img2, (5,5), 0)

# 使用 Canny 邊緣檢測
canny_edges = cv2.Canny(gray_img2, threshold1=30, threshold2=150)

# 顯示原圖與處理後的圖片
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# 原圖
axes[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axes[0].set_title("Original Image")
axes[0].axis("off")

# 處理後的圖
axes[1].imshow(cv2.cvtColor(canny_edges, cv2.COLOR_GRAY2RGB))
axes[1].set_title("Processed Image (High Brightness Removed & Smoothed)")
axes[1].axis("off")

plt.show()
