# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gameStatistics.ui'
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
    QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(950, 372)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.gameStatsHorizontalLayout = QHBoxLayout()
        self.gameStatsHorizontalLayout.setObjectName(u"gameStatsHorizontalLayout")
        self.gameStatsHorizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gameStatsHorizontalLayout.addItem(self.horizontalSpacer)

        self.gameStatsTitleLabel = QLabel(Dialog)
        self.gameStatsTitleLabel.setObjectName(u"gameStatsTitleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameStatsTitleLabel.sizePolicy().hasHeightForWidth())
        self.gameStatsTitleLabel.setSizePolicy(sizePolicy)
        self.gameStatsTitleLabel.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setPointSize(24)
        self.gameStatsTitleLabel.setFont(font)
        self.gameStatsTitleLabel.setLayoutDirection(Qt.LeftToRight)

        self.gameStatsHorizontalLayout.addWidget(self.gameStatsTitleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gameStatsHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.gameStatsReturnButton = QPushButton(Dialog)
        self.gameStatsReturnButton.setObjectName(u"gameStatsReturnButton")
        sizePolicy.setHeightForWidth(self.gameStatsReturnButton.sizePolicy().hasHeightForWidth())
        self.gameStatsReturnButton.setSizePolicy(sizePolicy)
        self.gameStatsReturnButton.setMinimumSize(QSize(200, 50))
        self.gameStatsReturnButton.setMaximumSize(QSize(200, 60))
        font1 = QFont()
        font1.setPointSize(16)
        self.gameStatsReturnButton.setFont(font1)

        self.gameStatsHorizontalLayout.addWidget(self.gameStatsReturnButton)


        self.gridLayout_2.addLayout(self.gameStatsHorizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total Money Earned:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Total Properties Purchased:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Doubles Rolled:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Games Played:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Total Rent Paid: ", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Number of Times Players Passed Go:", None))
        self.gameStatsTitleLabel.setText(QCoreApplication.translate("Dialog", u"Game Statistics", None))
        self.gameStatsReturnButton.setText(QCoreApplication.translate("Dialog", u"Return", None))
    # retranslateUi

