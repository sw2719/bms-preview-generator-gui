# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUfTNBG.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

from ui.dnd_listwidget import DnDListWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 650)
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_check_update = QAction(MainWindow)
        self.action_check_update.setObjectName(u"action_check_update")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)

        self.remove_button = QPushButton(self.centralwidget)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.remove_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.dir_listwidget = DnDListWidget(self.centralwidget)
        self.dir_listwidget.setObjectName(u"dir_listwidget")

        self.verticalLayout.addWidget(self.dir_listwidget)

        self.options_layout = QHBoxLayout()
        self.options_layout.setObjectName(u"options_layout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.options_layout.addWidget(self.label_3)

        self.start_edit = QLineEdit(self.centralwidget)
        self.start_edit.setObjectName(u"start_edit")
        self.start_edit.setPlaceholderText(u"20000")

        self.options_layout.addWidget(self.start_edit)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.options_layout.addWidget(self.label_4)

        self.end_edit = QLineEdit(self.centralwidget)
        self.end_edit.setObjectName(u"end_edit")
        self.end_edit.setPlaceholderText(u"40000")

        self.options_layout.addWidget(self.end_edit)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.options_layout.addWidget(self.label_5)

        self.fade_in_edit = QLineEdit(self.centralwidget)
        self.fade_in_edit.setObjectName(u"fade_in_edit")
        self.fade_in_edit.setPlaceholderText(u"1000")

        self.options_layout.addWidget(self.fade_in_edit)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.options_layout.addWidget(self.label_6)

        self.fade_out_edit = QLineEdit(self.centralwidget)
        self.fade_out_edit.setObjectName(u"fade_out_edit")
        self.fade_out_edit.setPlaceholderText(u"2000")

        self.options_layout.addWidget(self.fade_out_edit)


        self.verticalLayout.addLayout(self.options_layout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.filename_edit = QLineEdit(self.centralwidget)
        self.filename_edit.setObjectName(u"filename_edit")
        self.filename_edit.setPlaceholderText(u"preview_auto_generated.ogg")

        self.horizontalLayout_3.addWidget(self.filename_edit)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.param_edit = QLineEdit(self.centralwidget)
        self.param_edit.setObjectName(u"param_edit")

        self.horizontalLayout_3.addWidget(self.param_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.output_textedit = QPlainTextEdit(self.centralwidget)
        self.output_textedit.setObjectName(u"output_textedit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_textedit.sizePolicy().hasHeightForWidth())
        self.output_textedit.setSizePolicy(sizePolicy)
        self.output_textedit.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout.addWidget(self.output_textedit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.progressbar = QProgressBar(self.centralwidget)
        self.progressbar.setObjectName(u"progressbar")
        self.progressbar.setEnabled(True)
        self.progressbar.setMaximum(0)
        self.progressbar.setValue(0)
        self.progressbar.setTextVisible(True)
        self.progressbar.setInvertedAppearance(False)
        self.progressbar.setFormat(u"%p% (%v/%m)")

        self.horizontalLayout_4.addWidget(self.progressbar)

        self.action_button = QPushButton(self.centralwidget)
        self.action_button.setObjectName(u"action_button")

        self.horizontalLayout_4.addWidget(self.action_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 20))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action_check_update)
        self.menu.addAction(self.action_about)
        self.menu.addSeparator()
        self.menu.addAction(self.action_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BMS Preview Generator GUI", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.action_check_update.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Added directories", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.remove_button.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.start_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.start_edit.setInputMask("")
        self.start_edit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"End", None))
#if QT_CONFIG(tooltip)
        self.end_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.end_edit.setInputMask("")
        self.end_edit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Fade in", None))
#if QT_CONFIG(tooltip)
        self.fade_in_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fade_in_edit.setInputMask("")
        self.fade_in_edit.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Fade out", None))
#if QT_CONFIG(tooltip)
        self.fade_out_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.fade_out_edit.setInputMask("")
        self.fade_out_edit.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"File name", None))
#if QT_CONFIG(tooltip)
        self.filename_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Custom arguments", None))
#if QT_CONFIG(tooltip)
        self.param_edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.param_edit.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Output", None))
        self.action_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

