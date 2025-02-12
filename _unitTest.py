# Unit test

import cv2 as cv
import functions.__init__ as __init__
from Q8_Max_Pooling import Q8_Max_Pooling as test_func

# 設定要測試的函式名稱
function_name = 'Q8_Max_Pooling'
# 使用 getattr 獲取函式
test_func = getattr(__init__, function_name, None)

image = cv.imread(r'u:\_GitHubProject\ImageProcessing\images\imori.jpg')

converted_image = test_func(image)
cv.imshow('Converted Image', converted_image)
cv.waitKey(0)
cv.destroyAllWindows()