import os
import cv2

image = cv2.imread('./img/LAADS.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('test', image)
os.makedirs('./dist')
cv2.imwrite('./dist/test.jpg', image)
key = cv2.waitKey(10000)
cv2.destroyAllWindows()