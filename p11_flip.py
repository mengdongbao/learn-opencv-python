import cv2

from utils import show_img

image = cv2.imread('./img/LAADS.jpg')

# 0: X轴翻转 1: Y轴翻转 -1:同时沿XY翻转
dst = cv2.flip(image, 0)
show_img(dst)