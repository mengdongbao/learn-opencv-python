import os
import cv2

image = cv2.imread('./img/LAADS.jpg')

image_rgba = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)
r, g, b, a = cv2.split(image_rgba)
a[:, :] = 172
os.makedirs('./dist')
cv2.imwrite('./dist/test.png', cv2.merge([r, g, b, a]))