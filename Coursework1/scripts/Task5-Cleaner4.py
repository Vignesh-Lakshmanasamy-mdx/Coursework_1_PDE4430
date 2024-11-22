#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

from std_srvs.srv import Empty
from turtlesim.srv import Kill,Spawn,TeleportAbsolute

x_value=0
y_value=0
deg=0


def posecallback(pose_message):
    global x_value,y_value,deg
    x_value=pose_message.x
    y_value=pose_message.y
    deg=pose_message.theta 


def main():

    rospy.init_node('Turtlesim_Vaccum_cleaner',anonymous=True)

    global cmd_vel_pub
    cmd_vel_pub=rospy.Publisher('/turtle4/cmd_vel',Twist,queue_size=10)
    pose_sub=rospy.Subscriber('/turtle4/pose',Pose,posecallback)

    one_cleaner()

    rospy.spin()

def forward(value):
    twist=Twist()
    twist.linear.x=value
    cmd_vel_pub.publish(twist)
    rospy.sleep(2)

def rotate_deg(rotate):
    global x_value,y_value
    rospy.wait_for_service('turtle4/teleport_absolute')
    tele_turtle = rospy.ServiceProxy('turtle4/teleport_absolute', TeleportAbsolute)
    tele_turtle(x_value,y_value,rotate)
    rospy.sleep(1)

def kill():
    rospy.wait_for_service('kill')
    kill_turtle = rospy.ServiceProxy('kill', Kill)
    kill_turtle("turtle4")

def spawn():
    rospy.wait_for_service('spawn')
    add_turtle = rospy.ServiceProxy('spawn', Spawn)
    add_turtle(6,6,0.0,"turtle4")

def wall_detection():
    if x_value<=6.5 or x_value>=10 or y_value<=6 or y_value>=10:
        return True
    return False

def avoid_wall():
    twist=Twist()
    if wall_detection():
        if deg==0:
            rotate_deg(1.57)
            twist.linear.x=0.5
            cmd_vel_pub.publish(twist)
            rospy.sleep(1)
            rotate_deg(3.14)
            
        else:
            rotate_deg(1.57)
            twist.linear.x=0.5
            cmd_vel_pub.publish(twist)
            rospy.sleep(1)
            rotate_deg(0)            
            

def cycle():
    forward(4.5)
    """
    rotate_deg(1.57)
    forward(0.5)
    rotate_deg(3.14)
    """
    avoid_wall()
    forward(4.5)
    """
    rotate_deg(1.57)   
    forward(0.5)
    rotate_deg(0)
    """
    avoid_wall()
    

def one_cleaner():
    #kill()
    spawn()
    rospy.sleep(1)
    
    for count in range(4):
        cycle()
    forward(4.5)
    avoid_wall()
    forward(4.5)
    print(x_value,y_value,deg)

def func_reset():
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()       

if __name__ == "__main__":
    main()

