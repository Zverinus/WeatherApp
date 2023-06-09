# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alternativeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AlternativeDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(537, 393)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(537, 393))
        Dialog.setMaximumSize(QtCore.QSize(537, 393))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.placeName = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.placeName.setFont(font)
        self.placeName.setObjectName("placeName")
        self.verticalLayout_3.addWidget(self.placeName)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.latSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.latSpinBox.setFont(font)
        self.latSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.latSpinBox.setDecimals(7)
        self.latSpinBox.setMinimum(-90.0)
        self.latSpinBox.setMaximum(90.0)
        self.latSpinBox.setObjectName("latSpinBox")
        self.verticalLayout.addWidget(self.latSpinBox)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lonSpinBox = QtWidgets.QDoubleSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lonSpinBox.setFont(font)
        self.lonSpinBox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.lonSpinBox.setDecimals(7)
        self.lonSpinBox.setMinimum(-180.0)
        self.lonSpinBox.setMaximum(180.0)
        self.lonSpinBox.setObjectName("lonSpinBox")
        self.verticalLayout_2.addWidget(self.lonSpinBox)
        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        self.finishAddingButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finishAddingButton.sizePolicy().hasHeightForWidth())
        self.finishAddingButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.finishAddingButton.setFont(font)
        self.finishAddingButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.finishAddingButton.setObjectName("finishAddingButton")
        self.gridLayout.addWidget(self.finishAddingButton, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавление места по координатам"))
        self.label_4.setText(_translate("Dialog", "Название:"))
        self.label_2.setText(_translate("Dialog", "Широта в градусах (от -90 до 90):"))
        self.label_3.setText(_translate("Dialog", "Долгота в градусах (от -180 до 180):"))
        self.finishAddingButton.setText(_translate("Dialog", "Добавить"))
