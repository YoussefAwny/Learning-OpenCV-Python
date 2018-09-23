import numpy as np
import  cv2

#Simple thresholding
# dummy way
bw = cv2.imread("detect_blob.png", 0)
height, width = bw.shape[0:2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height, width, 1], 'uint8')

thresh = 85

for row in range(0, height):
    for col in range(0, width):
        if bw[row][col] > thresh:
            binary[row][col] = 255

cv2.imshow("Slow Binary", binary)

# built in thresholding

ret, thresh = cv2.threshold(bw, 85, 255, cv2.THRESH_BINARY)
cv2.imshow("cv", thresh)

#Adaptive thresholding

img = cv2.imread("sudoku.png", 0)
cv2.imshow("original2", img)

ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("basic Binary 2", thresh_basic)

thres_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("adaptive thresholding", thres_adapt)


cv2.waitKey(0)
cv2.destroyAllWindows()