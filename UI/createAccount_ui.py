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
        CreateAccountWindow.resize(789, 449)
        self.verticalLayout = QVBoxLayout(CreateAccountWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CreateAccountWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(29)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(CreateAccountWindow)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.usernameInput = QLineEdit(CreateAccountWindow)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMinimumSize(QSize(0, 40))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.usernameInput)

        self.label_3 = QLabel(CreateAccountWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.passwordInput = QLineEdit(CreateAccountWindow)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(0, 40))
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.passwordInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.errorLabel = QLabel(CreateAccountWindow)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.errorLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.createButton = QPushButton(CreateAccountWindow)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setMinimumSize(QSize(300, 50))
        font2 = QFont()
        font2.setPointSize(12)
        self.createButton.setFont(font2)

        self.horizontalLayout.addWidget(self.createButton)

        self.returnButton = QPushButton(CreateAccountWindow)
        self.returnButton.setObjectName(u"returnButton")
        self.returnButton.setMinimumSize(QSize(300, 50))
        self.returnButton.setFont(font2)

        self.horizontalLayout.addWidget(self.returnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CreateAccountWindow)

        QMetaObject.connectSlotsByName(CreateAccountWindow)
    # setupUi

    def retranslateUi(self, CreateAccountWindow):
        CreateAccountWindow.setWindowTitle(QCoreApplication.translate("CreateAccountWindow", u"Create New Account", None))
        self.label.setText(QCoreApplication.translate("CreateAccountWindow", u"Create New Account", None))
        self.label_2.setText(QCoreApplication.translate("CreateAccountWindow", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("CreateAccountWindow", u"Password:", None))
        self.errorLabel.setText("")
        self.createButton.setText(QCoreApplication.translate("CreateAccountWindow", u"Create", None))
        self.returnButton.setText(QCoreApplication.translate("CreateAccountWindow", u"Return", None))
    # retranslateUi

