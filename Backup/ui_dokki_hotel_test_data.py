# -*- coding: utf-8 -*-
from PyQt5 import QtCore
################################################################################
## Form generated from reading UI file 'dokki_hotelwrklfT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import icons_rc
import newicons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 700)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        db = QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName("DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-MEABQQJG;DATABASE=hotel;Trusted_Connection=yes;")
        if db.open():
                print("Connected to", db.databaseName())
        self.centralwidget.setStyleSheet(u"*{\n"
"border: none;\n"
"background-color: transparent;\n"
"color: #fff;\n"
"}\n"
"#centralwidget{ \n"
"background-color: #7FA1C3;\n"
"}\n"
"#side_menu{\n"
"background-color: #2F3645;\n"
"border-radius: 15px;\n"
"}\n"
"QPushButton {\n"
"padding: 10px;\n"
"background-color: #6482AD;\n"
"border-radius: 5px;\n"
"}\n"
"#main_body{\n"
"background-color: #F5EDED;\n"
"border-radius: 15px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 50))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        self.pushButton.setMaximumSize(QSize(16777215, 35))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/newicons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(28, 0, 301, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QFrame(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setFrameShape(QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 0))
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/newicons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/newicons/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/newicons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/icons/newicons/dollar-sign.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setFlat(False)

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/newicons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.side_menu, 0, Qt.AlignLeft)

        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy1)
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_body)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.tableGuests = QTableWidget(self.page)
        if (self.tableGuests.columnCount() < 7):
            self.tableGuests.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableGuests.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableGuests.setObjectName(u"tableGuests")
        self.tableGuests.setGeometry(QRect(0, 190, 601, 211))
        self.tableGuests.setStyleSheet(u"")
        self.tableGuests.setGridStyle(Qt.SolidLine)
        self.tableGuests.horizontalHeader().setDefaultSectionSize(85)
        self.guest_id_label = QLabel(self.page)
        self.guest_id_label.setObjectName(u"guest_id_label")
        self.guest_id_label.setGeometry(QRect(10, 10, 51, 16))
        self.frist_name_label = QLabel(self.page)
        self.frist_name_label.setObjectName(u"frist_name_label")
        self.frist_name_label.setGeometry(QRect(10, 50, 61, 16))
        self.last_name_label = QLabel(self.page)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setGeometry(QRect(10, 80, 71, 16))
        self.lineEdit_guest_id = QLineEdit(self.page)
        self.lineEdit_guest_id.setObjectName(u"lineEdit_guest_id")
        self.lineEdit_guest_id.setGeometry(QRect(80, 10, 113, 20))
        self.lineEdit_frist_name = QLineEdit(self.page)
        self.lineEdit_frist_name.setObjectName(u"lineEdit_frist_name")
        self.lineEdit_frist_name.setGeometry(QRect(80, 50, 113, 20))
        self.lineEdit_last_name = QLineEdit(self.page)
        self.lineEdit_last_name.setObjectName(u"lineEdit_last_name")
        self.lineEdit_last_name.setGeometry(QRect(80, 80, 113, 20))
        self.birth_date_label = QLabel(self.page)
        self.birth_date_label.setObjectName(u"birth_date_label")
        self.birth_date_label.setGeometry(QRect(290, 10, 61, 16))
        self.lineEdit_birth_date = QLineEdit(self.page)
        self.lineEdit_birth_date.setObjectName(u"lineEdit_birth_date")
        self.lineEdit_birth_date.setGeometry(QRect(370, 10, 113, 20))
        self.adress_label = QLabel(self.page)
        self.adress_label.setObjectName(u"adress_label")
        self.adress_label.setGeometry(QRect(290, 50, 47, 14))
        self.lineEdit_adress = QLineEdit(self.page)
        self.lineEdit_adress.setObjectName(u"lineEdit_adress")
        self.lineEdit_adress.setGeometry(QRect(360, 50, 113, 20))
        self.phone_label = QLabel(self.page)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(290, 80, 47, 14))
        self.lineEdit_phone = QLineEdit(self.page)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setGeometry(QRect(360, 80, 113, 20))
        self.email_label = QLabel(self.page)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(10, 110, 31, 16))
        self.lineEdit_email = QLineEdit(self.page)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(80, 110, 113, 20))
        self.insert_button_guest = QPushButton(self.page)
        self.insert_button_guest.setObjectName(u"insert_button_guest")
        self.insert_button_guest.setGeometry(QRect(80, 150, 75, 31))
        self.edit_button_guest = QPushButton(self.page)
        self.edit_button_guest.setObjectName(u"edit_button_guest")
        self.edit_button_guest.setGeometry(QRect(230, 150, 75, 31))
        self.delete_button_guest = QPushButton(self.page)
        self.delete_button_guest.setObjectName(u"delete_button_guest")
        self.delete_button_guest.setGeometry(QRect(380, 150, 75, 31))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.fetch_data()





        self.side_menu_num = 0

        self.pushButton.clicked.connect(lambda: self.side_menu_def_0())

        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))

    def side_menu_def_0(self):
            if self.side_menu_num == 0:
                    self.animation1 = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
                    self.animation1.setDuration(500)
                    self.animation1.setStartValue(300)
                    self.animation1.setEndValue(80)
                    self.animation1.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation2 = QtCore.QPropertyAnimation(self.pushButton_2, b"maximumWidth")
                    self.animation2.setDuration(500)
                    self.animation2.setStartValue(300)
                    self.animation2.setEndValue(70)
                    self.pushButton_2.setText("")
                    self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation3 = QtCore.QPropertyAnimation(self.pushButton_3, b"maximumWidth")
                    self.animation3.setDuration(500)
                    self.animation3.setStartValue(300)
                    self.animation3.setEndValue(70)
                    self.pushButton_3.setText("")
                    self.animation3.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation4 = QtCore.QPropertyAnimation(self.pushButton_4, b"maximumWidth")
                    self.animation4.setDuration(500)
                    self.animation4.setStartValue(300)
                    self.animation4.setEndValue(70)
                    self.pushButton_4.setText("")
                    self.animation4.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation5 = QtCore.QPropertyAnimation(self.pushButton_5, b"maximumWidth")
                    self.animation5.setDuration(500)
                    self.animation5.setStartValue(300)
                    self.animation5.setEndValue(70)
                    self.pushButton_5.setText("")
                    self.animation5.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation6 = QtCore.QPropertyAnimation(self.pushButton_6, b"maximumWidth")
                    self.animation6.setDuration(500)
                    self.animation6.setStartValue(300)
                    self.animation6.setEndValue(70)
                    self.pushButton_6.setText("")
                    self.animation6.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation1.start()
                    self.animation2.start()
                    self.animation3.start()
                    self.animation4.start()
                    self.animation5.start()
                    self.animation6.start()

                    self.side_menu_num = 1
            else:
                    self.animation11 = QtCore.QPropertyAnimation(self.side_menu, b"maximumWidth")
                    self.animation11.setDuration(500)
                    self.animation11.setStartValue(80)
                    self.animation11.setEndValue(300)
                    self.animation11.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation22 = QtCore.QPropertyAnimation(self.pushButton_2, b"maximumWidth")
                    self.animation22.setDuration(500)
                    self.animation22.setStartValue(70)
                    self.animation22.setEndValue(300)
                    self.pushButton_2.setText("Guests")
                    self.animation22.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation33 = QtCore.QPropertyAnimation(self.pushButton_3, b"maximumWidth")
                    self.animation33.setDuration(500)
                    self.animation33.setStartValue(70)
                    self.animation33.setEndValue(300)
                    self.pushButton_3.setText("Booking")
                    self.animation33.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation44 = QtCore.QPropertyAnimation(self.pushButton_4, b"maximumWidth")
                    self.animation44.setDuration(500)
                    self.animation44.setStartValue(70)
                    self.animation44.setEndValue(300)
                    self.pushButton_4.setText("Rooms")
                    self.animation44.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation55 = QtCore.QPropertyAnimation(self.pushButton_5, b"maximumWidth")
                    self.animation55.setDuration(500)
                    self.animation55.setStartValue(70)
                    self.animation55.setEndValue(300)
                    self.pushButton_5.setText("Transactions")
                    self.animation55.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation66 = QtCore.QPropertyAnimation(self.pushButton_6, b"maximumWidth")
                    self.animation66.setDuration(500)
                    self.animation66.setStartValue(70)
                    self.animation66.setEndValue(300)
                    self.pushButton_6.setText("Staff")
                    self.animation66.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

                    self.animation11.start()
                    self.animation22.start()
                    self.animation33.start()
                    self.animation44.start()
                    self.animation55.start()
                    self.animation66.start()

                    self.side_menu_num = 0


    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dokki Hotel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Guests", None))
#if QT_CONFIG(shortcut)
        self.pushButton_2.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Booking", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Rooms", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Transactions", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        ___qtablewidgetitem = self.tableGuests.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Guest_id", None));
        ___qtablewidgetitem1 = self.tableGuests.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"frist_name", None));
        ___qtablewidgetitem2 = self.tableGuests.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"last_name", None));
        ___qtablewidgetitem3 = self.tableGuests.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"dateOfBirth", None));
        ___qtablewidgetitem4 = self.tableGuests.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem5 = self.tableGuests.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"phone", None));
        ___qtablewidgetitem6 = self.tableGuests.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.guest_id_label.setText(QCoreApplication.translate("MainWindow", u"Guest_id", None))
        self.frist_name_label.setText(QCoreApplication.translate("MainWindow", u"frist_name", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"last_name", None))
        self.birth_date_label.setText(QCoreApplication.translate("MainWindow", u"dateOfBirth", None))
        self.adress_label.setText(QCoreApplication.translate("MainWindow", u"Adress", None))
        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"phone", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.insert_button_guest.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.edit_button_guest.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button_guest.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

        self.insert_button_guest.clicked.connect(self.insert_row)

    def insert_row(self):
        try:
            print("Getting data...")
            guest_id = self.lineEdit_guest_id.text()
            fname = self.lineEdit_frist_name.text()
            lname = self.lineEdit_last_name.text()
            date = self.lineEdit_birth_date.date().toString('yyyy-MM-dd')
            address = self.lineEdit_adress.text()
            phone = self.lineEdit_phone.text()
            email = self.lineEdit_email.text()

            print("Inserting data into the database...")
            query = QSqlQuery()
            query.prepare("INSERT INTO guest (Guest_id, frist_name, last_name, dateOfBirth, adress, phone, Email) VALUES (?, ?, ?, ?, ?, ?, ?)")
            query.addBindValue(guest_id)
            query.addBindValue(fname)
            query.addBindValue(lname)
            query.addBindValue(date)
            query.addBindValue(address)
            query.addBindValue(phone)
            query.addBindValue(email)

            if query.exec():
                    print("Inserting data into QTableWidget...")
                    row_position = self.tableGuests.rowCount()
                    self.tableGuests.insertRow(row_position)

                    self.tableGuests.setItem(row_position, 0, QTableWidgetItem(guest_id))
                    self.tableGuests.setItem(row_position, 1, QTableWidgetItem(fname))
                    self.tableGuests.setItem(row_position, 2, QTableWidgetItem(lname))
                    self.tableGuests.setItem(row_position, 3, QTableWidgetItem(date))
                    self.tableGuests.setItem(row_position, 4, QTableWidgetItem(address))
                    self.tableGuests.setItem(row_position, 5, QTableWidgetItem(phone))
                    self.tableGuests.setItem(row_position, 6, QTableWidgetItem(email))

            else:
                    # Handle any errors, for example:
                    print("Error inserting data: ", query.lastError().text())
        except Exception as e:
                print("Error:", e)



    def fetch_data(self):
            query = QSqlQuery()
            query.exec("SELECT * FROM guest ORDER BY Guest_id ASC")

            row = 0
            while query.next():
                    self.tableGuests.insertRow(row)
                    for col_index in range(query.record().count()):
                            value = query.value(col_index)

                            if isinstance(value, QDate):
                                    item = QTableWidgetItem(value.toString('yyyy-MM-dd'))
                            else:
                                    item = QTableWidgetItem(str(value))

                            self.tableGuests.setItem(row, col_index, item)
                    row += 1