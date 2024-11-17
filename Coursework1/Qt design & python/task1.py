# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task1.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.textBrowser.setGeometry(QtCore.QRect(20, 40, 601, 81))
        self.textBrowser.setObjectName("textBrowser")

        self.Vel_control = QtWidgets.QSlider(Dialog)
        self.Vel_control.setGeometry(QtCore.QRect(490, 150, 51, 221))
        self.Vel_control.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Vel_control.setMaximum(10)
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

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(270, 140, 181, 111))
        self.textEdit.setObjectName("textEdit")

        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(280, 160, 151, 23))
        self.checkBox.setObjectName("checkBox")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 200, 151, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 280, 181, 51))
        self.pushButton_4.setObjectName("pushButton_4")

        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(470, 380, 161, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")

        self.lcdNumberDegree = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumberDegree.setGeometry(QtCore.QRect(100, 240, 51, 41))
        self.lcdNumberDegree.setObjectName("lcdNumberDegree")

        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(470, 140, 161, 241))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(560, 340, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")

        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(280, 360, 151, 23))
        self.checkBox_2.setObjectName("checkBox_2")

        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(270, 350, 181, 41))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textBrowser_3.raise_()
        self.textEdit_2.raise_()
        self.buttonBox.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.textBrowser.raise_()
        self.Vel_control.raise_()
        self.direction_control.raise_()
        self.textBrowser_2.raise_()
        self.textEdit.raise_()
        self.checkBox.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.textBrowser_4.raise_()
        self.lcdNumberDegree.raise_()
        self.lcdNumber_2.raise_()
        self.checkBox_2.raise_()

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Direction control</p></body></html>"))
        self.checkBox.setText(_translate("Dialog", "Continuous motion"))
        self.pushButton_3.setText(_translate("Dialog", "Stop"))
        self.pushButton_4.setText(_translate("Dialog", "Reset Turtle Window"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Speed control</p></body></html>"))
        self.checkBox_2.setText(_translate("Dialog", "Wall Collision"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
