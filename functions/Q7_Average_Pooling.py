import cv2
import numpy as np

def Q7_Average_Pooling(img, G=8):
    # # 轉換為浮點型態以進行計算
    # img = img.astype(np.float32)
    
    # # 取得圖像的高(H)、寬(W)、通道數(C)
    # H, W, C = img.shape
    
    # # 池化後每個區塊的高和寬
    # Nh = int(H / G)
    # Nw = int(W / G)
    
    # # 建立一個新圖像來存放結果
    # out = np.zeros_like(img)

    # # 進行平均池化
    # for y in range(Nh):
    #     for x in range(Nw):
    #         for c in range(C):
    #             # 計算 GxG 區域的平均值
    #             pool_region = img[G*y:G*(y+1), G*x:G*(x+1), c]
    #             avg_value = np.mean(pool_region)
                
    #             # 將平均值填充回該區域
    #             out[G*y:G*(y+1), G*x:G*(x+1), c] = avg_value

    # # 將結果轉換為 uint8 格式
    # out = out.astype(np.uint8)
    
    #out = cv2.blur(img, (G, G))
    out = cv2.boxFilter(img, -1, (G, G), normalize=True)
    
    '''
    手動平均池化：
    你可以把這個方法想像成在一個房間裡，大家都穿著不同顏色的衣服。你決定把房間分成小區塊，然後在每個小區塊裡，所有人都必須穿上相同的衣服。例如，你把房間分成 4x4 的區塊，然後在每個區塊裡，所有人的衣服顏色都變成該區塊裡原來的平均顏色。所以，房間裡會變得很整齊，每個區塊裡的人都穿同一種顏色的衣服，區塊之間的區別很明顯。

    cv2.blur()：
    cv2.blur() 則更像是把整個房間的人都聚在一起，讓每個人稍微改變他們的衣服顏色，但他們的顏色會根據身邊的人來調整。每個人都會混合一些左右鄰居的顏色，這樣每個人穿的顏色都變得有點模糊和相似，但他們仍然保持一些獨特的顏色。這樣房間裡的變化會更加平滑，顏色之間的過渡不會那麼突然。

    cv2.boxFilter()：
    cv2.boxFilter()跟 cv2.blur() 很像，但你可以決定是否讓顏色更加均勻或允許有些人穿得更亮或更暗。
    '''
    
    
    return out
