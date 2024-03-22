# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'extraForGame.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1637, 983)
        font = QFont()
        font.setPointSize(9)
        Dialog.setFont(font)
        self.mortgageGroupBox = QGroupBox(Dialog)
        self.mortgageGroupBox.setObjectName(u"mortgageGroupBox")
        self.mortgageGroupBox.setGeometry(QRect(50, 50, 271, 151))
        self.mortgageGroupBox.setAlignment(Qt.AlignCenter)
        self.mortgageSelectionComboBox = QComboBox(self.mortgageGroupBox)
        self.mortgageSelectionComboBox.addItem("")
        self.mortgageSelectionComboBox.setObjectName(u"mortgageSelectionComboBox")
        self.mortgageSelectionComboBox.setGeometry(QRect(10, 30, 131, 41))
        self.unmortgageSelectionComboBox = QComboBox(self.mortgageGroupBox)
        self.unmortgageSelectionComboBox.addItem("")
        self.unmortgageSelectionComboBox.setObjectName(u"unmortgageSelectionComboBox")
        self.unmortgageSelectionComboBox.setGeometry(QRect(10, 90, 131, 41))
        self.mortgageItemButton = QPushButton(self.mortgageGroupBox)
        self.mortgageItemButton.setObjectName(u"mortgageItemButton")
        self.mortgageItemButton.setGeometry(QRect(150, 30, 111, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.mortgageItemButton.setFont(font1)
        self.unmortgageItemButton = QPushButton(self.mortgageGroupBox)
        self.unmortgageItemButton.setObjectName(u"unmortgageItemButton")
        self.unmortgageItemButton.setGeometry(QRect(150, 90, 111, 41))
        self.unmortgageItemButton.setFont(font1)
        self.housesGroupBox = QGroupBox(Dialog)
        self.housesGroupBox.setObjectName(u"housesGroupBox")
        self.housesGroupBox.setGeometry(QRect(340, 50, 271, 151))
        self.housesGroupBox.setAlignment(Qt.AlignCenter)
        self.buyHouseSelectionComboBox = QComboBox(self.housesGroupBox)
        self.buyHouseSelectionComboBox.addItem("")
        self.buyHouseSelectionComboBox.setObjectName(u"buyHouseSelectionComboBox")
        self.buyHouseSelectionComboBox.setGeometry(QRect(10, 30, 131, 41))
        self.sellHouseSelectionComboBox = QComboBox(self.housesGroupBox)
        self.sellHouseSelectionComboBox.addItem("")
        self.sellHouseSelectionComboBox.setObjectName(u"sellHouseSelectionComboBox")
        self.sellHouseSelectionComboBox.setGeometry(QRect(10, 90, 131, 41))
        self.buyHouseButton = QPushButton(self.housesGroupBox)
        self.buyHouseButton.setObjectName(u"buyHouseButton")
        self.buyHouseButton.setGeometry(QRect(150, 30, 111, 41))
        self.buyHouseButton.setFont(font1)
        self.sellHouseButton = QPushButton(self.housesGroupBox)
        self.sellHouseButton.setObjectName(u"sellHouseButton")
        self.sellHouseButton.setGeometry(QRect(150, 90, 111, 41))
        self.sellHouseButton.setFont(font1)
        self.inJailGroupBox = QGroupBox(Dialog)
        self.inJailGroupBox.setObjectName(u"inJailGroupBox")
        self.inJailGroupBox.setGeometry(QRect(70, 250, 331, 341))
        font2 = QFont()
        font2.setPointSize(12)
        self.inJailGroupBox.setFont(font2)
        self.inJailGroupBox.setAlignment(Qt.AlignCenter)
        self.inJailMainLabel = QLabel(self.inJailGroupBox)
        self.inJailMainLabel.setObjectName(u"inJailMainLabel")
        self.inJailMainLabel.setGeometry(QRect(120, 10, 91, 41))
        font3 = QFont()
        font3.setPointSize(20)
        self.inJailMainLabel.setFont(font3)
        self.payBailPushButton = QPushButton(self.inJailGroupBox)
        self.payBailPushButton.setObjectName(u"payBailPushButton")
        self.payBailPushButton.setGeometry(QRect(90, 70, 151, 51))
        self.GOOJFCpushButton = QPushButton(self.inJailGroupBox)
        self.GOOJFCpushButton.setObjectName(u"GOOJFCpushButton")
        self.GOOJFCpushButton.setGeometry(QRect(20, 140, 291, 51))
        self.rollDoublePushButton = QPushButton(self.inJailGroupBox)
        self.rollDoublePushButton.setObjectName(u"rollDoublePushButton")
        self.rollDoublePushButton.setGeometry(QRect(70, 210, 191, 51))
        self.inJailMessageLabel = QLabel(self.inJailGroupBox)
        self.inJailMessageLabel.setObjectName(u"inJailMessageLabel")
        self.inJailMessageLabel.setGeometry(QRect(10, 280, 311, 61))
        self.inJailMessageLabel.setFont(font1)
        self.inJailMessageLabel.setAlignment(Qt.AlignCenter)
        self.inJailMessageLabel.setWordWrap(True)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(430, 410, 321, 501))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 0, 301, 495))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font4 = QFont()
        font4.setPointSize(14)
        self.pushButton_4.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButton_5)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.normalCardVerticalLayout = QVBoxLayout()
        self.normalCardVerticalLayout.setObjectName(u"normalCardVerticalLayout")
        self.normalCardNameLabel = QLabel(self.gridLayoutWidget)
        self.normalCardNameLabel.setObjectName(u"normalCardNameLabel")
        font5 = QFont()
        font5.setPointSize(16)
        self.normalCardNameLabel.setFont(font5)
        self.normalCardNameLabel.setAlignment(Qt.AlignCenter)

        self.normalCardVerticalLayout.addWidget(self.normalCardNameLabel)

        self.normalCardBasicFormLayout = QFormLayout()
        self.normalCardBasicFormLayout.setObjectName(u"normalCardBasicFormLayout")
        self.normalCardColourSetLabel = QLabel(self.gridLayoutWidget)
        self.normalCardColourSetLabel.setObjectName(u"normalCardColourSetLabel")
        self.normalCardColourSetLabel.setFont(font2)

        self.normalCardBasicFormLayout.setWidget(0, QFormLayout.LabelRole, self.normalCardColourSetLabel)

        self.normalCardColourDisplayLabel = QLabel(self.gridLayoutWidget)
        self.normalCardColourDisplayLabel.setObjectName(u"normalCardColourDisplayLabel")
        self.normalCardColourDisplayLabel.setFont(font2)
        self.normalCardColourDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalCardBasicFormLayout.setWidget(0, QFormLayout.FieldRole, self.normalCardColourDisplayLabel)

        self.normalCardCostLabel = QLabel(self.gridLayoutWidget)
        self.normalCardCostLabel.setObjectName(u"normalCardCostLabel")
        self.normalCardCostLabel.setFont(font2)

        self.normalCardBasicFormLayout.setWidget(1, QFormLayout.LabelRole, self.normalCardCostLabel)

        self.normalCardCostDisplayLabel = QLabel(self.gridLayoutWidget)
        self.normalCardCostDisplayLabel.setObjectName(u"normalCardCostDisplayLabel")
        self.normalCardCostDisplayLabel.setFont(font2)
        self.normalCardCostDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalCardBasicFormLayout.setWidget(1, QFormLayout.FieldRole, self.normalCardCostDisplayLabel)

        self.normalCardHouseCostLabel = QLabel(self.gridLayoutWidget)
        self.normalCardHouseCostLabel.setObjectName(u"normalCardHouseCostLabel")
        self.normalCardHouseCostLabel.setFont(font2)

        self.normalCardBasicFormLayout.setWidget(2, QFormLayout.LabelRole, self.normalCardHouseCostLabel)

        self.normalCardHouseCostDisplayLabel = QLabel(self.gridLayoutWidget)
        self.normalCardHouseCostDisplayLabel.setObjectName(u"normalCardHouseCostDisplayLabel")
        self.normalCardHouseCostDisplayLabel.setFont(font2)
        self.normalCardHouseCostDisplayLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalCardBasicFormLayout.setWidget(2, QFormLayout.FieldRole, self.normalCardHouseCostDisplayLabel)


        self.normalCardVerticalLayout.addLayout(self.normalCardBasicFormLayout)

        self.normalCardRentLabel = QLabel(self.gridLayoutWidget)
        self.normalCardRentLabel.setObjectName(u"normalCardRentLabel")
        self.normalCardRentLabel.setFont(font4)
        self.normalCardRentLabel.setAlignment(Qt.AlignCenter)

        self.normalCardVerticalLayout.addWidget(self.normalCardRentLabel)

        self.normalcardRentFormLayout = QFormLayout()
        self.normalcardRentFormLayout.setObjectName(u"normalcardRentFormLayout")
        self.normalCardBaseRentLabel = QLabel(self.gridLayoutWidget)
        self.normalCardBaseRentLabel.setObjectName(u"normalCardBaseRentLabel")
        self.normalCardBaseRentLabel.setFont(font2)

        self.normalcardRentFormLayout.setWidget(0, QFormLayout.LabelRole, self.normalCardBaseRentLabel)

        self.normalCardBaseAmountLabel = QLabel(self.gridLayoutWidget)
        self.normalCardBaseAmountLabel.setObjectName(u"normalCardBaseAmountLabel")
        self.normalCardBaseAmountLabel.setFont(font2)
        self.normalCardBaseAmountLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalcardRentFormLayout.setWidget(0, QFormLayout.FieldRole, self.normalCardBaseAmountLabel)

        self.normalCardOneLabel = QLabel(self.gridLayoutWidget)
        self.normalCardOneLabel.setObjectName(u"normalCardOneLabel")
        self.normalCardOneLabel.setFont(font2)

        self.normalcardRentFormLayout.setWidget(1, QFormLayout.LabelRole, self.normalCardOneLabel)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalcardRentFormLayout.setWidget(1, QFormLayout.FieldRole, self.label_13)

        self.normalCardTwoLabel = QLabel(self.gridLayoutWidget)
        self.normalCardTwoLabel.setObjectName(u"normalCardTwoLabel")
        self.normalCardTwoLabel.setFont(font2)

        self.normalcardRentFormLayout.setWidget(2, QFormLayout.LabelRole, self.normalCardTwoLabel)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalcardRentFormLayout.setWidget(2, QFormLayout.FieldRole, self.label_15)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.normalcardRentFormLayout.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalcardRentFormLayout.setWidget(3, QFormLayout.FieldRole, self.label_14)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.normalcardRentFormLayout.setWidget(4, QFormLayout.LabelRole, self.label_21)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalcardRentFormLayout.setWidget(4, QFormLayout.FieldRole, self.label_20)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.normalcardRentFormLayout.setWidget(5, QFormLayout.LabelRole, self.label_22)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.normalcardRentFormLayout.setWidget(5, QFormLayout.FieldRole, self.label_16)


        self.normalCardVerticalLayout.addLayout(self.normalcardRentFormLayout)


        self.gridLayout.addLayout(self.normalCardVerticalLayout, 1, 0, 1, 1)

        self.frame_3 = QFrame(Dialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(780, 450, 321, 411))
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.frame_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 0, 301, 401))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_8 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setFont(font4)

        self.horizontalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setFont(font4)

        self.horizontalLayout_3.addWidget(self.pushButton_9)


        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_43 = QLabel(self.gridLayoutWidget_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font5)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_43)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_44 = QLabel(self.gridLayoutWidget_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_44)

        self.label_45 = QLabel(self.gridLayoutWidget_3)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.label_45)

        self.label_46 = QLabel(self.gridLayoutWidget_3)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font2)

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_46)

        self.label_47 = QLabel(self.gridLayoutWidget_3)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font2)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.label_47)


        self.verticalLayout_3.addLayout(self.formLayout_5)

        self.label_50 = QLabel(self.gridLayoutWidget_3)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font4)
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_50)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_53 = QLabel(self.gridLayoutWidget_3)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font2)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_53)

        self.label_54 = QLabel(self.gridLayoutWidget_3)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.label_54)

        self.label_55 = QLabel(self.gridLayoutWidget_3)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font2)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_55)

        self.label_56 = QLabel(self.gridLayoutWidget_3)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font2)
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.label_56)

        self.label_57 = QLabel(self.gridLayoutWidget_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.label_57)

        self.label_58 = QLabel(self.gridLayoutWidget_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.label_58)

        self.label_59 = QLabel(self.gridLayoutWidget_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font2)

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.label_59)

        self.label_60 = QLabel(self.gridLayoutWidget_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font2)
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.label_60)


        self.verticalLayout_3.addLayout(self.formLayout_6)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.frame_4 = QFrame(Dialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(1130, 460, 351, 351))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 0, 329, 341))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_10 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setFont(font4)

        self.horizontalLayout_4.addWidget(self.pushButton_11)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 4, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_48 = QLabel(self.gridLayoutWidget_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font5)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_48)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_49 = QLabel(self.gridLayoutWidget_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font2)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_49)

        self.label_51 = QLabel(self.gridLayoutWidget_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font2)
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.label_51)

        self.label_52 = QLabel(self.gridLayoutWidget_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_52)

        self.label_61 = QLabel(self.gridLayoutWidget_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font2)
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.label_61)


        self.verticalLayout_4.addLayout(self.formLayout_7)

        self.label_62 = QLabel(self.gridLayoutWidget_4)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font4)
        self.label_62.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_62)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_63 = QLabel(self.gridLayoutWidget_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font2)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_63)

        self.label_64 = QLabel(self.gridLayoutWidget_4)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font2)
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.label_64)

        self.label_65 = QLabel(self.gridLayoutWidget_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font2)

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_65)

        self.label_66 = QLabel(self.gridLayoutWidget_4)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font2)
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.label_66)


        self.verticalLayout_4.addLayout(self.formLayout_8)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 1, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.mortgageGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Please select properties below", None))
        self.mortgageSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.mortgageSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.unmortgageSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.unmortgageSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.mortgageItemButton.setText(QCoreApplication.translate("Dialog", u"Mortgage", None))
        self.unmortgageItemButton.setText(QCoreApplication.translate("Dialog", u"Unmortgage", None))
        self.housesGroupBox.setTitle(QCoreApplication.translate("Dialog", u"Please select properties below", None))
        self.buyHouseSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.buyHouseSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.sellHouseSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.sellHouseSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.buyHouseButton.setText(QCoreApplication.translate("Dialog", u"Buy House", None))
        self.sellHouseButton.setText(QCoreApplication.translate("Dialog", u"Sell House", None))
        self.inJailGroupBox.setTitle("")
        self.inJailMainLabel.setText(QCoreApplication.translate("Dialog", u"In Jail", None))
        self.payBailPushButton.setText(QCoreApplication.translate("Dialog", u"Pay Bail (\u00a350)", None))
        self.GOOJFCpushButton.setText(QCoreApplication.translate("Dialog", u"Use Get Out of Jail Free Card", None))
        self.rollDoublePushButton.setText(QCoreApplication.translate("Dialog", u"Roll for a Double", None))
        self.inJailMessageLabel.setText(QCoreApplication.translate("Dialog", u"Display Message Here", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Purchase", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Don't Purchase", None))
        self.normalCardNameLabel.setText(QCoreApplication.translate("Dialog", u"Card Name Here", None))
        self.normalCardColourSetLabel.setText(QCoreApplication.translate("Dialog", u"Colour Set:", None))
        self.normalCardColourDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Card Set Here", None))
        self.normalCardCostLabel.setText(QCoreApplication.translate("Dialog", u"Cost:", None))
        self.normalCardCostDisplayLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.normalCardHouseCostLabel.setText(QCoreApplication.translate("Dialog", u"House Cost:", None))
        self.normalCardHouseCostDisplayLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.normalCardRentLabel.setText(QCoreApplication.translate("Dialog", u"Rent Amounts", None))
        self.normalCardBaseRentLabel.setText(QCoreApplication.translate("Dialog", u"Base Rent:", None))
        self.normalCardBaseAmountLabel.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.normalCardOneLabel.setText(QCoreApplication.translate("Dialog", u"With 1 House:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.normalCardTwoLabel.setText(QCoreApplication.translate("Dialog", u"With 2 Houses:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"With 3 Houses:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"With 4 Houses:", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_22.setText(QCoreApplication.translate("Dialog", u"With 5 Houses:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Purchase", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Don't Purchase", None))
        self.label_43.setText(QCoreApplication.translate("Dialog", u"Card Name Here", None))
        self.label_44.setText(QCoreApplication.translate("Dialog", u"Card Set:", None))
        self.label_45.setText(QCoreApplication.translate("Dialog", u"Travel Square", None))
        self.label_46.setText(QCoreApplication.translate("Dialog", u"Cost:", None))
        self.label_47.setText(QCoreApplication.translate("Dialog", u"\u00a3200", None))
        self.label_50.setText(QCoreApplication.translate("Dialog", u"Rent Amounts", None))
        self.label_53.setText(QCoreApplication.translate("Dialog", u"With 1 Card:", None))
        self.label_54.setText(QCoreApplication.translate("Dialog", u"\u00a325", None))
        self.label_55.setText(QCoreApplication.translate("Dialog", u"With 2 Cards:", None))
        self.label_56.setText(QCoreApplication.translate("Dialog", u"\u00a350", None))
        self.label_57.setText(QCoreApplication.translate("Dialog", u"With 3 Cards:", None))
        self.label_58.setText(QCoreApplication.translate("Dialog", u"\u00a3100", None))
        self.label_59.setText(QCoreApplication.translate("Dialog", u"With 4 Cards:", None))
        self.label_60.setText(QCoreApplication.translate("Dialog", u"\u00a3200", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"Purchase", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"Don't Purchase", None))
        self.label_48.setText(QCoreApplication.translate("Dialog", u"Card Name Here", None))
        self.label_49.setText(QCoreApplication.translate("Dialog", u"Card Set:", None))
        self.label_51.setText(QCoreApplication.translate("Dialog", u"Utility", None))
        self.label_52.setText(QCoreApplication.translate("Dialog", u"Cost:", None))
        self.label_61.setText(QCoreApplication.translate("Dialog", u"\u00a3150", None))
        self.label_62.setText(QCoreApplication.translate("Dialog", u"Rent Amounts", None))
        self.label_63.setText(QCoreApplication.translate("Dialog", u"With 1 Card:", None))
        self.label_64.setText(QCoreApplication.translate("Dialog", u"4 * Current Dice Roll", None))
        self.label_65.setText(QCoreApplication.translate("Dialog", u"With 2 Cards:", None))
        self.label_66.setText(QCoreApplication.translate("Dialog", u"10 * Current Dice Roll", None))
    # retranslateUi

