import cv2
import numpy as np

def Grayscale(img):
    # # 复制原始图像
    img_origion = img.copy()
    # img = img.astype(np.float32)  # 使用 np.float32 而不是 np.float (np.float 已弃用)
    # b = img[:, :, 0]
    # g = img[:, :, 1]
    # r = img[:, :, 2]

    # 灰度化
    # 使用 cv2.cvtColor 将 RGB 图像转换为灰度
    gray = cv2.cvtColor(img_origion, cv2.COLOR_BGR2GRAY)

    ## 显示灰度图像
    # cv2.imshow("Gray Image", gray)

    # # 手动计算灰度图像
    # # 基於 ITU-R BT.709 標準，該標準用於高清電視（HDTV）的色彩空間。它定義了 RGB 色彩空間到灰度空間的轉換加權係數
    # out = 0.2126 * r + 0.7152 * g + 0.0722 * b
    # out = out.astype(np.uint8)

    # # 保存灰度图像
    # cv2.imwrite("out.jpg", out)
    
    return gray

# # 读取图像
# img = cv2.imread("U:\\_GitHubProject\\ImageProcessing\\_image.png")

# # 转换为灰度图像并显示结果
# result = Grayscale(img)
# cv2.imshow("Result Image", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
