import numpy as np
import cv2
import random

img = cv2.imread("fuzzy.png",1)
cv2.imshow("original", img)

#blur = cv2.GaussianBlur(img, (5,5), 10)
#cv2.imshow("blur", blur)

kernel = np.ones((10, 10), 'uint8')

#dilate = cv2.dilate(img, kernel, iterations=1)
#cv2.imshow("dilate", dilate)

erode = cv2.erode(img, kernel, iterations=1)
cv2.imshow("erode", erode)

gray = cv2.cvtColor(erode, cv2.COLOR_RGB2GRAY)
cv2.imshow("gray", gray)

ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh)

_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

objects = np.zeros((img.shape[0], img.shape[1], 3), 'uint8')


for c in contours:
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    area = cv2.contourArea(c)
    if area > 1000:
        cv2.drawContours(objects, [c], -1, color, -1)

cv2.imshow("contours", objects)




cv2.waitKey(0)
cv2.destroyAllWindows()