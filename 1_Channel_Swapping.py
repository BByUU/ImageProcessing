import cv2

# Read image
img = cv2.imread("image.png")
img_1 = img.copy()
b = img[:, :, 0].copy()
g = img[:, :, 1].copy()
r = img[:, :, 2].copy()

# RGB > BGR
img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

# Save result
cv2.imwrite("1_Channel_Swapping_ans.jpg", img)
cv2.imshow("result", img)


# You could use cv2.cvtColor() function to directly swap the color channels.
img_rgb = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
cv2.imshow("img_rgb", img_rgb)


cv2.waitKey(0)
cv2.destroyAllWindows()
