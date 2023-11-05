import cv2

from utils import show_img

img = cv2.imread('./img/LAADS.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# 二值化
# retval, dst = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# show_img(dst, 100)

# 反二值化
# retval, dst = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)
# show_img(dst, 100)

# 低阈值零处理
# retval, dst = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TOZERO)
# show_img(dst, 100)

# 高阈值零处理
# retval, dst = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TOZERO_INV)
# show_img(dst, 100)

# 截断处理
# retval, dst = cv2.threshold(img_gray, 150, 255, cv2.THRESH_TRUNC)
# show_img(dst, 100)

# 自适应处理
# dst = cv2.adaptiveThreshold(
#     img_gray,
#     255,
#     cv2.ADAPTIVE_THRESH_MEAN_C,
#     cv2.THRESH_BINARY, # 二值或反二值
#     5,
#     3
# )
# show_img(dst, 100)



# Otsu 方法自动寻找阈值
t, dst = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
show_img(img_gray, 10)



