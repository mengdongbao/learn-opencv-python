import cv2

from utils import show_img

image = cv2.imread('./img/LAADS.jpg')

# 指定缩放大小
# dst = cv2.resize(image, (100, 200))
# show_img(dst)


# 指定缩放比例
dst = cv2.resize(image, None, fx=.5, fy=.5)
show_img(dst)