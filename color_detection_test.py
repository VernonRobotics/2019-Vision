import cv2
import numpy as np 

img = cv2.imread("Test_Images/image3.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

'''white = np.uint8([[[240,240,240]]])
hsvWhite = cv2.cvtColor(white, cv2.COLOR_BGR2HSV)
print(hsvWhite)

lower_color = np.array([hsvWhite[0][0][0]-10, 100, 100])
upper_color = np.array([hsvWhite[0][0][0]+10, 255, 255])'''

lower_color = np.array([0, 0, 0], dtype=np.uint8)
upper_color = np.array([0, 0, 100], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_color, upper_color)
res = cv2.bitwise_and(img, img, mask = mask)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
