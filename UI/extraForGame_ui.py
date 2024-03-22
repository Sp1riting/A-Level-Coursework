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
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 50, 271, 151))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.mortgageSelectionComboBox = QComboBox(self.groupBox)
        self.mortgageSelectionComboBox.addItem("")
        self.mortgageSelectionComboBox.setObjectName(u"mortgageSelectionComboBox")
        self.mortgageSelectionComboBox.setGeometry(QRect(10, 30, 131, 41))
        self.unmortgageSelectionComboBox = QComboBox(self.groupBox)
        self.unmortgageSelectionComboBox.addItem("")
        self.unmortgageSelectionComboBox.setObjectName(u"unmortgageSelectionComboBox")
        self.unmortgageSelectionComboBox.setGeometry(QRect(10, 90, 131, 41))
        self.mortgageItemButton = QPushButton(self.groupBox)
        self.mortgageItemButton.setObjectName(u"mortgageItemButton")
        self.mortgageItemButton.setGeometry(QRect(150, 30, 111, 41))
        font1 = QFont()
        font1.setPointSize(10)
        self.mortgageItemButton.setFont(font1)
        self.unmortgageItemButton = QPushButton(self.groupBox)
        self.unmortgageItemButton.setObjectName(u"unmortgageItemButton")
        self.unmortgageItemButton.setGeometry(QRect(150, 90, 111, 41))
        self.unmortgageItemButton.setFont(font1)
        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(340, 50, 271, 151))
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.buyHouseSelectionComboBox = QComboBox(self.groupBox_2)
        self.buyHouseSelectionComboBox.addItem("")
        self.buyHouseSelectionComboBox.setObjectName(u"buyHouseSelectionComboBox")
        self.buyHouseSelectionComboBox.setGeometry(QRect(10, 30, 131, 41))
        self.sellHouseSelectionComboBox = QComboBox(self.groupBox_2)
        self.sellHouseSelectionComboBox.addItem("")
        self.sellHouseSelectionComboBox.setObjectName(u"sellHouseSelectionComboBox")
        self.sellHouseSelectionComboBox.setGeometry(QRect(10, 90, 131, 41))
        self.buyHouseButton = QPushButton(self.groupBox_2)
        self.buyHouseButton.setObjectName(u"buyHouseButton")
        self.buyHouseButton.setGeometry(QRect(150, 30, 111, 41))
        self.buyHouseButton.setFont(font1)
        self.sellHouseButton = QPushButton(self.groupBox_2)
        self.sellHouseButton.setObjectName(u"sellHouseButton")
        self.sellHouseButton.setGeometry(QRect(150, 90, 111, 41))
        self.sellHouseButton.setFont(font1)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(70, 250, 331, 341))
        font2 = QFont()
        font2.setPointSize(12)
        self.groupBox_3.setFont(font2)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 91, 41))
        font3 = QFont()
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 70, 151, 51))
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 140, 291, 51))
        self.pushButton_3 = QPushButton(self.groupBox_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(70, 210, 191, 51))
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 280, 311, 61))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
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

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setPointSize(16)
        self.label_3.setFont(font5)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_5)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_7)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_9)


        self.verticalLayout.addLayout(self.formLayout)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_12)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_13)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_18)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_15)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_19)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_14)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_21)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.label_20)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_22)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.label_16)


        self.verticalLayout.addLayout(self.formLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

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
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Please select properties below", None))
        self.mortgageSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.mortgageSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.unmortgageSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.unmortgageSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.mortgageItemButton.setText(QCoreApplication.translate("Dialog", u"Mortgage", None))
        self.unmortgageItemButton.setText(QCoreApplication.translate("Dialog", u"Unmortgage", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Please select properties below", None))
        self.buyHouseSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.buyHouseSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.sellHouseSelectionComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Select Property", None))

        self.sellHouseSelectionComboBox.setCurrentText(QCoreApplication.translate("Dialog", u"Select Property", None))
        self.buyHouseButton.setText(QCoreApplication.translate("Dialog", u"Buy House", None))
        self.sellHouseButton.setText(QCoreApplication.translate("Dialog", u"Sell House", None))
        self.groupBox_3.setTitle("")
        self.label.setText(QCoreApplication.translate("Dialog", u"In Jail", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Pay Bail (\u00a350)", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Use Get Out of Jail Free Card", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Roll for a Double", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Display Message Here", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Purchase", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Don't Purchase", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Card Name Here", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Colour Set:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Card Set Here", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Cost:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"House Cost:", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Rent Amounts", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Base Rent:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"With 1 House:", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"\u00a3Amount", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"With 2 Houses:", None))
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

