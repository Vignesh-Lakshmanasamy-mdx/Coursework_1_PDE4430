#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,math
from std_srvs.srv import Empty

x_value=0
y_value=0
deg=0
cmd_vel_controller=1.0
index=0

def posecallback(pose_message):
    global x_value,y_value,deg
    x_value=pose_message.x
    y_value=pose_message.y
    deg=pose_message.theta 


def main():

    rospy.init_node('Turtlesim_Avoid_wall_collision',anonymous=True)

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
    global x_value,y_value,deg,cmd_vel_controller,index
    twist=Twist()
    if (x_value>=1 and x_value<=10) and (y_value>=1 and y_value<=10):
        twist.linear.x=cmd_vel_controller
        cmd_vel_pub.publish(twist)
    elif (x_value<1.5 or x_value>9.5 or y_value<1.5 or y_value>9.5) and index==0:
        change_angle(0)

def reverse():

    twist=Twist()
    global x_value,y_value,deg,cmd_vel_controller

    if (x_value>=1 and x_value<=10) and (y_value>=1 and y_value<=10):
        twist.linear.x=-(cmd_vel_controller)
        cmd_vel_pub.publish(twist)
    elif (x_value<1.5 or x_value>9.5 or y_value<1.5 or y_value>9.5) and index==0:
        change_angle(0)
    
def change_angle(value):
    global radian_value,cmd_vel_controller,x_value,y_value,deg,index
    deg_value=int(value)
    radian_value=deg_value*0.0174533
    twist=Twist()
    global deg
    #print(radian_value)

    rate=rospy.Rate(10)
    if (x_value>=1 and x_value<=10) and (y_value>=1 and y_value<=10):
        while not rospy.is_shutdown():

            #calculating difference in the current and expected theta value
            theta_diff=radian_value-deg
            #normalization of theta formula 
            theta_diff=(theta_diff+math.pi)%(2*math.pi)-math.pi

            if abs(theta_diff)>0.1: 
                twist.angular.z=0.5432*theta_diff/abs(theta_diff)
                cmd_vel_pub.publish(twist)
        
            else:
                twist.angular.z=0.0
                cmd_vel_pub.publish(twist)
                break
            rate.sleep()
    elif (x_value<1.5 or x_value>9.5 or y_value<1.5 or y_value>9.5) and index==0:
        if x_value<1.5:
            radian_value=0
        elif x_value>9.5:
            radian_value= (180*0.0174533)
        elif y_value>9.5:
            radian_value= (270*0.0174533)
        elif y_value<1.5:
            radian_value=(90*0.0174533)

        while not rospy.is_shutdown():

            #calculating difference in the current and expected theta value
            theta_diff=radian_value-deg
            #normalization of theta formula 
            theta_diff=(theta_diff+math.pi)%(2*math.pi)-math.pi

            if abs(theta_diff)>0.1: 
                twist.angular.z=0.5432*theta_diff/abs(theta_diff)
                cmd_vel_pub.publish(twist)
        
            else:
                twist.angular.z=0.0
                twist.linear.x=1.0
                cmd_vel_pub.publish(twist)
                break
            rate.sleep()
def change_speed(value):
    
    global cmd_vel_controller
    cmd_vel_controller=float(value)


def func_reset():
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()

def by_rotation():
    global index
    index=0
    
def by_uturn():
    global index
    index=1

# Form implementation generated from reading ui file 'Task3.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(654, 481)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 101, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 140, 91, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 20, 611, 101))
        self.textBrowser.setObjectName("textBrowser")

        self.Vel_control = QtWidgets.QSlider(Dialog)
        self.Vel_control.setGeometry(QtCore.QRect(510, 150, 51, 221))
        self.Vel_control.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Vel_control.setMaximum(6)
        self.Vel_control.setMinimum(1)
        self.Vel_control.setProperty("value", 1)
        self.Vel_control.setOrientation(QtCore.Qt.Vertical)
        self.Vel_control.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Vel_control.setTickInterval(1)
        self.Vel_control.setObjectName("Vel_control")

        self.direction_control = QtWidgets.QDial(Dialog)
        self.direction_control.setGeometry(QtCore.QRect(40, 170, 171, 191))
        self.direction_control.setMaximum(360)
        self.direction_control.setProperty("value", 0)
        self.direction_control.setInvertedAppearance(True)
        self.direction_control.setObjectName("direction_control")

        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 360, 211, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(260, 140, 181, 51))
        self.pushButton_4.setObjectName("pushButton_4")

        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(490, 380, 141, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.lcdNumberDegree = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumberDegree.setGeometry(QtCore.QRect(100, 240, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumberDegree.setFont(font)
        self.lcdNumberDegree.setStyleSheet("")
        self.lcdNumberDegree.setObjectName("lcdNumberDegree")

        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(490, 140, 141, 241))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(573, 332, 41, 31))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 210, 251, 111))
        self.textEdit_2.setObjectName("textEdit_2")

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(240, 270, 231, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Avoid by Rotation")
        self.comboBox.addItem("Avoid by uturn")
        
        self.textEdit_2.raise_()
        self.textBrowser_3.raise_()
        self.buttonBox.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.Vel_control.raise_()
        self.direction_control.raise_()
        self.textBrowser_2.raise_()
        self.pushButton_4.raise_()
        self.textBrowser_4.raise_()
        self.lcdNumberDegree.raise_()
        self.lcdNumber_2.raise_()
        self.comboBox.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(forward)
        self.pushButton_2.clicked.connect(reverse)
        self.direction_control.valueChanged.connect(change_angle)
        self.direction_control.valueChanged.connect(self.dis_angle)
        self.Vel_control.valueChanged.connect(change_speed)
        self.Vel_control.valueChanged.connect(self.dis_speed)
        self.pushButton_4.clicked.connect(func_reset)
        
        self.comboBox.currentIndexChanged.connect(self.method_selection)

    def dis_speed(self,value):
        if value==0:
            self.lcdNumber_2.display(value+1)
        else:
            self.lcdNumber_2.display(value)

    def dis_angle(self,value):
        self.lcdNumberDegree.display(value)
    
    def method_selection(self,index):
        if index==0:
            by_rotation()
        elif index==1:
            by_uturn()


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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coursework 1 -  Task 3</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#c17d11;\">Avoiding wall collision </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#c17d11;\"> Override movement if wall hitting is imminent </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Vel_control.setToolTip(_translate("Dialog", "<html><head/><body><p>1</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Direction control</p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "Reset Turtle Window"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed control</p></body></html>"))
        self.lcdNumberDegree.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#5c3566;\">Select the method of Avoiding wall Collision</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "Avoid wall collision by rotation"))
        self.comboBox.setItemText(1, _translate("Dialog", "Avoid wall collision by U turn"))


if __name__ == "__main__":
    main()    
