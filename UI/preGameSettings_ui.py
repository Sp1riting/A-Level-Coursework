# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preGameSettings.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(846, 570)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.preGameTitleLabel = QLabel(Dialog)
        self.preGameTitleLabel.setObjectName(u"preGameTitleLabel")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(False)
        self.preGameTitleLabel.setFont(font1)
        self.preGameTitleLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.preGameTitleLabel, 0, 0, 1, 1)

        self.preGameErrorLabel = QLabel(Dialog)
        self.preGameErrorLabel.setObjectName(u"preGameErrorLabel")
        self.preGameErrorLabel.setFont(font)

        self.gridLayout.addWidget(self.preGameErrorLabel, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.preGamePlayButton = QPushButton(Dialog)
        self.preGamePlayButton.setObjectName(u"preGamePlayButton")
        self.preGamePlayButton.setMinimumSize(QSize(200, 75))
        font2 = QFont()
        font2.setPointSize(16)
        self.preGamePlayButton.setFont(font2)

        self.horizontalLayout.addWidget(self.preGamePlayButton)

        self.preGameReturnButton = QPushButton(Dialog)
        self.preGameReturnButton.setObjectName(u"preGameReturnButton")
        self.preGameReturnButton.setMinimumSize(QSize(200, 75))
        self.preGameReturnButton.setFont(font2)

        self.horizontalLayout.addWidget(self.preGameReturnButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.startingBalanceLabel = QLabel(self.groupBox)
        self.startingBalanceLabel.setObjectName(u"startingBalanceLabel")
        self.startingBalanceLabel.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.startingBalanceLabel)

        self.moneyFromGoLabel = QLabel(self.groupBox)
        self.moneyFromGoLabel.setObjectName(u"moneyFromGoLabel")
        self.moneyFromGoLabel.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.moneyFromGoLabel)

        self.numberOfPlayersLabel = QLabel(self.groupBox)
        self.numberOfPlayersLabel.setObjectName(u"numberOfPlayersLabel")
        self.numberOfPlayersLabel.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.numberOfPlayersLabel)

        self.rentFromJailLabel = QLabel(self.groupBox)
        self.rentFromJailLabel.setObjectName(u"rentFromJailLabel")
        self.rentFromJailLabel.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.rentFromJailLabel)

        self.fastBankruptcyLabel = QLabel(self.groupBox)
        self.fastBankruptcyLabel.setObjectName(u"fastBankruptcyLabel")
        self.fastBankruptcyLabel.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.fastBankruptcyLabel)

        self.startingBalanceSpinBox = QSpinBox(self.groupBox)
        self.startingBalanceSpinBox.setObjectName(u"startingBalanceSpinBox")
        self.startingBalanceSpinBox.setMaximum(10000)
        self.startingBalanceSpinBox.setSingleStep(1000)
        self.startingBalanceSpinBox.setValue(1500)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.startingBalanceSpinBox)

        self.moneyFromGoSpinBox = QSpinBox(self.groupBox)
        self.moneyFromGoSpinBox.setObjectName(u"moneyFromGoSpinBox")
        self.moneyFromGoSpinBox.setMaximum(2000)
        self.moneyFromGoSpinBox.setSingleStep(100)
        self.moneyFromGoSpinBox.setValue(200)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.moneyFromGoSpinBox)

        self.numberOfPlayersSpinBox = QSpinBox(self.groupBox)
        self.numberOfPlayersSpinBox.setObjectName(u"numberOfPlayersSpinBox")
        self.numberOfPlayersSpinBox.setMaximum(8)
        self.numberOfPlayersSpinBox.setValue(4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.numberOfPlayersSpinBox)

        self.fastBankruptcyCheckBox = QCheckBox(self.groupBox)
        self.fastBankruptcyCheckBox.setObjectName(u"fastBankruptcyCheckBox")
        font3 = QFont()
        font3.setPointSize(8)
        self.fastBankruptcyCheckBox.setFont(font3)
        self.fastBankruptcyCheckBox.setLayoutDirection(Qt.RightToLeft)
        self.fastBankruptcyCheckBox.setAutoFillBackground(False)
        self.fastBankruptcyCheckBox.setIconSize(QSize(30, 30))
        self.fastBankruptcyCheckBox.setChecked(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.fastBankruptcyCheckBox)

        self.rentFromJailCheckBox = QCheckBox(self.groupBox)
        self.rentFromJailCheckBox.setObjectName(u"rentFromJailCheckBox")
        self.rentFromJailCheckBox.setFont(font)
        self.rentFromJailCheckBox.setLayoutDirection(Qt.RightToLeft)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.rentFromJailCheckBox)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.preGameTitleLabel.setText(QCoreApplication.translate("Dialog", u"Pre-Game Settings", None))
        self.preGameErrorLabel.setText("")
        self.preGamePlayButton.setText(QCoreApplication.translate("Dialog", u"Play Game", None))
        self.preGameReturnButton.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.groupBox.setTitle("")
        self.startingBalanceLabel.setText(QCoreApplication.translate("Dialog", u"Starting Balance:", None))
        self.moneyFromGoLabel.setText(QCoreApplication.translate("Dialog", u"Money From Go:", None))
        self.numberOfPlayersLabel.setText(QCoreApplication.translate("Dialog", u"Number of Players:", None))
        self.rentFromJailLabel.setText(QCoreApplication.translate("Dialog", u"Rent From Jail:", None))
        self.fastBankruptcyLabel.setText(QCoreApplication.translate("Dialog", u"Fast Bankruptcies:", None))
        self.fastBankruptcyCheckBox.setText("")
        self.rentFromJailCheckBox.setText("")
    # retranslateUi

