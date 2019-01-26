import numpy as np
import cv2

#Try to find cameras
'''counter = 0

while(True):
    try: 
        cap = cv2.VideoCapture(counter)
        counter+=1
        print("Camera found at " + counter)
        break
    except:
        print("")
    if(counter > 18): 
        break
'''

cap = cv2.VideoCapture(0)


while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()