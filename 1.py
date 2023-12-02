
import cv2
import numpy

img = cv2.imread ("1_input.jpg")
img = cv2.cvtColor (img , cv2.COLOR_BGR2GRAY)

threshold = 100
img [img > threshold] = 255
img [img <= threshold] = 0

cv2.imshow ("result 1" , img)
cv2.waitKey ()