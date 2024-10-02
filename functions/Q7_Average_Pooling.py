import cv2
import numpy as np

def Q7_Average_Pooling(img, G=8):
    # 轉換為浮點型態以進行計算
    img = img.astype(np.float32)
    
    # 取得圖像的高(H)、寬(W)、通道數(C)
    H, W, C = img.shape
    
    # 池化後每個區塊的高和寬
    Nh = int(H / G)
    Nw = int(W / G)
    
    # 建立一個新圖像來存放結果
    out = np.zeros_like(img)

    # 進行平均池化
    for y in range(Nh):
        for x in range(Nw):
            for c in range(C):
                # 計算 GxG 區域的平均值
                pool_region = img[G*y:G*(y+1), G*x:G*(x+1), c]
                avg_value = np.mean(pool_region)
                
                # 將平均值填充回該區域
                out[G*y:G*(y+1), G*x:G*(x+1), c] = avg_value

    # 將結果轉換為 uint8 格式
    out = out.astype(np.uint8)
    
    return out
