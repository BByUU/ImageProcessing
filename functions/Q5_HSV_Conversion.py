import cv2
import numpy as np

def Q5_HSV_Conversion(img):
    # 使用 OpenCV 將圖像從 BGR 轉換到 HSV 色彩空間
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 調整色調（H值），色調增加 180 度並取模 360
    # OpenCV 在將 BGR 轉換到 HSV 時，色相（H）的範圍是 [0, 179]。這是因為在 8-bit 圖像中，色相值被壓縮到了 180 度範圍內，以適應 [0, 255] 的範圍。
    # 因此，當嘗試將色相增加 180 度並取 mod 360 時，實際上應使用取 mod 180（% 180），而不是 360，以保持在 OpenCV 的色相範圍內。
    hsv[:, :, 0] = (hsv[:, :, 0].astype(int) + 90) % 180

    # 使用 OpenCV 從 HSV 色彩空間轉回 BGR 色彩空間
    output_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return output_img


    # # 將圖像數據從0-255整數轉換為0.0-1.0浮點數
    # img = img.astype(np.float32) / 255.

    # # 初始化輸出圖像，與輸入圖像尺寸和類型相同
    # out = np.zeros_like(img)

    # # 找到每個像素中的最大和最小值，用於計算HSV
    # max_v = np.max(img, axis=2).copy()
    # min_v = np.min(img, axis=2).copy()
    # min_arg = np.argmin(img, axis=2)

    # # 初始化色調數組
    # H = np.zeros_like(max_v)

    # # 當最大值等於最小值時，色調設為0（灰階）
    # H[np.where(max_v == min_v)] = 0

    # # 如果最小值來自藍色通道
    # ind = np.where(min_arg == 0)
    # H[ind] = 60 * (img[..., 1][ind] - img[..., 2][ind]) / (max_v[ind] - min_v[ind]) + 60

    # # 如果最小值來自紅色通道
    # ind = np.where(min_arg == 2)
    # H[ind] = 60 * (img[..., 0][ind] - img[..., 1][ind]) / (max_v[ind] - min_v[ind]) + 180

    # # 如果最小值來自綠色通道
    # ind = np.where(min_arg == 1)
    # H[ind] = 60 * (img[..., 2][ind] - img[..., 0][ind]) / (max_v[ind] - min_v[ind]) + 300
    
    # # 計算亮度（最大值）
    # V = max_v.copy()
    # # 計算飽和度（最大值與最小值的差）
    # S = max_v.copy() - min_v.copy()

    # # 色調平移操作，將色調加180然後取模360
    # H = (H + 180) % 360

    # # 計算RGB轉換所需的中間參數
    # C = S
    # H_ = H // 60
    # X = C * (1 - np.abs( H_ % 2 - 1))
    # Z = np.zeros_like(H)

    # # 定義RGB轉換的顏色組合
    # vals = [[Z, X, C], [Z, C, X], [X, C, Z], [C, X, Z], [C, Z, X], [X, Z, C]]

    # # 根據H_的值決定使用哪種顏色組合
    # for i in range(6):
    #     ind = np.where((i <= H_) & (H_ < (i+1)))
    #     out[..., 0][ind] = (V-C)[ind] + vals[i][0][ind]
    #     out[..., 1][ind] = (V-C)[ind] + vals[i][1][ind]
    #     out[..., 2][ind] = (V-C)[ind] + vals[i][2][ind]

    # # 當最大值等於最小值時（灰階），設置RGB為0
    # out[np.where(max_v == min_v)] = 0
    # # 將輸出數據從0.0-1.0轉換為0-255並轉為uint8
    # out = (out * 255).astype(np.uint8)
    
    # return out
