#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

x_value=0
y_value=0
deg=0
cmd_vel_controller=1.0


def posecallback(pose_message):
    global x_value,y_value,deg
    x_value=pose_message.x
    y_value=pose_message.y
    deg=pose_message.theta 

def main():

    rospy.init_node('Turtlesim_teleoperation',anonymous=True)

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

def forward():

    twist=Twist()
    global x_value,y_value,deg,cmd_vel_controller
    twist.linear.x=cmd_vel_controller
    cmd_vel_pub.publish(twist)
   

def reverse():

    twist=Twist()
    global x_value,y_value,deg,cmd_vel_controller
    twist.linear.x=-(cmd_vel_controller)
    cmd_vel_pub.publish(twist)

def change_angle(value):
    deg_value=int(value)
    radian_value=deg_value*0.0174533
    twist=Twist()
    global deg
    #print(radian_value)
    
    rate=rospy.Rate(10)
    

    
    while not rospy.is_shutdown():

        #calculating difference in the current and expected theta value
        theta_diff=radian_value-deg
        #normalization of theta formula - took from google
        theta_diff=(theta_diff+3.14)%(2*3.14)-3.14

        if abs(theta_diff)>0.1:
            twist.angular.z=0.5432*theta_diff/abs(theta_diff)
            cmd_vel_pub.publish(twist)
        
        else:
            
            twist.angular.z=0.0
            cmd_vel_pub.publish(twist)
            break
        rate.sleep()

def change_speed(value):
    
    global cmd_vel_controller
    cmd_vel_controller=float(value)


# Form implementation generated from reading ui file 'Task1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(68, 130, 141, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 130, 131, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 601, 81))
        self.textBrowser.setObjectName("textBrowser")

        self.Vel_control = QtWidgets.QSlider(Dialog)
        self.Vel_control.setGeometry(QtCore.QRect(440, 140, 51, 231))
        self.Vel_control.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Vel_control.setMaximum(10)
        self.Vel_control.setOrientation(QtCore.Qt.Vertical)
        self.Vel_control.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Vel_control.setTickInterval(1)
        self.Vel_control.setObjectName("Vel_control")

        self.direction_control = QtWidgets.QDial(Dialog)
        self.direction_control.setGeometry(QtCore.QRect(110, 160, 171, 191))
        self.direction_control.setMaximum(180)
        self.direction_control.setProperty("value", 0)
        self.direction_control.setInvertedAppearance(True)
        self.direction_control.setObjectName("direction_control")
        
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 340, 141, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(forward)
        self.pushButton_2.clicked.connect(reverse)
        self.direction_control.valueChanged.connect(change_angle)
        self.Vel_control.valueChanged.connect(change_speed)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Forward"))
        self.pushButton_2.setText(_translate("Dialog", "Reverse"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">PDE4430 - Mobile Robotics</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coursework 1 -  Task 1</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#204a87;\">Teleoperation Using the Keyboard, with an option to change movement speed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Vel_control.setToolTip(_translate("Dialog", "<html><head/><body><p>1</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Direction control</p></body></html>"))


if __name__ == "__main__":
    main()
