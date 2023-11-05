import cv2
import numpy as np

from utils import show_img

image = cv2.imread('./img/LAADS.jpg', cv2.IMREAD_GRAYSCALE)

row_num = len(image)
col_num = len(image[0])

"""
x' = x * a + y * b + c
y' = y * d + y * e + f
"""
# 平移
M1 = np.float32(
    [
        [1,0,50],
        [0,1,50]
    ]
)
# 旋转
M2 = cv2.getRotationMatrix2D(
    (len(image) / 2, len(image[0]) / 2),
    10, # 旋转角度(十进制度) 逆时针为正
    1
)
# 倾斜
M3 = cv2.getAffineTransform(
    np.float32(
        [
            [0,0],
            [col_num - 1,0],
            [0,row_num - 1]
        ]
    ),
    np.float32(
        [
            [0,100],
            [col_num - 1,0],
            [0,row_num - 1]
        ]
    )
)
print(image.shape)
dst = cv2.warpAffine(image, M3, image.T.shape)
show_img(dst)