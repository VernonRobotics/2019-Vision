import cv2
import numpy as np
import math

cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)

while(True):
    ret, frame = cap.read()

    image = frame
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    M = np.ones(gray.shape, dtype= "uint8") * 10
    gray = cv2.subtract(gray, M)


    ret, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5,5), np.uint8)

    opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
    
    height, width = opening.shape[:2]
    opening = cv2.rectangle(opening, (0,0), (width, 10), (0,0,0), -1)
    opening = cv2.rectangle(opening, (0, height-10), (width, height), (0,0,0), -1)


    contours, hierarchy = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    
    try:
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

        c = sorted_contours[0]
        rows, cols = image.shape[:2]
        [vx,vy,x,y] = cv2.fitLine(c, cv2.cv.CV_DIST_L2,0,0.01,0.01)
        lefty = int((-x*vy/vx) + y)
        righty = int(((cols-x)*vy/vx)+y)
        slope = (float)(righty-lefty)/(cols-1)
        coord1 = (int(((-1 * lefty)/slope)),0)
        coord2 = (int((((-1 * lefty)+height)/slope)),height)
        cv2.line(image,(cols-1,righty),(0,lefty),(0,0,255),2)
        cv2.line(image, coord1, coord2, (255,0,0), 3)
    except:
        print("line calculation error")

        
    def getPointsForRobotControl():
        x1,y1 = coord1[0],coord1[1]
        x2, y2 = coord2[0], coord2[1]
        angle = 0.0
        x1 = (float)(x1-(width/2))/(width/2)
        y1 = (float)(y1-(height/2))/(height/2)
        x2 = (float)(x2-(width/2))/(width/2)
        y2 = (float)(y2-(height/2))/(height/2)
        
        angle = math.atan((x1-x2)/(y1-y2))
        x = (x1+x2)/2
        angle = round(angle,5)
        x = round(x,5)
        return x, angle

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
