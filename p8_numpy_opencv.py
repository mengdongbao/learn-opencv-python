import cv2
import numpy as np

from utils import show_img
width = 200
height = 100

# 纯黑
# img = np.zeros((height, width), np.uint8)
# show_img(img, 3)

# 纯白
# img = np.ones((height, width), np.uint8) * 255
# show_img(img, 3)

# 指定区域白色
# img = np.zeros((height, width), np.uint8)
# img[:50, 50:] = 255
# show_img(img, 3)


# 生成彩色图形
# img = np.zeros((height, width, 3), np.uint8)
# only_blue = img.copy()
# only_blue[:, :, 0] = 255
# show_img(only_blue, 3)

# 生成随机图像
# img = np.random.randint(0, 255, size=(height, width, 3), dtype=np.uint8)
# show_img(img)

# 拼接影像
img = cv2.imread('./img/LAADS.jpg')
img_h = np.hstack((img, img))
show_img(img_h)