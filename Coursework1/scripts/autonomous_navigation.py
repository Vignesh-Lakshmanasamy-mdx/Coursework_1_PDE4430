#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_srvs.srv import Empty
from turtlesim.srv import Kill,Spawn
import sys,math

x_value=0
y_value=0
deg=0
x_t=0
y_t=0
theta_t=0

def posecallback(pose_message):
    global x_value,y_value,deg
    x_value=pose_message.x
    y_value=pose_message.y
    deg=pose_message.theta 

def main():

    rospy.init_node('Turtlesim_autonomous_navigation',anonymous=True)

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

def kill():
    rospy.wait_for_service('kill')
    kill_turtle = rospy.ServiceProxy('kill', Kill)
    kill_turtle("turtle1")

def spawn(x,y,deg):
    deg=deg*3.14/180
    rospy.wait_for_service('spawn')
    add_turtle = rospy.ServiceProxy('spawn', Spawn)
    add_turtle(x,y,deg,"turtle1")

def turtle_origin_points(x_origin,y_origin,theta_origin):
    if x_origin<1 or x_origin>10:
        x_origin=5.54
    if y_origin<1 or y_origin>10:
        y_origin=5.54
    if theta_origin<0 or theta_origin>360:
        theta_origin=0
    print(x_origin,y_origin,theta_origin)
    kill()
    spawn(x_origin,y_origin,theta_origin)

def turtle_target_points(x_target,y_target,theta_target):
    
    global x_t,y_t,theta_t
    if x_target<1 or x_target>10:
        x_target=2
    if y_target<1 or y_target>10:
        y_target=2
    if theta_target<0 or theta_target>360:
        theta_target=0.0
    
    x_t=x_target
    y_t=y_target
    theta_t=theta_target

def target_distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def target_angle(x1,y1,x2,y2):
    return math.atan2(y2-y1,x2-x1)

def move_turtle():

    global x_t,y_t,theta_t,x_value,y_value,deg
    twist=Twist()
    rate=rospy.Rate(10)
    """
    #triangle side 1
    side1=abs(x_t-x_value)
    side2=abs(y_t-y_value)
    side3=math.sqrt(side1**2+side2**2)
    angle=math.degrees(math.atan(side2/side1))
    angle=angle*0.0174533
    print(side3,angle)
    """
    
    while not rospy.is_shutdown():
        angle=target_angle(x_value,y_value,x_t,y_t)

        theta_diff=angle-deg
        theta_diff=(theta_diff+math.pi)%(2*math.pi)-math.pi
        
        
        if abs(theta_diff)>0.1:  
            twist.angular.z=0.5*theta_diff/abs(theta_diff)
            twist.linear.x=0.0
            cmd_vel_pub.publish(twist)
        else:
            twist.angular.z=0.0

            distance=target_distance(x_value,y_value,x_t,y_t)
            if distance>0.1:
                twist.linear.x=3.0
                cmd_vel_pub.publish(twist)
            else:
                twist.linear.x=0.0
                cmd_vel_pub.publish(twist)
                break
        rate.sleep()
    

    angle_on_reach_point=theta_t*0.01744
    theta_diff=angle_on_reach_point-deg
    theta_diff=(theta_diff+math.pi)%(2*math.pi)-math.pi

    while abs(theta_diff)>0.1:
        twist.angular.z=0.5*theta_diff/abs(theta_diff)
        cmd_vel_pub.publish(twist)
        theta_diff=(theta_t*0.01744)-deg
        theta_diff=(theta_diff+math.pi)%(2*math.pi)-math.pi
        rate.sleep()
    
    twist.angular.z=0.0
    cmd_vel_pub.publish(twist)

    print(x_value,y_value,(deg*180/3.14))

def turtle_reset():
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()

# Form implementation generated from reading ui file 'Task2.ui'
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

        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(20, 30, 601, 81))
        self.textBrowser_5.setObjectName("textBrowser_5")

        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 130, 601, 301))
        self.textEdit_3.setObjectName("textEdit_3")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 210, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setObjectName("label_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(210, 170, 191, 191))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(410, 170, 191, 191))
        self.textEdit_5.setObjectName("textEdit_5")

        self.origin_x = QtWidgets.QTextEdit(Dialog)
        self.origin_x.setGeometry(QtCore.QRect(220, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.origin_x.setFont(font)
        self.origin_x.setObjectName("origin_x")
        self.Origin_y = QtWidgets.QTextEdit(Dialog)
        self.Origin_y.setGeometry(QtCore.QRect(220, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Origin_y.setFont(font)
        self.Origin_y.setObjectName("Origin_y")
        
        self.origin_theta = QtWidgets.QTextEdit(Dialog)
        self.origin_theta.setGeometry(QtCore.QRect(220, 310, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.origin_theta.setFont(font)
        self.origin_theta.setObjectName("origin_theta")
        
        self.Target_Theta = QtWidgets.QTextEdit(Dialog)
        self.Target_Theta.setGeometry(QtCore.QRect(420, 310, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Target_Theta.setFont(font)
        self.Target_Theta.setObjectName("Target_Theta")
        
        self.Target_x = QtWidgets.QTextEdit(Dialog)
        self.Target_x.setGeometry(QtCore.QRect(420, 210, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Target_x.setFont(font)
        self.Target_x.setObjectName("Target_x")
        
        self.Target_y = QtWidgets.QTextEdit(Dialog)
        self.Target_y.setGeometry(QtCore.QRect(420, 260, 171, 31))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Target_y.setFont(font)
        self.Target_y.setObjectName("Target_y")
        
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 135, 561, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.turtle_spawn = QtWidgets.QPushButton(Dialog)
        self.turtle_spawn.setGeometry(QtCore.QRect(30, 380, 171, 25))
        self.turtle_spawn.setObjectName("Spawn_new_turtle")        
        
        self.move_to_target = QtWidgets.QPushButton(Dialog)
        self.move_to_target.setGeometry(QtCore.QRect(220, 380, 171, 25))
        self.move_to_target.setObjectName("move_to_target")
        
        self.Rest_turtle = QtWidgets.QPushButton(Dialog)
        self.Rest_turtle.setGeometry(QtCore.QRect(420, 380, 171, 25))
        self.Rest_turtle.setObjectName("Rest_turtle")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.turtle_spawn.clicked.connect(self.accept_values)
        self.move_to_target.clicked.connect(self.Turtle_target_motion)
        self.Rest_turtle.clicked.connect(turtle_reset)
    def accept_values(self):
        try :
            x_origin=float(self.origin_x.toPlainText())
            y_origin=float(self.Origin_y.toPlainText())
            theta_origin=float(self.origin_theta.toPlainText())
            
            turtle_origin_points(x_origin,y_origin,theta_origin)
            
            x_target=float(self.Target_x.toPlainText())
            y_target=float(self.Target_y.toPlainText())
            theta_target=float(self.Target_Theta.toPlainText())
            
            turtle_target_points(x_target,y_target,theta_target)
        except:
            print("Enter a Valid Data")

    def Turtle_target_motion(self):
        try:
            move_turtle()
        except:
            print("invalid operation")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">PDE4430 - Mobile Robotics</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Coursework 1 -  Task 2</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#4e9a06;\">Autonomous navigation to any given coordinate in the Turtlesim window</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Dialog", "X coordinate point"))
        self.label_2.setText(_translate("Dialog", "Y coordinate point"))
        self.label_3.setText(_translate("Dialog", "Theta Value (Deg.)"))
        self.textEdit_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Turtle Origin Coordinates</p></body></html>"))
        self.textEdit_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Turtle Target Coordinates</p></body></html>"))
        self.origin_x.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400;\"><br /></p></body></html>"))
        self.Origin_y.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400;\"><br /></p></body></html>"))
        self.origin_theta.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400;\"><br /></p></body></html>"))
        self.Target_Theta.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400;\"><br /></p></body></html>"))
        self.Target_x.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400;\"><br /></p></body></html>"))
        self.Target_y.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'URW Bookman\'; font-size:11pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-weight:400;\"><br /></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enter X &amp; Y coordinate value Between 1 &amp; 10</p></body></html>"))
        self.move_to_target.setText(_translate("Dialog", "Move to Target"))
        self.Rest_turtle.setText(_translate("Dialog", "Reset Turtle Window"))
        self.turtle_spawn.setText(_translate("Dialog", "Spawn"))

if __name__ == "__main__":
    
    main()