# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'howToPlay.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(811, 421)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.howToPlayHorizontalLayout = QHBoxLayout()
        self.howToPlayHorizontalLayout.setObjectName(u"howToPlayHorizontalLayout")
        self.howToPlayHorizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.howToPlayHorizontalLayout.addItem(self.horizontalSpacer)

        self.howToPlayTitleLabel = QLabel(Dialog)
        self.howToPlayTitleLabel.setObjectName(u"howToPlayTitleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.howToPlayTitleLabel.sizePolicy().hasHeightForWidth())
        self.howToPlayTitleLabel.setSizePolicy(sizePolicy)
        self.howToPlayTitleLabel.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setPointSize(24)
        self.howToPlayTitleLabel.setFont(font)
        self.howToPlayTitleLabel.setLayoutDirection(Qt.LeftToRight)

        self.howToPlayHorizontalLayout.addWidget(self.howToPlayTitleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.howToPlayHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.howToPlayReturnButton = QPushButton(Dialog)
        self.howToPlayReturnButton.setObjectName(u"howToPlayReturnButton")
        sizePolicy.setHeightForWidth(self.howToPlayReturnButton.sizePolicy().hasHeightForWidth())
        self.howToPlayReturnButton.setSizePolicy(sizePolicy)
        self.howToPlayReturnButton.setMinimumSize(QSize(200, 50))
        self.howToPlayReturnButton.setMaximumSize(QSize(200, 60))
        font1 = QFont()
        font1.setPointSize(16)
        self.howToPlayReturnButton.setFont(font1)

        self.howToPlayHorizontalLayout.addWidget(self.howToPlayReturnButton)


        self.gridLayout.addLayout(self.howToPlayHorizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 787, 291))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.howToPlayInfo = QLabel(self.scrollAreaWidgetContents)
        self.howToPlayInfo.setObjectName(u"howToPlayInfo")
        self.howToPlayInfo.setMinimumSize(QSize(0, 250))
        self.howToPlayInfo.setSizeIncrement(QSize(1000, 1000))
        self.howToPlayInfo.setBaseSize(QSize(500, 500))
        font2 = QFont()
        font2.setPointSize(10)
        self.howToPlayInfo.setFont(font2)
        self.howToPlayInfo.setAutoFillBackground(False)
        self.howToPlayInfo.setFrameShape(QFrame.Box)
        self.howToPlayInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.howToPlayInfo.setWordWrap(True)

        self.gridLayout_2.addWidget(self.howToPlayInfo, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.howToPlayTitleLabel.setText(QCoreApplication.translate("Dialog", u"How To Play", None))
        self.howToPlayReturnButton.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.howToPlayInfo.setText(QCoreApplication.translate("Dialog", u"Explain how the game is played here example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text e"
                        "xample text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text example text ", None))
    # retranslateUi

