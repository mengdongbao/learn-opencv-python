import cv2
from cv2.typing import MatLike

def show_img(data:MatLike, second: int=3):
    cv2.imshow('', data)
    cv2.waitKey(second * 1000)
    cv2.destroyAllWindows()