#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,math
from std_srvs.srv import Empty
from turtlesim.srv import Kill,Spawn,TeleportAbsolute
"""
from Task5Cleaner1 import main as cleaner1
from Task5Cleaner2 import main as cleaner2
from Task5Cleaner3 import main as cleaner3
from Task5Cleaner4 import main as cleaner4
"""
import Task5Cleaner1,Task5Cleaner2,Task5Cleaner3,Task5Cleaner4
import concurrent.futures

x_value=0
y_value=0
deg=0

number_of_robots=0

def posecallback(pose_message):
    global x_value,y_value,deg
    x_value=pose_message.x
    y_value=pose_message.y
    deg=pose_message.theta 


def main():

    rospy.init_node('Turtlesim_Vaccum_cleaner',anonymous=True)

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

    rospy.spin()
"""
def forward(value,turtlename):
    twist=Twist()
    twist.linear.x=value
    turtlename.publish(twist)
    rospy.sleep(2)

def rotate_deg(rotate):
    global x_value,y_value
    rospy.wait_for_service('turtle1/teleport_absolute')
    tele_turtle = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    tele_turtle(x_value,y_value,rotate)
    rospy.sleep(1)
"""
def kill():
    rospy.wait_for_service('kill')
    kill_turtle = rospy.ServiceProxy('kill', Kill)
    kill_turtle("turtle1")

def spawn(x,y,name):
    rospy.wait_for_service('spawn')
    add_turtle = rospy.ServiceProxy('spawn', Spawn)
    add_turtle(x,y,0,name)
    rospy.Publisher(f'/{name}/cmd_vel',Twist,queue_size=10)
    
def func_reset():
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()       

def Run_robots():
    kill()
    
    spawn(0.5,0.5,"turtle1")
    spawn(6,0.5,"turtle2")
    spawn(0.5,6,"turtle3")
    spawn(6,6,"turtle4")
    
    # Create a ThreadPoolExecutor to run functions concurrently - took from google
    with concurrent.futures.ThreadPoolExecutor() as executor:
      
        executor.submit(Task5Cleaner1.main)
        executor.submit(Task5Cleaner2.main)
        executor.submit(Task5Cleaner3.main)
        executor.submit(Task5Cleaner4.main)
       
    """
    Task5Cleaner1.main()
    Task5Cleaner2.main()
    Task5Cleaner3.main()
    Task5Cleaner4.main()
     """ 
    rospy.sleep(2)


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

        self.comboBox.currentIndexChanged.connect(self.number_of_cleaners)
        self.pushButton_3.clicked.connect(Run_robots)
        self.pushButton_5.clicked.connect(func_reset)

    def number_of_cleaners(self,index):
        global number_of_robots
        if index==0:
            number_of_robots=4
        


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
    
