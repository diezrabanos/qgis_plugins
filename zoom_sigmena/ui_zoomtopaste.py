# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_zoomtopaste.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_zoomtopaste(object):
    def setupUi(self, zoomtopaste):
        zoomtopaste.setObjectName("zoomtopaste")
        zoomtopaste.resize(453, 142)
        self.buttonBox = QtWidgets.QDialogButtonBox(zoomtopaste)
        self.buttonBox.setGeometry(QtCore.QRect(270, 110, 176, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(zoomtopaste)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 35, 435, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.hboxlayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)
        self.xCoord = QtWidgets.QLineEdit(self.layoutWidget)
        self.xCoord.setObjectName("xCoord")
        self.hboxlayout.addWidget(self.xCoord)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)
        self.yCoord = QtWidgets.QLineEdit(self.layoutWidget)
        self.yCoord.setObjectName("yCoord")
        self.hboxlayout.addWidget(self.yCoord)
        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        #self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        #self.label_3.setObjectName("label_3")
        #self.gridlayout.addWidget(self.label_3, 0, 0, 1, 1)
        #self.spinBoxScale = QtWidgets.QSpinBox(self.layoutWidget)
        #self.spinBoxScale.setObjectName("spinBoxScale")
        #self.gridlayout.addWidget(self.spinBoxScale, 0, 1, 1, 1)
        self.hboxlayout.addLayout(self.gridlayout)
        self.ChkOverClippboard = QtWidgets.QLabel(zoomtopaste)
        self.ChkOverClippboard.setGeometry(QtCore.QRect(9, 9, 181, 20))
        self.ChkOverClippboard.setObjectName("ChkOverClippboard")
        self.label_5 = QtWidgets.QLabel(zoomtopaste)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 261, 64))
        self.label_5.setObjectName("label_5")
        #self.checkBox = QtWidgets.QCheckBox(zoomtopaste)
        #self.checkBox.setGeometry(QtCore.QRect(290, 90, 151, 20))
        #self.checkBox.setChecked(False)
        #self.checkBox.setObjectName("checkBox")

        self.retranslateUi(zoomtopaste)
        self.buttonBox.accepted.connect(zoomtopaste.accept)
        self.buttonBox.rejected.connect(zoomtopaste.reject)
        QtCore.QMetaObject.connectSlotsByName(zoomtopaste)
        zoomtopaste.setTabOrder(self.xCoord, self.yCoord)
        #zoomtopaste.setTabOrder(self.yCoord, self.spinBoxScale)
        zoomtopaste.setTabOrder(self.yCoord, self.buttonBox)

    def retranslateUi(self, zoomtopaste):
        _translate = QtCore.QCoreApplication.translate
        zoomtopaste.setWindowTitle(_translate("zoomtopaste", "Zoom to Paste"))
        self.label.setText(_translate("zoomtopaste", "X"))
        self.label_2.setText(_translate("zoomtopaste", "Y"))
        #self.label_3.setText(_translate("zoomtopaste", "Scale view by"))
        self.ChkOverClippboard.setText(_translate("zoomtopaste", "Zoom to Point"))
        self.label_5.setText(_translate("zoomtopaste", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal; text-decoration:none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Para datos en geograficas, X es longitud e </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">Y es latitud. Para datos proyectados, mete</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"> la X e Y en las unidades adecuadas de la </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">proyeccion, metros.</p></body></html>"))
        #self.checkBox.setText(_translate("zoomtopaste", "Automaticly over Clipboard"))

