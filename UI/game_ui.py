# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import Icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1320, 1277)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.boardImageLabel = QLabel(self.groupBox)
        self.boardImageLabel.setObjectName(u"boardImageLabel")
        self.boardImageLabel.setGeometry(QRect(0, 0, 1151, 1161))
        self.endTurnButton = QPushButton(self.groupBox)
        self.endTurnButton.setObjectName(u"endTurnButton")
        self.endTurnButton.setGeometry(QRect(330, 540, 231, 121))
        font1 = QFont()
        font1.setPointSize(24)
        self.endTurnButton.setFont(font1)
        self.bankruptButton = QPushButton(self.groupBox)
        self.bankruptButton.setObjectName(u"bankruptButton")
        self.bankruptButton.setGeometry(QRect(610, 540, 221, 121))
        self.bankruptButton.setFont(font1)
        self.displayLabel = QLabel(self.groupBox)
        self.displayLabel.setObjectName(u"displayLabel")
        self.displayLabel.setGeometry(QRect(210, 880, 731, 71))
        self.displayLabel.setAlignment(Qt.AlignCenter)
        self.displayLabel.setWordWrap(True)
        self.dice1Outline = QLabel(self.groupBox)
        self.dice1Outline.setObjectName(u"dice1Outline")
        self.dice1Outline.setGeometry(QRect(380, 690, 161, 161))
        self.dice1Outline.setFrameShape(QFrame.Box)
        self.dice2Outline = QLabel(self.groupBox)
        self.dice2Outline.setObjectName(u"dice2Outline")
        self.dice2Outline.setGeometry(QRect(630, 690, 161, 161))
        self.dice2Outline.setFrameShape(QFrame.Box)
        self.dice1dot1 = QLabel(self.groupBox)
        self.dice1dot1.setObjectName(u"dice1dot1")
        self.dice1dot1.setGeometry(QRect(390, 670, 41, 91))
        font2 = QFont()
        font2.setPointSize(50)
        self.dice1dot1.setFont(font2)
        self.dice1dot4 = QLabel(self.groupBox)
        self.dice1dot4.setObjectName(u"dice1dot4")
        self.dice1dot4.setGeometry(QRect(440, 720, 41, 91))
        self.dice1dot4.setFont(font2)
        self.dice1dot6 = QLabel(self.groupBox)
        self.dice1dot6.setObjectName(u"dice1dot6")
        self.dice1dot6.setGeometry(QRect(390, 770, 41, 91))
        self.dice1dot6.setFont(font2)
        self.dice1dot7 = QLabel(self.groupBox)
        self.dice1dot7.setObjectName(u"dice1dot7")
        self.dice1dot7.setGeometry(QRect(490, 770, 41, 91))
        self.dice1dot7.setFont(font2)
        self.dice1dot2 = QLabel(self.groupBox)
        self.dice1dot2.setObjectName(u"dice1dot2")
        self.dice1dot2.setGeometry(QRect(490, 670, 41, 91))
        self.dice1dot2.setFont(font2)
        self.dice1dot5 = QLabel(self.groupBox)
        self.dice1dot5.setObjectName(u"dice1dot5")
        self.dice1dot5.setGeometry(QRect(490, 720, 41, 91))
        self.dice1dot5.setFont(font2)
        self.dice1dot3 = QLabel(self.groupBox)
        self.dice1dot3.setObjectName(u"dice1dot3")
        self.dice1dot3.setGeometry(QRect(390, 720, 41, 91))
        self.dice1dot3.setFont(font2)
        self.dice2dot5 = QLabel(self.groupBox)
        self.dice2dot5.setObjectName(u"dice2dot5")
        self.dice2dot5.setGeometry(QRect(740, 720, 41, 91))
        self.dice2dot5.setFont(font2)
        self.dice2dot3 = QLabel(self.groupBox)
        self.dice2dot3.setObjectName(u"dice2dot3")
        self.dice2dot3.setGeometry(QRect(640, 720, 41, 91))
        self.dice2dot3.setFont(font2)
        self.dice2dot7 = QLabel(self.groupBox)
        self.dice2dot7.setObjectName(u"dice2dot7")
        self.dice2dot7.setGeometry(QRect(740, 770, 41, 91))
        self.dice2dot7.setFont(font2)
        self.dice2dot6 = QLabel(self.groupBox)
        self.dice2dot6.setObjectName(u"dice2dot6")
        self.dice2dot6.setGeometry(QRect(640, 770, 41, 91))
        self.dice2dot6.setFont(font2)
        self.dice2dot1 = QLabel(self.groupBox)
        self.dice2dot1.setObjectName(u"dice2dot1")
        self.dice2dot1.setGeometry(QRect(640, 670, 41, 91))
        self.dice2dot1.setFont(font2)
        self.dice2dot2 = QLabel(self.groupBox)
        self.dice2dot2.setObjectName(u"dice2dot2")
        self.dice2dot2.setGeometry(QRect(740, 670, 41, 91))
        self.dice2dot2.setFont(font2)
        self.dice2dot4 = QLabel(self.groupBox)
        self.dice2dot4.setObjectName(u"dice2dot4")
        self.dice2dot4.setGeometry(QRect(690, 720, 41, 91))
        self.dice2dot4.setFont(font2)

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalSpacer_2 = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.currentPlayerLabel = QLabel(Dialog)
        self.currentPlayerLabel.setObjectName(u"currentPlayerLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currentPlayerLabel.sizePolicy().hasHeightForWidth())
        self.currentPlayerLabel.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(24)
        font3.setBold(False)
        self.currentPlayerLabel.setFont(font3)
        self.currentPlayerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.currentPlayerLabel)

        self.verticalSpacer = QSpacerItem(20, 75, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.playerInfoBox = QGroupBox(Dialog)
        self.playerInfoBox.setObjectName(u"playerInfoBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.playerInfoBox.sizePolicy().hasHeightForWidth())
        self.playerInfoBox.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(20)
        self.playerInfoBox.setFont(font4)
        self.verticalLayout = QVBoxLayout(self.playerInfoBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.player1NameLabel = QLabel(self.playerInfoBox)
        self.player1NameLabel.setObjectName(u"player1NameLabel")
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        self.player1NameLabel.setPalette(palette)
        font5 = QFont()
        font5.setStrikeOut(False)
        self.player1NameLabel.setFont(font5)
        self.player1NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player1NameLabel)

        self.player1BalanceLabel = QLabel(self.playerInfoBox)
        self.player1BalanceLabel.setObjectName(u"player1BalanceLabel")
        self.player1BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player1BalanceLabel)

        self.player2NameLabel = QLabel(self.playerInfoBox)
        self.player2NameLabel.setObjectName(u"player2NameLabel")
        palette1 = QPalette()
        brush2 = QBrush(QColor(0, 170, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.player2NameLabel.setPalette(palette1)
        self.player2NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player2NameLabel)

        self.player2BalanceLabel = QLabel(self.playerInfoBox)
        self.player2BalanceLabel.setObjectName(u"player2BalanceLabel")
        self.player2BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player2BalanceLabel)

        self.player3NameLabel = QLabel(self.playerInfoBox)
        self.player3NameLabel.setObjectName(u"player3NameLabel")
        palette2 = QPalette()
        brush3 = QBrush(QColor(0, 0, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.player3NameLabel.setPalette(palette2)
        self.player3NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player3NameLabel)

        self.player3BalanceLabel = QLabel(self.playerInfoBox)
        self.player3BalanceLabel.setObjectName(u"player3BalanceLabel")
        self.player3BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player3BalanceLabel)

        self.player4NameLabel = QLabel(self.playerInfoBox)
        self.player4NameLabel.setObjectName(u"player4NameLabel")
        palette3 = QPalette()
        brush4 = QBrush(QColor(255, 170, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.player4NameLabel.setPalette(palette3)
        self.player4NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player4NameLabel)

        self.player4BalanceLabel = QLabel(self.playerInfoBox)
        self.player4BalanceLabel.setObjectName(u"player4BalanceLabel")
        self.player4BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player4BalanceLabel)

        self.player5NameLabel = QLabel(self.playerInfoBox)
        self.player5NameLabel.setObjectName(u"player5NameLabel")
        palette4 = QPalette()
        brush5 = QBrush(QColor(85, 170, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.player5NameLabel.setPalette(palette4)
        self.player5NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player5NameLabel)

        self.player5BalanceLabel = QLabel(self.playerInfoBox)
        self.player5BalanceLabel.setObjectName(u"player5BalanceLabel")
        self.player5BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player5BalanceLabel)

        self.player6NameLabel = QLabel(self.playerInfoBox)
        self.player6NameLabel.setObjectName(u"player6NameLabel")
        palette5 = QPalette()
        brush6 = QBrush(QColor(85, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.player6NameLabel.setPalette(palette5)
        self.player6NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player6NameLabel)

        self.player6BalanceLabel = QLabel(self.playerInfoBox)
        self.player6BalanceLabel.setObjectName(u"player6BalanceLabel")
        self.player6BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player6BalanceLabel)

        self.player7NameLabel = QLabel(self.playerInfoBox)
        self.player7NameLabel.setObjectName(u"player7NameLabel")
        palette6 = QPalette()
        brush7 = QBrush(QColor(170, 85, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush7)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        self.player7NameLabel.setPalette(palette6)
        self.player7NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player7NameLabel)

        self.player7BalanceLabel = QLabel(self.playerInfoBox)
        self.player7BalanceLabel.setObjectName(u"player7BalanceLabel")
        self.player7BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player7BalanceLabel)

        self.player8NameLabel = QLabel(self.playerInfoBox)
        self.player8NameLabel.setObjectName(u"player8NameLabel")
        self.player8NameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player8NameLabel)

        self.player8BalanceLabel = QLabel(self.playerInfoBox)
        self.player8BalanceLabel.setObjectName(u"player8BalanceLabel")
        self.player8BalanceLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.player8BalanceLabel)


        self.verticalLayout_2.addWidget(self.playerInfoBox)

        self.verticalSpacer_3 = QSpacerItem(20, 110, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.tradeButton = QPushButton(Dialog)
        self.tradeButton.setObjectName(u"tradeButton")
        self.tradeButton.setMinimumSize(QSize(125, 75))
        self.tradeButton.setFont(font4)

        self.horizontalLayout.addWidget(self.tradeButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.mortgageButton = QPushButton(Dialog)
        self.mortgageButton.setObjectName(u"mortgageButton")
        self.mortgageButton.setMinimumSize(QSize(175, 75))
        self.mortgageButton.setFont(font4)

        self.horizontalLayout.addWidget(self.mortgageButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.housesButton = QPushButton(Dialog)
        self.housesButton.setObjectName(u"housesButton")
        self.housesButton.setMinimumSize(QSize(150, 75))
        self.housesButton.setFont(font4)

        self.horizontalLayout.addWidget(self.housesButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.transactionLabel = QLabel(Dialog)
        self.transactionLabel.setObjectName(u"transactionLabel")
        self.transactionLabel.setMinimumSize(QSize(670, 0))
        self.transactionLabel.setAlignment(Qt.AlignCenter)
        self.transactionLabel.setWordWrap(True)

        self.horizontalLayout.addWidget(self.transactionLabel)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.boardImageLabel.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><img src=\":/newPrefix/gameBoard.png\"/></p></body></html>", None))
        self.endTurnButton.setText(QCoreApplication.translate("Dialog", u"End Turn", None))
        self.bankruptButton.setText(QCoreApplication.translate("Dialog", u"Bankrupt", None))
        self.displayLabel.setText(QCoreApplication.translate("Dialog", u"Display Message Here", None))
        self.dice1Outline.setText("")
        self.dice2Outline.setText("")
        self.dice1dot1.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice1dot4.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice1dot6.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice1dot7.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice1dot2.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice1dot5.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice1dot3.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot5.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot3.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot7.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot6.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot1.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot2.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.dice2dot4.setText(QCoreApplication.translate("Dialog", u"\u2022", None))
        self.currentPlayerLabel.setText(QCoreApplication.translate("Dialog", u"player1", None))
        self.playerInfoBox.setTitle(QCoreApplication.translate("Dialog", u"Players", None))
        self.player1NameLabel.setText(QCoreApplication.translate("Dialog", u"player1", None))
        self.player1BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player2NameLabel.setText(QCoreApplication.translate("Dialog", u"player2", None))
        self.player2BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player3NameLabel.setText(QCoreApplication.translate("Dialog", u"player3", None))
        self.player3BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player4NameLabel.setText(QCoreApplication.translate("Dialog", u"player4", None))
        self.player4BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player5NameLabel.setText(QCoreApplication.translate("Dialog", u"player5", None))
        self.player5BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player6NameLabel.setText(QCoreApplication.translate("Dialog", u"player6", None))
        self.player6BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player7NameLabel.setText(QCoreApplication.translate("Dialog", u"player7", None))
        self.player7BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.player8NameLabel.setText(QCoreApplication.translate("Dialog", u"player8", None))
        self.player8BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a30", None))
        self.tradeButton.setText(QCoreApplication.translate("Dialog", u"Trade", None))
        self.mortgageButton.setText(QCoreApplication.translate("Dialog", u"Mortgage", None))
        self.housesButton.setText(QCoreApplication.translate("Dialog", u"Houses", None))
        self.transactionLabel.setText(QCoreApplication.translate("Dialog", u"Transaction Message Here", None))
    # retranslateUi

