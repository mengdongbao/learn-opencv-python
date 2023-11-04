import cv2

image = cv2.imread('./img/LAADS.jpg')

print(image)
# print('彩色影像的 行，列，通道:', image.shape) # 彩色影像的 行，列，通道
# print('像素个数:', image.size) # 像素个数
# print('dtype:', image.dtype) # 数据类型
# print('某点RGB:', image[100, 100], 'px')