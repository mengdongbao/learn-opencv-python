import cv2

image = cv2.imread('./img/LAADS.jpg')

""" GRAY 灰度空间 """
# dst = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# cv2.imshow('', dst)
# cv2.waitKey(1000 * 3)
# cv2.destroyAllWindows()


""" HSV 色调[0,180] 饱和度 亮度"""
dst = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
cv2.imshow('', dst)
cv2.waitKey(1000 * 3)
cv2.destroyAllWindows()



