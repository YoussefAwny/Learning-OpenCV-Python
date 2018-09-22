import numpy as np
import cv2

img = cv2.imread("thresh.jpg")
cv2.imshow("original", img)
cv2.moveWindow("original", 0, 0)
h, w, c = img.shape;

blur = cv2.GaussianBlur(img, (5, 55), 0)
cv2.imshow("blur", blur)
cv2.moveWindow("blur", w, 0)

kernel = np.ones((5,5),'uint8')

dilate = cv2.dilate(img, kernel, iterations=1)
erode = cv2.erode(img, kernel, iterations=1)
cv2.imshow("dilate", dilate)
cv2.imshow("erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()