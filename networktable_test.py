import threading
import time
from networktables import NetworkTables
#from line_detection import getPointsForRobotControl

import logging

logging.basicConfig(level=logging.DEBUG)

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.19.89.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

print("Connected")

vis_T = NetworkTables.getTable("VisionTable")
robot_state = vis_T.getAutoUpdateValue("RobotState", "disabled")
counter = 0
#def vision_processing():
while True:
    y, angle = getPointsForRobotControl()
    vis_T.putNumber("Y", y)
    vis_T.putNumber("Angle", angle)
    '''counter = counter + 1
    vis_T.putNumber("Y", counter)'''
    print(robot_state.value)
    time.sleep(.4)

#def camera_feed():

'''vis_thread = threading.Thread(name='vision_thread', target=vision_processing)
vis_thread.setDaemon(True)
vis_thread.start()'''
#cam_thread = threading.Thread(name="camera_feed", target=camera_thread)
#cam_thread.setDaemon(True)


'''if not robot_state.value == "disabled":
    print robot_state.value
    vis_thread.start()'''
    #cam_thread.start()
