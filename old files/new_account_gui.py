# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_account.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1150, 500)
        Form.setMinimumSize(QtCore.QSize(1150, 500))
        Form.setMaximumSize(QtCore.QSize(1150, 500))
        Form.setStyleSheet("background-color: white")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1150, 50))
        self.label.setStyleSheet("background-color: rgb(57, 24, 71)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 290, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.pw2 = QtWidgets.QLineEdit(Form)
        self.pw2.setGeometry(QtCore.QRect(770, 310, 250, 31))
        self.pw2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.pw2.setText("")
        self.pw2.setObjectName("pw2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(770, 110, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_12.setObjectName("label_12")
        self.dob = QtWidgets.QLineEdit(Form)
        self.dob.setGeometry(QtCore.QRect(770, 130, 250, 31))
        self.dob.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.dob.setObjectName("dob")
        self.pw1 = QtWidgets.QLineEdit(Form)
        self.pw1.setGeometry(QtCore.QRect(770, 220, 250, 31))
        self.pw1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.pw1.setText("")
        self.pw1.setObjectName("pw1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.phone = QtWidgets.QLineEdit(Form)
        self.phone.setGeometry(QtCore.QRect(110, 310, 250, 31))
        self.phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.phone.setInputMask("")
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(230, 290, 55, 16))
        self.label_14.setStyleSheet("color: red;\n"
"font: 63 6pt \"Montserrat Italic\";")
        self.label_14.setObjectName("label_14")
        self.f_name = QtWidgets.QLineEdit(Form)
        self.f_name.setGeometry(QtCore.QRect(110, 130, 250, 31))
        self.f_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.f_name.setObjectName("f_name")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(440, 110, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(770, 200, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_11.setObjectName("label_11")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(440, 200, 191, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_10.setObjectName("label_10")
        self.state = QtWidgets.QLineEdit(Form)
        self.state.setGeometry(QtCore.QRect(440, 310, 250, 31))
        self.state.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.state.setText("")
        self.state.setMaxLength(2)
        self.state.setObjectName("state")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(770, 290, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_13.setObjectName("label_13")
        self.street = QtWidgets.QLineEdit(Form)
        self.street.setGeometry(QtCore.QRect(440, 130, 250, 31))
        self.street.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.street.setObjectName("street")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(440, 290, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        font.setKerning(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(57, 24, 71);\n"
"font: 63 8pt \"Montserrat SemiBold\";\n"
"")
        self.label_9.setObjectName("label_9")
        self.login_b = QtWidgets.QPushButton(Form)
        self.login_b.setGeometry(QtCore.QRect(110, 380, 911, 41))
        self.login_b.setStyleSheet("background-color: rgb(180, 145, 76);\n"
"font: 12pt \"Montserrat SemiBold\";\n"
"color: white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 5px;")
        self.login_b.setObjectName("login_b")
        self.city = QtWidgets.QLineEdit(Form)
        self.city.setGeometry(QtCore.QRect(440, 220, 250, 31))
        self.city.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.city.setText("")
        self.city.setObjectName("city")
        self.l_name = QtWidgets.QLineEdit(Form)
        self.l_name.setGeometry(QtCore.QRect(110, 220, 250, 31))
        self.l_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: outset;\n"
"border-color: grey;\n"
"border-width: 1px;\n"
"border-radius: 5px;")
        self.l_name.setText("")
        self.l_name.setObjectName("l_name")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "PHONE NUMBER"))
        self.label_3.setText(_translate("Form", "LAST NAME"))
        self.label_12.setText(_translate("Form", "DATE OF BIRTH"))
        self.label_2.setText(_translate("Form", "FIRST NAME"))
        self.label_14.setText(_translate("Form", "*optional"))
        self.label_4.setText(_translate("Form", "STREET ADDRESS"))
        self.label_11.setText(_translate("Form", "ENTER PASSWORD"))
        self.label_10.setText(_translate("Form", "CITY"))
        self.label_13.setText(_translate("Form", "CONFIRM PASSWORD"))
        self.label_9.setText(_translate("Form", "STATE"))
        self.login_b.setText(_translate("Form", "CREATE ACCOUNT"))
