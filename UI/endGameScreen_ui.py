# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'endGameScreen.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(676, 448)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gameEndTitleLabel = QLabel(Dialog)
        self.gameEndTitleLabel.setObjectName(u"gameEndTitleLabel")
        font = QFont()
        font.setPointSize(24)
        self.gameEndTitleLabel.setFont(font)
        self.gameEndTitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.gameEndTitleLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(17)
        self.label_2.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.winnerDisplayLabel = QLabel(Dialog)
        self.winnerDisplayLabel.setObjectName(u"winnerDisplayLabel")
        self.winnerDisplayLabel.setFont(font1)
        self.winnerDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.winnerDisplayLabel)

        self.doublesLabel = QLabel(Dialog)
        self.doublesLabel.setObjectName(u"doublesLabel")
        font2 = QFont()
        font2.setPointSize(14)
        self.doublesLabel.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.doublesLabel)

        self.doublesDisplayLabel = QLabel(Dialog)
        self.doublesDisplayLabel.setObjectName(u"doublesDisplayLabel")
        self.doublesDisplayLabel.setFont(font2)
        self.doublesDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doublesDisplayLabel)

        self.propertiesLabel = QLabel(Dialog)
        self.propertiesLabel.setObjectName(u"propertiesLabel")
        self.propertiesLabel.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.propertiesLabel)

        self.propertiesDisplayLabel = QLabel(Dialog)
        self.propertiesDisplayLabel.setObjectName(u"propertiesDisplayLabel")
        self.propertiesDisplayLabel.setFont(font2)
        self.propertiesDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.propertiesDisplayLabel)

        self.earnedLabel = QLabel(Dialog)
        self.earnedLabel.setObjectName(u"earnedLabel")
        self.earnedLabel.setFont(font2)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.earnedLabel)

        self.earnedDisplayLabel = QLabel(Dialog)
        self.earnedDisplayLabel.setObjectName(u"earnedDisplayLabel")
        self.earnedDisplayLabel.setFont(font2)
        self.earnedDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.earnedDisplayLabel)

        self.rentLabel = QLabel(Dialog)
        self.rentLabel.setObjectName(u"rentLabel")
        self.rentLabel.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.rentLabel)

        self.rentDisplayLabel = QLabel(Dialog)
        self.rentDisplayLabel.setObjectName(u"rentDisplayLabel")
        self.rentDisplayLabel.setFont(font2)
        self.rentDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.rentDisplayLabel)

        self.goLabel = QLabel(Dialog)
        self.goLabel.setObjectName(u"goLabel")
        self.goLabel.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.goLabel)

        self.goDisplayLabel = QLabel(Dialog)
        self.goDisplayLabel.setObjectName(u"goDisplayLabel")
        self.goDisplayLabel.setFont(font2)
        self.goDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.goDisplayLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(1, QFormLayout.FieldRole, self.verticalSpacer_2)


        self.verticalLayout.addLayout(self.formLayout)

        self.gameEndReturnButton = QPushButton(Dialog)
        self.gameEndReturnButton.setObjectName(u"gameEndReturnButton")
        font3 = QFont()
        font3.setPointSize(16)
        self.gameEndReturnButton.setFont(font3)

        self.verticalLayout.addWidget(self.gameEndReturnButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.gameEndTitleLabel.setText(QCoreApplication.translate("Dialog", u"Game Over!", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Winner:", None))
        self.winnerDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Display Winner's Name Here", None))
        self.doublesLabel.setText(QCoreApplication.translate("Dialog", u"Doubles Rolled:", None))
        self.doublesDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Display Doubles Rolled Here", None))
        self.propertiesLabel.setText(QCoreApplication.translate("Dialog", u"Properties Purchased:", None))
        self.propertiesDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Display Properties Purchased Here", None))
        self.earnedLabel.setText(QCoreApplication.translate("Dialog", u"Money Earned:", None))
        self.earnedDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Display Money Earned Here", None))
        self.rentLabel.setText(QCoreApplication.translate("Dialog", u"Rent Paid:", None))
        self.rentDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Display Rent Paid Here", None))
        self.goLabel.setText(QCoreApplication.translate("Dialog", u"Number of Times Passed Go:", None))
        self.goDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Display Passed Go Amount Here", None))
        self.gameEndReturnButton.setText(QCoreApplication.translate("Dialog", u"Back To Main Menu", None))
    # retranslateUi

