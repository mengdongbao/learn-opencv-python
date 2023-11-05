# 透视
import cv2
import numpy as np

from utils import show_img

image = cv2.imread('./img/LAADS.jpg', cv2.IMREAD_GRAYSCALE)
row_num = len(image)
col_num = len(image[0])


M = cv2.getPerspectiveTransform(
    np.float32(
        [
            [0, 0],
            [col_num - 1, 0],
            [0, row_num - 1],
            [col_num - 1, row_num - 1]
        ],
    ),
    np.float32(
        [
            [100, 0],
            [col_num - 1 - 100, 0],
            [0, row_num - 1],
            [col_num - 1, row_num - 1]
        ]
    )
)

dst = cv2.warpPerspective(image, M, (col_num, row_num))
show_img(dst)