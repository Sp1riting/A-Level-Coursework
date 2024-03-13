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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(726, 377)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.gamesPlayedLabel = QLabel(self.groupBox)
        self.gamesPlayedLabel.setObjectName(u"gamesPlayedLabel")
        font = QFont()
        font.setPointSize(12)
        self.gamesPlayedLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.gamesPlayedLabel)

        self.gamesPlayedValue = QLabel(self.groupBox)
        self.gamesPlayedValue.setObjectName(u"gamesPlayedValue")
        self.gamesPlayedValue.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.gamesPlayedValue)

        self.doublesRolledLabel = QLabel(self.groupBox)
        self.doublesRolledLabel.setObjectName(u"doublesRolledLabel")
        self.doublesRolledLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.doublesRolledLabel)

        self.doublesRolledValue = QLabel(self.groupBox)
        self.doublesRolledValue.setObjectName(u"doublesRolledValue")
        self.doublesRolledValue.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doublesRolledValue)

        self.propertiesPurchasedLabel = QLabel(self.groupBox)
        self.propertiesPurchasedLabel.setObjectName(u"propertiesPurchasedLabel")
        self.propertiesPurchasedLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.propertiesPurchasedLabel)

        self.propertiesPurchasedValue = QLabel(self.groupBox)
        self.propertiesPurchasedValue.setObjectName(u"propertiesPurchasedValue")
        self.propertiesPurchasedValue.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.propertiesPurchasedValue)

        self.moneyEarnedLabel = QLabel(self.groupBox)
        self.moneyEarnedLabel.setObjectName(u"moneyEarnedLabel")
        self.moneyEarnedLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.moneyEarnedLabel)

        self.moneyEarnedValue = QLabel(self.groupBox)
        self.moneyEarnedValue.setObjectName(u"moneyEarnedValue")
        self.moneyEarnedValue.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.moneyEarnedValue)

        self.rentPaidLabel = QLabel(self.groupBox)
        self.rentPaidLabel.setObjectName(u"rentPaidLabel")
        self.rentPaidLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.rentPaidLabel)

        self.rentPaidValue = QLabel(self.groupBox)
        self.rentPaidValue.setObjectName(u"rentPaidValue")
        self.rentPaidValue.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.rentPaidValue)

        self.passedGoLabel = QLabel(self.groupBox)
        self.passedGoLabel.setObjectName(u"passedGoLabel")
        self.passedGoLabel.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.passedGoLabel)

        self.passedGoValue = QLabel(self.groupBox)
        self.passedGoValue.setObjectName(u"passedGoValue")
        self.passedGoValue.setFont(font)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.passedGoValue)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


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
        font1 = QFont()
        font1.setPointSize(24)
        self.gameStatsTitleLabel.setFont(font1)
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
        font2 = QFont()
        font2.setPointSize(16)
        self.gameStatsReturnButton.setFont(font2)

        self.gameStatsHorizontalLayout.addWidget(self.gameStatsReturnButton)


        self.gridLayout_2.addLayout(self.gameStatsHorizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.gamesPlayedLabel.setText(QCoreApplication.translate("Dialog", u"Games Played:", None))
        self.gamesPlayedValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.doublesRolledLabel.setText(QCoreApplication.translate("Dialog", u"Doubles Rolled:", None))
        self.doublesRolledValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.propertiesPurchasedLabel.setText(QCoreApplication.translate("Dialog", u"Total Properties Purchased:", None))
        self.propertiesPurchasedValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.moneyEarnedLabel.setText(QCoreApplication.translate("Dialog", u"Total Money Earned:", None))
        self.moneyEarnedValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.rentPaidLabel.setText(QCoreApplication.translate("Dialog", u"Total Rent Paid: ", None))
        self.rentPaidValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.passedGoLabel.setText(QCoreApplication.translate("Dialog", u"Number of Times Players Passed Go:", None))
        self.passedGoValue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.gameStatsTitleLabel.setText(QCoreApplication.translate("Dialog", u"Game Statistics", None))
        self.gameStatsReturnButton.setText(QCoreApplication.translate("Dialog", u"Return", None))
    # retranslateUi

