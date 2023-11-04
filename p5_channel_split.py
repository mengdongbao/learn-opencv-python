import cv2

image = cv2.imread('./img/LAADS.jpg')

r, g, b = cv2.split(image)
print(r)
rgb = cv2.merge([r, g, b])
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(image_hsv)
print(h)

""" 练习: H 通道全调整为 180 """

h[:, :] = 180
hsv = cv2.merge([h, s, v])
cv2.imshow('', hsv)
cv2.waitKey(1000 * 3)
cv2.destroyAllWindows()