# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'licenseBgYAGl.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_LicenseForm(object):
    def setupUi(self, LicenseForm):
        if not LicenseForm.objectName():
            LicenseForm.setObjectName(u"LicenseForm")
        LicenseForm.resize(521, 372)
        self.verticalLayout = QVBoxLayout(LicenseForm)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.about_textedit = QTextEdit(LicenseForm)
        self.about_textedit.setObjectName(u"about_textedit")
        self.about_textedit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.about_textedit.setReadOnly(True)

        self.verticalLayout.addWidget(self.about_textedit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.close_button = QPushButton(LicenseForm)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(LicenseForm)
        self.close_button.clicked.connect(LicenseForm.close)

        QMetaObject.connectSlotsByName(LicenseForm)
    # setupUi

    def retranslateUi(self, LicenseForm):
        LicenseForm.setWindowTitle(QCoreApplication.translate("LicenseForm", u"License", None))
        self.close_button.setText(QCoreApplication.translate("LicenseForm", u"Close", None))
    # retranslateUi

