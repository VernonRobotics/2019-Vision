import cv2
import numpy as np

image = cv2.imread('Test_Images/image3.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

dst = cv2.fastNlMeansDenoisingColored(image, None, 6, 6, 7, 21)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(dst, 110, 255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
height, width = opening.shape[:2]
print height
print width
opening = cv2.rectangle(opening, (0,0), (width, 10), (0,0,0), -1)
opening = cv2.rectangle(opening, (0, height-10), (width, height), (0,0,0), -1)


#edged = cv2.Canny(opening, 30, 200)

_, contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


'''def get_contour_areas(contours):
    all_areas = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas'''

sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
#print get_contour_areas(sorted_contours)
for c in sorted_contours:
    if cv2.contourArea(c) > 1500.0:
        #cv2.drawContours(image, [c], -1, (0,255,0), 3)
        rows, cols = image.shape[:2]
        [vx,vy,x,y] = cv2.fitLine(c, cv2.DIST_L2,0,0.01,0.01)
        lefty = int((-x*vy/vx) + y)
        righty = int(((cols-x)*vy/vx)+y)
        cv2.line(image,(cols-1,righty),(0,lefty),(0,0,255),2)
        cv2.imshow("Largest Contour", image)
    


#cv2.imshow("Opening", opening)
#cv2.imshow("Contours", image)
cv2.waitKey(0)
cv2.destroyAllWindows()