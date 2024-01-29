# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import Icons_rc

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(1170, 579)
        font = QFont()
        font.setPointSize(12)
        w_LoginForm.setFont(font)
        w_LoginForm.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.le_UserID = QLineEdit(self.groupBox)
        self.le_UserID.setObjectName(u"le_UserID")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_UserID)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_Password)

        self.verticalSpacer = QSpacerItem(20, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.FieldRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.pb_Cancel = QPushButton(w_LoginForm)
        self.pb_Cancel.setObjectName(u"pb_Cancel")

        self.gridLayout.addWidget(self.pb_Cancel, 3, 1, 1, 1)

        self.pb_Ok = QPushButton(w_LoginForm)
        self.pb_Ok.setObjectName(u"pb_Ok")

        self.gridLayout.addWidget(self.pb_Ok, 3, 0, 1, 1)

        self.lbl_Message = QLabel(w_LoginForm)
        self.lbl_Message.setObjectName(u"lbl_Message")

        self.gridLayout.addWidget(self.lbl_Message, 4, 0, 1, 1)

        self.label_4 = QLabel(w_LoginForm)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)


        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"Login Screen", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Welcome! Please Login", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"User ID:", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"Password:", None))
        self.pb_Cancel.setText(QCoreApplication.translate("w_LoginForm", u"Cancel", None))
        self.pb_Ok.setText(QCoreApplication.translate("w_LoginForm", u"Ok", None))
        self.lbl_Message.setText(QCoreApplication.translate("w_LoginForm", u"Message", None))
        self.label_4.setText(QCoreApplication.translate("w_LoginForm", u"TextLabel", None))
    # retranslateUi

