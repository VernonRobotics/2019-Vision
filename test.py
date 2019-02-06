import numpy as np
import cv2
from line_detection import getPointsForRobotControl 

'''img = cv2.imread('Test_Images/image3.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = np.zeros((100,100,3), np.uint8)
rectangle = cv2.rectangle(img, (5, 10),(90,95),(255,255,255),-1)

cv2.imwrite('Test_Images/template.jpg', rectangle)'''

print getPointsForRobotControl()

