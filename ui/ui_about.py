# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutDhTDBL.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_AboutForm(object):
    def setupUi(self, AboutForm):
        if not AboutForm.objectName():
            AboutForm.setObjectName(u"AboutForm")
        AboutForm.resize(445, 228)
        self.verticalLayout = QVBoxLayout(AboutForm)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.top_label = QLabel(AboutForm)
        self.top_label.setObjectName(u"top_label")
        self.top_label.setText(u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:700;\">BmsPreviewAudioGeneratorGUI</span></p></body></html>")

        self.verticalLayout.addWidget(self.top_label)

        self.version_label = QLabel(AboutForm)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setText(u"Version")

        self.verticalLayout.addWidget(self.version_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(AboutForm)
        self.label.setObjectName(u"label")
        self.label.setFrameShadow(QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setText(u"<html><head/><body><p>Copyright (c) 2024 Shinwoo Kim (sw2719)</p><p>Licensed under the MIT License</p><p>This software comes with absolutely no warranty.</p></body></html>")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setMargin(0)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(AboutForm)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.github_button = QPushButton(AboutForm)
        self.github_button.setObjectName(u"github_button")
        self.github_button.setFlat(True)

        self.horizontalLayout.addWidget(self.github_button)

        self.license_button = QPushButton(AboutForm)
        self.license_button.setObjectName(u"license_button")
        self.license_button.setFlat(True)

        self.horizontalLayout.addWidget(self.license_button)

        self.close_button = QPushButton(AboutForm)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AboutForm)
        self.close_button.clicked.connect(AboutForm.close)

        QMetaObject.connectSlotsByName(AboutForm)
    # setupUi

    def retranslateUi(self, AboutForm):
        AboutForm.setWindowTitle(QCoreApplication.translate("AboutForm", u"About", None))
        self.label_3.setText(QCoreApplication.translate("AboutForm", u"<html><head/><body><p><span style=\" font-size:8pt;\">Click 'View license' to read this program and included softwares' license.</span></p></body></html>", None))
        self.github_button.setText(QCoreApplication.translate("AboutForm", u"Open GitHub repo", None))
        self.license_button.setText(QCoreApplication.translate("AboutForm", u"View license", None))
        self.close_button.setText(QCoreApplication.translate("AboutForm", u"Close", None))
    # retranslateUi

