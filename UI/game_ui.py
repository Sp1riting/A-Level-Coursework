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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1806, 1165)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.currentPlayerLabel = QLabel(Dialog)
        self.currentPlayerLabel.setObjectName(u"currentPlayerLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentPlayerLabel.sizePolicy().hasHeightForWidth())
        self.currentPlayerLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.currentPlayerLabel.setFont(font1)
        self.currentPlayerLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.currentPlayerLabel)

        self.playerInfoBox = QGroupBox(Dialog)
        self.playerInfoBox.setObjectName(u"playerInfoBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.playerInfoBox.sizePolicy().hasHeightForWidth())
        self.playerInfoBox.setSizePolicy(sizePolicy1)
        self.playerInfoBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.playerInfoBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.player1NameLabel = QLabel(self.playerInfoBox)
        self.player1NameLabel.setObjectName(u"player1NameLabel")
        font2 = QFont()
        font2.setStrikeOut(False)
        self.player1NameLabel.setFont(font2)

        self.verticalLayout.addWidget(self.player1NameLabel)

        self.player1BalanceLabel = QLabel(self.playerInfoBox)
        self.player1BalanceLabel.setObjectName(u"player1BalanceLabel")

        self.verticalLayout.addWidget(self.player1BalanceLabel)

        self.player2NameLabel = QLabel(self.playerInfoBox)
        self.player2NameLabel.setObjectName(u"player2NameLabel")

        self.verticalLayout.addWidget(self.player2NameLabel)

        self.player2BalanceLabel = QLabel(self.playerInfoBox)
        self.player2BalanceLabel.setObjectName(u"player2BalanceLabel")

        self.verticalLayout.addWidget(self.player2BalanceLabel)

        self.player3NameLabel = QLabel(self.playerInfoBox)
        self.player3NameLabel.setObjectName(u"player3NameLabel")

        self.verticalLayout.addWidget(self.player3NameLabel)

        self.player3BalanceLabel = QLabel(self.playerInfoBox)
        self.player3BalanceLabel.setObjectName(u"player3BalanceLabel")

        self.verticalLayout.addWidget(self.player3BalanceLabel)

        self.player4NameLabel = QLabel(self.playerInfoBox)
        self.player4NameLabel.setObjectName(u"player4NameLabel")

        self.verticalLayout.addWidget(self.player4NameLabel)

        self.player4BalanceLabel = QLabel(self.playerInfoBox)
        self.player4BalanceLabel.setObjectName(u"player4BalanceLabel")

        self.verticalLayout.addWidget(self.player4BalanceLabel)

        self.player5NameLabel = QLabel(self.playerInfoBox)
        self.player5NameLabel.setObjectName(u"player5NameLabel")

        self.verticalLayout.addWidget(self.player5NameLabel)

        self.player5BalanceLabel = QLabel(self.playerInfoBox)
        self.player5BalanceLabel.setObjectName(u"player5BalanceLabel")

        self.verticalLayout.addWidget(self.player5BalanceLabel)

        self.player6NameLabel = QLabel(self.playerInfoBox)
        self.player6NameLabel.setObjectName(u"player6NameLabel")

        self.verticalLayout.addWidget(self.player6NameLabel)

        self.player6BalanceLabel = QLabel(self.playerInfoBox)
        self.player6BalanceLabel.setObjectName(u"player6BalanceLabel")

        self.verticalLayout.addWidget(self.player6BalanceLabel)

        self.player7NameLabel = QLabel(self.playerInfoBox)
        self.player7NameLabel.setObjectName(u"player7NameLabel")

        self.verticalLayout.addWidget(self.player7NameLabel)

        self.player7BalanceLabel = QLabel(self.playerInfoBox)
        self.player7BalanceLabel.setObjectName(u"player7BalanceLabel")

        self.verticalLayout.addWidget(self.player7BalanceLabel)

        self.player8NameLabel = QLabel(self.playerInfoBox)
        self.player8NameLabel.setObjectName(u"player8NameLabel")

        self.verticalLayout.addWidget(self.player8NameLabel)

        self.player8BalanceLabel = QLabel(self.playerInfoBox)
        self.player8BalanceLabel.setObjectName(u"player8BalanceLabel")

        self.verticalLayout.addWidget(self.player8BalanceLabel)


        self.verticalLayout_2.addWidget(self.playerInfoBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 468, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(125, 75))
        font3 = QFont()
        font3.setPointSize(16)
        self.pushButton.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(175, 75))
        self.pushButton_2.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(150, 75))
        self.pushButton_3.setFont(font3)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.currentPlayerLabel.setText(QCoreApplication.translate("Dialog", u"player1", None))
        self.playerInfoBox.setTitle(QCoreApplication.translate("Dialog", u"Players", None))
        self.player1NameLabel.setText(QCoreApplication.translate("Dialog", u"player1", None))
        self.player1BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player2NameLabel.setText(QCoreApplication.translate("Dialog", u"player2", None))
        self.player2BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player3NameLabel.setText(QCoreApplication.translate("Dialog", u"player3", None))
        self.player3BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player4NameLabel.setText(QCoreApplication.translate("Dialog", u"player4", None))
        self.player4BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player5NameLabel.setText(QCoreApplication.translate("Dialog", u"player5", None))
        self.player5BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player6NameLabel.setText(QCoreApplication.translate("Dialog", u"player6", None))
        self.player6BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player7NameLabel.setText(QCoreApplication.translate("Dialog", u"player7", None))
        self.player7BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.player8NameLabel.setText(QCoreApplication.translate("Dialog", u"player8", None))
        self.player8BalanceLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3balance", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Trade", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Mortgage", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Houses", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Transaction Message Here", None))
    # retranslateUi

