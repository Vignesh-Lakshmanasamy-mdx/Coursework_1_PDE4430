#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,math
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
    cmd_vel_pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    pose_sub=rospy.Subscriber('/turtle1/pose',Pose,posecallback)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    rospy.spin()

def forward(value):
    twist=Twist()
    twist.linear.x=value
    cmd_vel_pub.publish(twist)
    rospy.sleep(2)

def rotate_deg(rotate):
    global x_value,y_value
    rospy.wait_for_service('turtle1/teleport_absolute')
    tele_turtle = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    tele_turtle(x_value,y_value,rotate)
    rospy.sleep(1)

def kill():
    rospy.wait_for_service('kill')
    kill_turtle = rospy.ServiceProxy('kill', Kill)
    kill_turtle("turtle1")

def spawn():
    rospy.wait_for_service('spawn')
    add_turtle = rospy.ServiceProxy('spawn', Spawn)
    add_turtle(0.5,0.5,0.0,"turtle1")

def wall_detection():
    if x_value<=1 or x_value>=10 or y_value<=1 or y_value>=10:
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
    forward(10)
    """
    rotate_deg(1.57)
    forward(0.5)
    rotate_deg(3.14)
    """
    avoid_wall()
    forward(10)
    """
    rotate_deg(1.57)   
    forward(0.5)
    rotate_deg(0)
    """
    avoid_wall()
    

def one_cleaner():
    kill()
    spawn()
    rospy.sleep(1)
    
    for count in range(10):
        cycle()
    forward(10)
    
def func_reset():
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()       


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task4.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 611, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.Start_the_1_cleaner = QtWidgets.QPushButton(Dialog)
        self.Start_the_1_cleaner.setGeometry(QtCore.QRect(180, 120, 281, 31))
        self.Start_the_1_cleaner.setObjectName("Start_the_1_cleaner")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 190, 181, 51))
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Start_the_1_cleaner.clicked.connect(one_cleaner)
        self.pushButton_5.clicked.connect(func_reset)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">PDE4430 - Mobile Robotics</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coursework 1 -  Task 4</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#c17d11;\">Vaccum Cleaning behaviour </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Start_the_1_cleaner.setText(_translate("Dialog", "Start the Vaccum Cleaner"))
        self.pushButton_5.setText(_translate("Dialog", "Reset Turtle Window"))

       
if __name__ == "__main__":
    main()

