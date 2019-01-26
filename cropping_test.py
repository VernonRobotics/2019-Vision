import cv2
import numpy as np

image = cv2.imread('Test_Images/image2.jpg')
height, width = image.shape[:2]

'''start_row, start_col = int(height * .25), int(width*.25)

end_row, end_col = int(height * .75), int(width * .75)'''

start_row, start_col = 50, 50

end_row, end_col = height+50, height+50 
print height, width

cropped = image[start_row:end_row, start_col:end_col]

height, width = cropped.shape[:2]
print height
print width

cv2.imshow("Original Image", image)
cv2.imshow("Cropped Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()