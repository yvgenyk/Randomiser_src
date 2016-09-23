# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_design.ui'
#
# Created: Fri Sep 23 21:43:55 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(315, 225)
        Form.setMinimumSize(QtCore.QSize(315, 225))
        Form.setMaximumSize(QtCore.QSize(315, 225))
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 312, 218))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.loadLable = QtGui.QLabel(self.verticalLayoutWidget)
        self.loadLable.setMinimumSize(QtCore.QSize(150, 30))
        self.loadLable.setMaximumSize(QtCore.QSize(150, 30))
        self.loadLable.setText(_fromUtf8(""))
        self.loadLable.setObjectName(_fromUtf8("loadLable"))
        self.horizontalLayout.addWidget(self.loadLable)
        self.loadBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.loadBtn.setMinimumSize(QtCore.QSize(150, 30))
        self.loadBtn.setMaximumSize(QtCore.QSize(150, 30))
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.horizontalLayout.addWidget(self.loadBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(150, 30))
        self.label.setMaximumSize(QtCore.QSize(150, 30))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.newFileName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.newFileName.setMinimumSize(QtCore.QSize(150, 30))
        self.newFileName.setMaximumSize(QtCore.QSize(150, 30))
        self.newFileName.setObjectName(_fromUtf8("newFileName"))
        self.horizontalLayout_2.addWidget(self.newFileName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(150, 30))
        self.label_2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.psrLine = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.psrLine.setMinimumSize(QtCore.QSize(150, 30))
        self.psrLine.setMaximumSize(QtCore.QSize(150, 30))
        self.psrLine.setObjectName(_fromUtf8("psrLine"))
        self.horizontalLayout_3.addWidget(self.psrLine)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.startBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.startBtn.setMinimumSize(QtCore.QSize(310, 30))
        self.startBtn.setMaximumSize(QtCore.QSize(310, 30))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.verticalLayout.addWidget(self.startBtn)
        self.delBtn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.delBtn.setMinimumSize(QtCore.QSize(310, 30))
        self.delBtn.setMaximumSize(QtCore.QSize(310, 30))
        self.delBtn.setObjectName(_fromUtf8("delBtn"))
        self.verticalLayout.addWidget(self.delBtn)
        self.statusLable = QtGui.QLabel(self.verticalLayoutWidget)
        self.statusLable.setMinimumSize(QtCore.QSize(310, 30))
        self.statusLable.setMaximumSize(QtCore.QSize(310, 30))
        self.statusLable.setText(_fromUtf8(""))
        self.statusLable.setObjectName(_fromUtf8("statusLable"))
        self.verticalLayout.addWidget(self.statusLable)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Randomise", None))
        self.loadBtn.setText(_translate("Form", "Load File", None))
        self.label.setText(_translate("Form", "New File Name:", None))
        self.label_2.setText(_translate("Form", "Enter % number of strings:", None))
        self.startBtn.setText(_translate("Form", "Start", None))
        self.delBtn.setText(_translate("Form", "Delete New Lines", None))

