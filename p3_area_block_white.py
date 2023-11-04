import cv2

image = cv2.imread('./img/LAADS.jpg')

for i in range(100, 200):
    for j in range(200, 300):
        image[i, j] = [255, 255, 255]
cv2.imshow('', image)
cv2.waitKey(1000 * 3)
cv2.destroyAllWindows()