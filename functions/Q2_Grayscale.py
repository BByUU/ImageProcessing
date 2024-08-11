import cv2

def Q2_Grayscale(img):
    # 直接使用 OpenCV 函式
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

    # # 手动计算灰度图像
    # # 基於 ITU-R BT.709 標準，該標準用於高清電視（HDTV）的色彩空間。它定義了 RGB 色彩空間到灰度空間的轉換加權係數
    # img = img.astype(np.float32)  # 使用 np.float32 而不是 np.float (np.float 已弃用)
    # b = img[:, :, 0]
    # g = img[:, :, 1]
    # r = img[:, :, 2]
    # out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # out = out.astype(np.uint8)
    # return out
