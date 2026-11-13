# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cats.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(296, 267)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 284, 251))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.LabelOfAppName = QLabel(self.widget)
        self.LabelOfAppName.setObjectName(u"LabelOfAppName")
        self.LabelOfAppName.setStyleSheet(u"margin:25px;\n"
"font: 9pt \"Segoe Script\";\n"
"color: rgb(0, 170, 0)")

        self.verticalLayout.addWidget(self.LabelOfAppName)

        self.GenerateFact = QPushButton(self.widget)
        self.GenerateFact.setObjectName(u"GenerateFact")
        self.GenerateFact.setStyleSheet(u"background-color: rgb(0, 170, 0);\n"
"color:white;\n"
"font: 9pt \"Segoe Script\";")

        self.verticalLayout.addWidget(self.GenerateFact)

        self.FactAboutCats = QLabel(self.widget)
        self.FactAboutCats.setObjectName(u"FactAboutCats")
        self.FactAboutCats.setStyleSheet(u"margin: 10px;\n"
"font: 700 10pt \"Segoe Script\";\n"
"color: rgb(0, 170, 0)")

        self.verticalLayout.addWidget(self.FactAboutCats)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.LabelOfAppName.setText(QCoreApplication.translate("Dialog", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440 \u0444\u0430\u043a\u0442\u043e\u0432 \u043e \u043a\u043e\u0442\u0438\u043a\u0430\u0445", None))
        self.GenerateFact.setText(QCoreApplication.translate("Dialog", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0444\u0430\u043a\u0442....", None))
        self.FactAboutCats.setText(QCoreApplication.translate("Dialog", u"\u0417\u0434\u0435\u0441\u044c \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u0444\u0430\u043a\u0442 \u043e \u043a\u043e\u0442\u0438\u043a\u0430\u0445...", None))
    # retranslateUi

