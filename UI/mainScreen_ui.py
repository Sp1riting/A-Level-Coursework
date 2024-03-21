# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainScreen.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 582)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.initialTitleLabel = QLabel(self.centralwidget)
        self.initialTitleLabel.setObjectName(u"initialTitleLabel")
        font = QFont()
        font.setPointSize(40)
        font.setBold(True)
        self.initialTitleLabel.setFont(font)
        self.initialTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.initialTitleLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.openLoginButton = QPushButton(self.centralwidget)
        self.openLoginButton.setObjectName(u"openLoginButton")
        self.openLoginButton.setMinimumSize(QSize(300, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.openLoginButton.setFont(font1)

        self.horizontalLayout.addWidget(self.openLoginButton)

        self.openCreateAccountButton = QPushButton(self.centralwidget)
        self.openCreateAccountButton.setObjectName(u"openCreateAccountButton")
        self.openCreateAccountButton.setMinimumSize(QSize(300, 50))
        self.openCreateAccountButton.setFont(font1)

        self.horizontalLayout.addWidget(self.openCreateAccountButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Zooopoly", None))
        self.initialTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Zooopoly", None))
        self.openLoginButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.openCreateAccountButton.setText(QCoreApplication.translate("MainWindow", u"Create new account", None))
    # retranslateUi

