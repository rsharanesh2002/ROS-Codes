#!/usr/bin/env python3
import rospy # importing the rospy library
from turtlesim.srv import *
from turtlesim.msg import  *
from std_srvs.srv import Empty
turtle_x = 0
turtle_y = 0
theta = 0

def pose_callback(pose):
    global turtle_x,turtle_y,theta
    turtle_x = pose.x
    turtle_y = pose.y
    theta = pose.theta
    rospy.loginfo("Turtle\'s X = %f ; Turtle\'s Y = %f ; Theta = %f \n",turtle_x,turtle_y,theta)


def func():
    global turtle_x,turtle_y,theta
    rospy.init_node('move_turtle',anonymous=True)
    rospy.Subscriber('/turtle1/pose',Pose,pose_callback)
    #rospy.loginfo("X:axis at %f \n",turtle_x)
    rospy.wait_for_service("/turtle1/teleport_absolute")
    tele_abs = rospy.ServiceProxy("/turtle1/teleport_absolute", TeleportAbsolute)
    #start_coord = int(input("Enter the start point (symmetric coordinate; enter only one value): "))
    num_shape = 5 #int(input("Enter the number of point edged star the bot should cover: "))
    angle =  (3.14/num_shape)
                          
    try:
      resp1 = tele_abs(int(turtle_x),int(turtle_y),0)
      #resp2 = tele_abs(start_coord,start_coord,0)
    except rospy.ServiceException as exc:
      print("Service did not process request: " + str(exc))
    
    rospy.wait_for_service("/clear")
    clear = rospy.ServiceProxy("/clear",Empty)
    res = clear()

    rospy.wait_for_service("/turtle1/teleport_relative")
    tele_rel = rospy.ServiceProxy("/turtle1/teleport_relative",TeleportRelative)
   
    try:
      tele_rel(2,angle)
      tele_rel(2,angle*4)
      tele_rel(2,angle*2)
      tele_rel(2,angle*4)
      tele_rel(2,angle*2)
      tele_rel(2,angle*4)
      tele_rel(2,angle*2)
      tele_rel(2,angle*4)
      tele_rel(2,angle*2)
      tele_rel(2,angle*4)
      
    except:
      print("Service did not process request: " + str(exc))
  
if __name__ == '__main__':
    try:
        #Testing our function
        func()
    except rospy.ROSInterruptException: pass
