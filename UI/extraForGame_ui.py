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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1374, 967)
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
        font = QFont()
        font.setPointSize(10)
        self.mortgageItemButton.setFont(font)
        self.unmortgageItemButton = QPushButton(self.groupBox)
        self.unmortgageItemButton.setObjectName(u"unmortgageItemButton")
        self.unmortgageItemButton.setGeometry(QRect(150, 90, 111, 41))
        self.unmortgageItemButton.setFont(font)
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
        self.buyHouseButton.setFont(font)
        self.sellHouseButton = QPushButton(self.groupBox_2)
        self.sellHouseButton.setObjectName(u"sellHouseButton")
        self.sellHouseButton.setGeometry(QRect(150, 90, 111, 41))
        self.sellHouseButton.setFont(font)
        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(70, 250, 331, 341))
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 91, 41))
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
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
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

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
    # retranslateUi
