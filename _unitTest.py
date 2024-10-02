# Unit test

import cv2 as cv
import functions.__init__ as __init__
#from Q5_HSV_Conversion import Q5_HSV_Conversion as test_func

# 設定要測試的函式名稱
function_name = 'Q6_Discretization_of_Color'
# 使用 getattr 獲取函式
test_func = getattr(__init__, function_name, None)

image = cv.imread(r'u:\_GitHubProject\ImageProcessing\images\imori.jpg')

converted_image = test_func(image)
cv.imshow('Converted Image', converted_image)
cv.waitKey(0)
cv.destroyAllWindows()