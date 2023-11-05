import cv2

from utils import show_img

image = cv2.imread('./img/LAADS.jpg')

# print(image)
# print('彩色影像的 行，列，通道:', image.shape) # 彩色影像的 行，列，通道
# print('像素个数:', image.size) # 像素个数
# print('dtype:', image.dtype) # 数据类型
# print('某点RGB:', image[100, 100], 'px')

img_gray = cv2.imread('./img/LAADS.jpg', cv2.IMREAD_GRAYSCALE)
print(image[0, 1, 0]*0.114 + image[0,1,1]*0.578 + image[0,1,2]*0.299)
print(img_gray[0, 1])