import cv2
import numpy as np

def Q6_Discretization_of_Color(img):
    # Read image
    img = img.astype(np.float32)
    # 定義條件
    conditions = [
        (img >= 0) & (img < 63),
        (img >= 63) & (img < 127),
        (img >= 127) & (img < 191),
        (img >= 191) & (img < 256)
    ]
    
    # 定義每個條件對應的值
    values = [32, 96, 160, 224]
    
    # 應用 np.select 來根據條件分配值
    categorized_image = np.select(conditions, values)
    return categorized_image
    