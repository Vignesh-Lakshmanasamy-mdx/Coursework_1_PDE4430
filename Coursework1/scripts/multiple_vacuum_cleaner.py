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

    
def func_reset():
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()       

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task5.ui'
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
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 40, 611, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(270, 140, 61, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(60, 140, 191, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 200, 181, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 140, 181, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">PDE4430 - Mobile Robotics</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coursework 1 -  Task 5</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#c17d11;\">Multiple turtles vaccum cleaning behaviour </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Dialog", "4"))
        self.comboBox.setItemText(1, _translate("Dialog", "5"))
        self.comboBox.setItemText(2, _translate("Dialog", "11"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of Turtles</p></body></html>"))
        self.pushButton_5.setText(_translate("Dialog", "Reset Turtle Window"))
        self.pushButton_3.setText(_translate("Dialog", "Start the cleaner"))


if __name__ == "__main__":
    main()
    
