# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMenu.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1089, 583)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.menuPlayButton = QPushButton(Dialog)
        self.menuPlayButton.setObjectName(u"menuPlayButton")
        self.menuPlayButton.setMinimumSize(QSize(300, 100))
        font = QFont()
        font.setPointSize(20)
        self.menuPlayButton.setFont(font)

        self.horizontalLayout.addWidget(self.menuPlayButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.menuReturnButton = QPushButton(Dialog)
        self.menuReturnButton.setObjectName(u"menuReturnButton")
        self.menuReturnButton.setMinimumSize(QSize(300, 100))
        self.menuReturnButton.setFont(font)

        self.horizontalLayout.addWidget(self.menuReturnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.menuHowToPlayButton = QPushButton(Dialog)
        self.menuHowToPlayButton.setObjectName(u"menuHowToPlayButton")
        self.menuHowToPlayButton.setEnabled(True)
        self.menuHowToPlayButton.setMinimumSize(QSize(300, 100))
        self.menuHowToPlayButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.menuHowToPlayButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.menuStatisticsButton = QPushButton(Dialog)
        self.menuStatisticsButton.setObjectName(u"menuStatisticsButton")
        self.menuStatisticsButton.setMinimumSize(QSize(300, 100))
        self.menuStatisticsButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.menuStatisticsButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.menuTitleLabel = QLabel(Dialog)
        self.menuTitleLabel.setObjectName(u"menuTitleLabel")
        font1 = QFont()
        font1.setPointSize(40)
        font1.setBold(True)
        self.menuTitleLabel.setFont(font1)
        self.menuTitleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.menuTitleLabel, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 8, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.menuPlayButton.setText(QCoreApplication.translate("Dialog", u"Play", None))
        self.menuReturnButton.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.menuHowToPlayButton.setText(QCoreApplication.translate("Dialog", u"How To Play", None))
        self.menuStatisticsButton.setText(QCoreApplication.translate("Dialog", u"Statistics", None))
        self.menuTitleLabel.setText(QCoreApplication.translate("Dialog", u"Zooopoly", None))
    # retranslateUi

