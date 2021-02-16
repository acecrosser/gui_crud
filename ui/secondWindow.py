# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secondWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(417, 302)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 397, 282))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.titleLine = QLineEdit(self.widget)
        self.titleLine.setObjectName(u"titleLine")

        self.gridLayout.addWidget(self.titleLine, 0, 1, 1, 1)

        self.saveButton = QPushButton(self.widget)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.priceLine = QDoubleSpinBox(self.widget)
        self.priceLine.setObjectName(u"priceLine")

        self.gridLayout.addWidget(self.priceLine, 1, 1, 1, 1)

        self.cancelButton = QPushButton(self.widget)
        self.cancelButton.setObjectName(u"cancelButton")

        self.gridLayout.addWidget(self.cancelButton, 1, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.linkLine = QLineEdit(self.widget)
        self.linkLine.setObjectName(u"linkLine")

        self.gridLayout.addWidget(self.linkLine, 2, 1, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.textArea = QTextEdit(self.widget)
        self.textArea.setObjectName(u"textArea")

        self.gridLayout.addWidget(self.textArea, 3, 1, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"\u0417\u044b\u043a\u0440\u044b\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u0441\u044b\u043b\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442", None))
    # retranslateUi

