# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photo.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 559)
        MainWindow.setStyleSheet("background-color: rgb(250, 255, 255);\n"
"background-color: rgb(253, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 591, 451))
        self.label.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 161, 31))
        self.pushButton.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"color: rgb(0, 56, 62);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 490, 111, 23))
        self.pushButton_2.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 56, 62);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 161, 451))
        self.listWidget.setStyleSheet("background-color: rgb(242, 255, 255);")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 490, 111, 23))
        self.pushButton_3.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 56, 62);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(310, 490, 111, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 56, 62);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(550, 490, 111, 23))
        self.pushButton_6.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 56, 62);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(670, 490, 111, 23))
        self.pushButton_7.setStyleSheet("background-color: rgb(242, 255, 255);\n"
"font: 63 10pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 56, 62);")
        self.pushButton_7.setObjectName("pushButton_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "картинка"))
        self.pushButton.setText(_translate("MainWindow", "Папка"))
        self.pushButton_2.setText(_translate("MainWindow", "Вліво"))
        self.pushButton_3.setText(_translate("MainWindow", "Дзеркало"))
        self.pushButton_4.setText(_translate("MainWindow", "Вправо"))
        self.pushButton_6.setText(_translate("MainWindow", "Різкість"))
        self.pushButton_7.setText(_translate("MainWindow", "Ч/Б"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
