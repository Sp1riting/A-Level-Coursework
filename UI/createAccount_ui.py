# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createAccount.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreateAccountWindow(object):
    def setupUi(self, CreateAccountWindow):
        if not CreateAccountWindow.objectName():
            CreateAccountWindow.setObjectName(u"CreateAccountWindow")
        CreateAccountWindow.resize(1088, 582)
        self.verticalLayout = QVBoxLayout(CreateAccountWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.accountTitleLabel = QLabel(CreateAccountWindow)
        self.accountTitleLabel.setObjectName(u"accountTitleLabel")
        font = QFont()
        font.setPointSize(29)
        self.accountTitleLabel.setFont(font)
        self.accountTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.accountTitleLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.accountUsernameLabel = QLabel(CreateAccountWindow)
        self.accountUsernameLabel.setObjectName(u"accountUsernameLabel")
        font1 = QFont()
        font1.setPointSize(16)
        self.accountUsernameLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.accountUsernameLabel)

        self.accountUsernameInput = QLineEdit(CreateAccountWindow)
        self.accountUsernameInput.setObjectName(u"accountUsernameInput")
        self.accountUsernameInput.setMinimumSize(QSize(0, 40))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.accountUsernameInput)

        self.accountPasswordLabel = QLabel(CreateAccountWindow)
        self.accountPasswordLabel.setObjectName(u"accountPasswordLabel")
        self.accountPasswordLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.accountPasswordLabel)

        self.accountPasswordInput = QLineEdit(CreateAccountWindow)
        self.accountPasswordInput.setObjectName(u"accountPasswordInput")
        self.accountPasswordInput.setMinimumSize(QSize(0, 40))
        self.accountPasswordInput.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.accountPasswordInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.createErrorLabel = QLabel(CreateAccountWindow)
        self.createErrorLabel.setObjectName(u"createErrorLabel")
        self.createErrorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.createErrorLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.createAccountButton = QPushButton(CreateAccountWindow)
        self.createAccountButton.setObjectName(u"createAccountButton")
        self.createAccountButton.setMinimumSize(QSize(300, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.createAccountButton.setFont(font2)

        self.horizontalLayout.addWidget(self.createAccountButton)

        self.createReturnButton = QPushButton(CreateAccountWindow)
        self.createReturnButton.setObjectName(u"createReturnButton")
        self.createReturnButton.setMinimumSize(QSize(300, 50))
        self.createReturnButton.setFont(font2)

        self.horizontalLayout.addWidget(self.createReturnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CreateAccountWindow)

        QMetaObject.connectSlotsByName(CreateAccountWindow)
    # setupUi

    def retranslateUi(self, CreateAccountWindow):
        CreateAccountWindow.setWindowTitle(QCoreApplication.translate("CreateAccountWindow", u"Create New Account", None))
        self.accountTitleLabel.setText(QCoreApplication.translate("CreateAccountWindow", u"Create New Account", None))
        self.accountUsernameLabel.setText(QCoreApplication.translate("CreateAccountWindow", u"Username:", None))
        self.accountPasswordLabel.setText(QCoreApplication.translate("CreateAccountWindow", u"Password:", None))
        self.createErrorLabel.setText("")
        self.createAccountButton.setText(QCoreApplication.translate("CreateAccountWindow", u"Create", None))
        self.createReturnButton.setText(QCoreApplication.translate("CreateAccountWindow", u"Return", None))
    # retranslateUi

