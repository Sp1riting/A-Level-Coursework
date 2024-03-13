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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreateAccountWindow(object):
    def setupUi(self, CreateAccountWindow):
        if not CreateAccountWindow.objectName():
            CreateAccountWindow.setObjectName(u"CreateAccountWindow")
        CreateAccountWindow.resize(753, 399)
        self.verticalLayout = QVBoxLayout(CreateAccountWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loginTitleLabel = QLabel(CreateAccountWindow)
        self.loginTitleLabel.setObjectName(u"loginTitleLabel")
        font = QFont()
        font.setPointSize(29)
        self.loginTitleLabel.setFont(font)
        self.loginTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.loginTitleLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.usernameLabel = QLabel(CreateAccountWindow)
        self.usernameLabel.setObjectName(u"usernameLabel")
        font1 = QFont()
        font1.setPointSize(16)
        self.usernameLabel.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.usernameLabel)

        self.loginUsernameInput = QLineEdit(CreateAccountWindow)
        self.loginUsernameInput.setObjectName(u"loginUsernameInput")
        self.loginUsernameInput.setMinimumSize(QSize(0, 40))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.loginUsernameInput)

        self.passwordLabel = QLabel(CreateAccountWindow)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.passwordLabel)

        self.loginPasswordInput = QLineEdit(CreateAccountWindow)
        self.loginPasswordInput.setObjectName(u"loginPasswordInput")
        self.loginPasswordInput.setMinimumSize(QSize(0, 40))
        self.loginPasswordInput.setSizeIncrement(QSize(0, 0))
        self.loginPasswordInput.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.loginPasswordInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.loginErrorLabel = QLabel(CreateAccountWindow)
        self.loginErrorLabel.setObjectName(u"loginErrorLabel")
        self.loginErrorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.loginErrorLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.loginButton = QPushButton(CreateAccountWindow)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMinimumSize(QSize(300, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.loginButton.setFont(font2)

        self.horizontalLayout.addWidget(self.loginButton)

        self.loginReturnButton = QPushButton(CreateAccountWindow)
        self.loginReturnButton.setObjectName(u"loginReturnButton")
        self.loginReturnButton.setMinimumSize(QSize(300, 50))
        self.loginReturnButton.setFont(font2)

        self.horizontalLayout.addWidget(self.loginReturnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CreateAccountWindow)

        QMetaObject.connectSlotsByName(CreateAccountWindow)
    # setupUi

    def retranslateUi(self, CreateAccountWindow):
        CreateAccountWindow.setWindowTitle(QCoreApplication.translate("CreateAccountWindow", u"Create New Account", None))
        self.loginTitleLabel.setText(QCoreApplication.translate("CreateAccountWindow", u"Welcome! Please Login", None))
        self.usernameLabel.setText(QCoreApplication.translate("CreateAccountWindow", u"Username:", None))
        self.passwordLabel.setText(QCoreApplication.translate("CreateAccountWindow", u"Password:", None))
        self.loginErrorLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("CreateAccountWindow", u"Login", None))
        self.loginReturnButton.setText(QCoreApplication.translate("CreateAccountWindow", u"Return", None))
    # retranslateUi

