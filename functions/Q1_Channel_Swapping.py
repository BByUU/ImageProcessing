import cv2
def Q1_Channel_Swapping(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img