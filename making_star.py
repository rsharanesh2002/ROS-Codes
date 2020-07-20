#!/usr/bin/env python
import rospy # importing the rospy library
from turtlesim.srv import *
from turtlesim.msg import  *
from std_srvs.srv import Empty
  
'''
def pose_callback(pose):
    global turtle_x,turtle_y,theta
    turtle_x = pose.x
    turtle_y = pose.y
    theta = pose.theta
    rospy.loginfo("Turtle\'s X = %f ; Turtle\'s Y = %f ; Theta = %f \n",turtle_x,turtle_y,theta)
'''

def func():
    rospy.init_node('move_turtle',anonymous=True)
    #rospy.Subscriber('/turtle1/pose',Pose,pose_callback)
    #rospy.loginfo("X:axis at %f \n",turtle_x)
    rospy.wait_for_service("/turtle1/teleport_absolute")
    tele_abs = rospy.ServiceProxy("/turtle1/teleport_absolute", TeleportAbsolute)
    try:
      #resp1 = tele_abs(int(turtle_x),int(turtle_y),0)
      resp2 = tele_abs(3,3,0)
    except rospy.ServiceException as exc:
      print("Service did not process request: " + str(exc))
    
    rospy.wait_for_service("/clear")
    clear = rospy.ServiceProxy("/clear",Empty)
    res = clear()


    rospy.wait_for_service("/turtle1/teleport_relative")
    tele_rel = rospy.ServiceProxy("/turtle1/teleport_relative",TeleportRelative)
    try:
      res1 = tele_rel(2,0.63)
      res2 = tele_rel(2,5.025)
      res3 = tele_rel(2,2.513)
      res4 = tele_rel(2,5.025)
      res5 = tele_rel(2,2.513)
      res6 = tele_rel(2,5.025)
      res7 = tele_rel(2,2.513)
      res8 = tele_rel(2,5.025)
      res9 = tele_rel(2,2.513)
      res10 = tele_rel(2,5.025)
    except:
      print("Service did not process request: " + str(exc))
  
if __name__ == '__main__':
    try:
        #Testing our function
        func()
    except rospy.ROSInterruptException: pass
