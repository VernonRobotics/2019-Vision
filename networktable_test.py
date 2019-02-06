import threading
import time
from networktables import Networktables
from line_detection import getPointsForRobotControl

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

Netwoktables.initialize(server='10.19.89.2')
Networktables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

print("Connected")

vis_T = Networktables.getTable("VisionTable")
robot_state = vis_T.getAutoUpdateValue("RobotState", "disabled")
counter = 0
def vision_processing():
    while True:
        '''y, angle = getPointsForRobotControl()
        vis_T.putNumber("Y", y)
        vis_T.putNumber("Angle", angle)'''
        counter = counter + 1
        vis_T.putNumber("Y", counter)

        time.sleep(.4)

#def camera_feed():

vis_thread = threading.Thread(name='vision_thread', target=vision_processing)
vis_thread.setDaemon(True)

#cam_thread = threading.Thread(name="camera_feed", target=camera_thread)
#cam_thread.setDaemon(True)


if not robot_state.value == "disabled":
    vis_thread.start()
    #cam_thread.start()
