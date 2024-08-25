# -*- coding: utf-8 -*-
from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
################################################################################
## Form generated from reading UI file 'dokki_hotelXSpyPS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        db.setDatabaseName(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-MEABQQJG;DATABASE=hotel;Trusted_Connection=yes;")
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
"background-color: #6482AD;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: #6482AD;\n"
"}\n"
"\n"
"QDateEdit{\n"
"background-color: #6482AD;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: #6482AD;\n"
"}\n"
"\n"
"QStackedWidget{\n"
"background-color: #2F3645;\n"
"}\n"
"\n"
"")
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
        self.tableGuests.setGeometry(QRect(0, 200, 861, 221))
        self.tableGuests.setStyleSheet(u"")
        self.tableGuests.setGridStyle(Qt.SolidLine)
        self.tableGuests.horizontalHeader().setDefaultSectionSize(110)
        self.guest_id_label = QLabel(self.page)
        self.guest_id_label.setObjectName(u"guest_id_label")
        self.guest_id_label.setGeometry(QRect(10, 10, 71, 16))
        self.frist_name_label = QLabel(self.page)
        self.frist_name_label.setObjectName(u"frist_name_label")
        self.frist_name_label.setGeometry(QRect(10, 40, 81, 16))
        self.last_name_label = QLabel(self.page)
        self.last_name_label.setObjectName(u"last_name_label")
        self.last_name_label.setGeometry(QRect(10, 70, 91, 16))
        self.lineEdit_guest_id = QLineEdit(self.page)
        self.lineEdit_guest_id.setObjectName(u"lineEdit_guest_id")
        self.lineEdit_guest_id.setGeometry(QRect(132, 10, 111, 20))
        self.lineEdit_frist_name = QLineEdit(self.page)
        self.lineEdit_frist_name.setObjectName(u"lineEdit_frist_name")
        self.lineEdit_frist_name.setGeometry(QRect(130, 40, 113, 20))
        self.lineEdit_last_name = QLineEdit(self.page)
        self.lineEdit_last_name.setObjectName(u"lineEdit_last_name")
        self.lineEdit_last_name.setGeometry(QRect(130, 70, 113, 20))
        self.birth_date_label = QLabel(self.page)
        self.birth_date_label.setObjectName(u"birth_date_label")
        self.birth_date_label.setGeometry(QRect(320, 20, 91, 16))
        self.adress_label = QLabel(self.page)
        self.adress_label.setObjectName(u"adress_label")
        self.adress_label.setGeometry(QRect(320, 50, 61, 21))
        self.lineEdit_adress = QLineEdit(self.page)
        self.lineEdit_adress.setObjectName(u"lineEdit_adress")
        self.lineEdit_adress.setGeometry(QRect(440, 50, 113, 20))
        self.phone_label = QLabel(self.page)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(320, 80, 51, 21))
        self.lineEdit_phone = QLineEdit(self.page)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setGeometry(QRect(440, 80, 113, 20))
        self.email_label = QLabel(self.page)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(10, 100, 81, 16))
        self.lineEdit_email = QLineEdit(self.page)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(130, 100, 113, 20))
        self.insert_button_guest = QPushButton(self.page)
        self.insert_button_guest.setObjectName(u"insert_button_guest")
        self.insert_button_guest.setGeometry(QRect(90, 150, 81, 41))
        self.edit_button_guest = QPushButton(self.page)
        self.edit_button_guest.setObjectName(u"edit_button_guest")
        self.edit_button_guest.setGeometry(QRect(300, 150, 81, 41))
        self.delete_button_guest = QPushButton(self.page)
        self.delete_button_guest.setObjectName(u"delete_button_guest")
        self.delete_button_guest.setGeometry(QRect(490, 150, 81, 41))
        self.dateEdit = QDateEdit(self.page)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(440, 20, 110, 22))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableBooking = QTableWidget(self.page_2)
        if (self.tableBooking.columnCount() < 6):
            self.tableBooking.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableBooking.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.tableBooking.setObjectName(u"tableBooking")
        self.tableBooking.setGeometry(QRect(0, 200, 861, 221))
        self.tableBooking.setStyleSheet(u"")
        self.tableBooking.setGridStyle(Qt.SolidLine)
        self.tableBooking.horizontalHeader().setDefaultSectionSize(110)
        self.insert_button_booking = QPushButton(self.page_2)
        self.insert_button_booking.setObjectName(u"insert_button_booking")
        self.insert_button_booking.setGeometry(QRect(90, 150, 81, 41))
        self.edit_button_booking = QPushButton(self.page_2)
        self.edit_button_booking.setObjectName(u"edit_button_booking")
        self.edit_button_booking.setGeometry(QRect(300, 150, 81, 41))
        self.delete_button_booking = QPushButton(self.page_2)
        self.delete_button_booking.setObjectName(u"delete_button_booking")
        self.delete_button_booking.setGeometry(QRect(490, 150, 81, 41))
        self.label_Booking = QLabel(self.page_2)
        self.label_Booking.setObjectName(u"label_Booking")
        self.label_Booking.setGeometry(QRect(20, 20, 91, 16))
        self.label_booking_guest = QLabel(self.page_2)
        self.label_booking_guest.setObjectName(u"label_booking_guest")
        self.label_booking_guest.setGeometry(QRect(20, 60, 61, 16))
        self.label_booking_room = QLabel(self.page_2)
        self.label_booking_room.setObjectName(u"label_booking_room")
        self.label_booking_room.setGeometry(QRect(20, 90, 61, 16))
        self.label_checkin = QLabel(self.page_2)
        self.label_checkin.setObjectName(u"label_checkin")
        self.label_checkin.setGeometry(QRect(360, 20, 101, 16))
        self.label_checkout = QLabel(self.page_2)
        self.label_checkout.setObjectName(u"label_checkout")
        self.label_checkout.setGeometry(QRect(360, 50, 101, 16))
        self.label_totalprice = QLabel(self.page_2)
        self.label_totalprice.setObjectName(u"label_totalprice")
        self.label_totalprice.setGeometry(QRect(360, 90, 81, 21))
        self.lineEdit_booking = QLineEdit(self.page_2)
        self.lineEdit_booking.setObjectName(u"lineEdit_booking")
        self.lineEdit_booking.setGeometry(QRect(132, 20, 111, 20))
        self.lineEdit_booking_guest = QLineEdit(self.page_2)
        self.lineEdit_booking_guest.setObjectName(u"lineEdit_booking_guest")
        self.lineEdit_booking_guest.setGeometry(QRect(130, 60, 111, 20))
        self.lineEdit_booking_room = QLineEdit(self.page_2)
        self.lineEdit_booking_room.setObjectName(u"lineEdit_booking_room")
        self.lineEdit_booking_room.setGeometry(QRect(132, 90, 111, 20))
        self.dateEdit_checkin = QDateEdit(self.page_2)
        self.dateEdit_checkin.setObjectName(u"dateEdit_checkin")
        self.dateEdit_checkin.setGeometry(QRect(490, 20, 110, 22))
        self.dateEdit_checkout = QDateEdit(self.page_2)
        self.dateEdit_checkout.setObjectName(u"dateEdit_checkout")
        self.dateEdit_checkout.setGeometry(QRect(490, 50, 110, 22))
        self.lineEdit_totalPrice = QLineEdit(self.page_2)
        self.lineEdit_totalPrice.setObjectName(u"lineEdit_totalPrice")
        self.lineEdit_totalPrice.setGeometry(QRect(490, 90, 113, 20))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.tableRoom = QTableWidget(self.page_3)
        if (self.tableRoom.columnCount() < 4):
            self.tableRoom.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableRoom.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableRoom.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableRoom.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableRoom.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.tableRoom.setObjectName(u"tableRoom")
        self.tableRoom.setGeometry(QRect(0, 200, 861, 221))
        self.tableRoom.setStyleSheet(u"")
        self.tableRoom.setGridStyle(Qt.SolidLine)
        self.tableRoom.horizontalHeader().setDefaultSectionSize(110)
        self.insert_button_Room = QPushButton(self.page_3)
        self.insert_button_Room.setObjectName(u"insert_button_Room")
        self.insert_button_Room.setGeometry(QRect(90, 150, 81, 41))
        self.edit_button_Room = QPushButton(self.page_3)
        self.edit_button_Room.setObjectName(u"edit_button_Room")
        self.edit_button_Room.setGeometry(QRect(300, 150, 81, 41))
        self.delete_button_Room = QPushButton(self.page_3)
        self.delete_button_Room.setObjectName(u"delete_button_Room")
        self.delete_button_Room.setGeometry(QRect(490, 150, 81, 41))
        self.label_Room_id = QLabel(self.page_3)
        self.label_Room_id.setObjectName(u"label_Room_id")
        self.label_Room_id.setGeometry(QRect(20, 10, 71, 16))
        self.label_Hotell_id = QLabel(self.page_3)
        self.label_Hotell_id.setObjectName(u"label_Hotell_id")
        self.label_Hotell_id.setGeometry(QRect(20, 70, 71, 16))
        self.label_Type_id = QLabel(self.page_3)
        self.label_Type_id.setObjectName(u"label_Type_id")
        self.label_Type_id.setGeometry(QRect(320, 10, 61, 21))
        self.label_statue = QLabel(self.page_3)
        self.label_statue.setObjectName(u"label_statue")
        self.label_statue.setGeometry(QRect(320, 70, 61, 21))
        self.lineEdit_Room_id = QLineEdit(self.page_3)
        self.lineEdit_Room_id.setObjectName(u"lineEdit_Room_id")
        self.lineEdit_Room_id.setGeometry(QRect(120, 10, 113, 20))
        self.lineEdit_Hotell_id = QLineEdit(self.page_3)
        self.lineEdit_Hotell_id.setObjectName(u"lineEdit_Hotell_id")
        self.lineEdit_Hotell_id.setGeometry(QRect(120, 70, 113, 20))
        self.lineEdit_Type_id = QLineEdit(self.page_3)
        self.lineEdit_Type_id.setObjectName(u"lineEdit_Type_id")
        self.lineEdit_Type_id.setGeometry(QRect(410, 10, 113, 20))
        self.comboBox_statue = QComboBox(self.page_3)
        self.comboBox_statue.addItem("")
        self.comboBox_statue.addItem("")
        self.comboBox_statue.setObjectName(u"comboBox_statue")
        self.comboBox_statue.setGeometry(QRect(410, 70, 121, 31))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.tablePayment = QTableWidget(self.page_4)
        if (self.tablePayment.columnCount() < 5):
            self.tablePayment.setColumnCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tablePayment.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tablePayment.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tablePayment.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tablePayment.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tablePayment.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        self.tablePayment.setObjectName(u"tablePayment")
        self.tablePayment.setGeometry(QRect(0, 200, 861, 221))
        self.tablePayment.setStyleSheet(u"")
        self.tablePayment.setGridStyle(Qt.SolidLine)
        self.tablePayment.horizontalHeader().setDefaultSectionSize(110)
        self.insert_button_transactions = QPushButton(self.page_4)
        self.insert_button_transactions.setObjectName(u"insert_button_transactions")
        self.insert_button_transactions.setGeometry(QRect(90, 150, 81, 41))
        self.edit_button_transactions = QPushButton(self.page_4)
        self.edit_button_transactions.setObjectName(u"edit_button_transactions")
        self.edit_button_transactions.setGeometry(QRect(300, 150, 81, 41))
        self.delete_button_transactions = QPushButton(self.page_4)
        self.delete_button_transactions.setObjectName(u"delete_button_transactions")
        self.delete_button_transactions.setGeometry(QRect(490, 150, 81, 41))
        self.label_payment_id = QLabel(self.page_4)
        self.label_payment_id.setObjectName(u"label_payment_id")
        self.label_payment_id.setGeometry(QRect(20, 10, 91, 16))
        self.label_trans_booking_id = QLabel(self.page_4)
        self.label_trans_booking_id.setObjectName(u"label_trans_booking_id")
        self.label_trans_booking_id.setGeometry(QRect(20, 60, 91, 16))
        self.label_amount = QLabel(self.page_4)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setGeometry(QRect(20, 100, 61, 16))
        self.label_paymentDate = QLabel(self.page_4)
        self.label_paymentDate.setObjectName(u"label_paymentDate")
        self.label_paymentDate.setGeometry(QRect(300, 10, 101, 16))
        self.label_paymentMethoud = QLabel(self.page_4)
        self.label_paymentMethoud.setObjectName(u"label_paymentMethoud")
        self.label_paymentMethoud.setGeometry(QRect(300, 60, 121, 16))
        self.lineEdit_payment_id = QLineEdit(self.page_4)
        self.lineEdit_payment_id.setObjectName(u"lineEdit_payment_id")
        self.lineEdit_payment_id.setGeometry(QRect(112, 10, 121, 20))
        self.lineEdit_trans_booking_id = QLineEdit(self.page_4)
        self.lineEdit_trans_booking_id.setObjectName(u"lineEdit_trans_booking_id")
        self.lineEdit_trans_booking_id.setGeometry(QRect(110, 60, 121, 20))
        self.lineEdit_amount = QLineEdit(self.page_4)
        self.lineEdit_amount.setObjectName(u"lineEdit_amount")
        self.lineEdit_amount.setGeometry(QRect(112, 100, 121, 20))
        self.dateEdit_paymentDate = QDateEdit(self.page_4)
        self.dateEdit_paymentDate.setObjectName(u"dateEdit_paymentDate")
        self.dateEdit_paymentDate.setGeometry(QRect(410, 10, 141, 31))
        self.comboBox_paymentMethoud = QComboBox(self.page_4)
        self.comboBox_paymentMethoud.addItem("")
        self.comboBox_paymentMethoud.addItem("")
        self.comboBox_paymentMethoud.addItem("")
        self.comboBox_paymentMethoud.setObjectName(u"comboBox_paymentMethoud")
        self.comboBox_paymentMethoud.setGeometry(QRect(440, 60, 111, 22))
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.tableStaff = QTableWidget(self.page_5)
        if (self.tableStaff.columnCount() < 10):
            self.tableStaff.setColumnCount(10)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(5, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(6, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(7, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(8, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableStaff.setHorizontalHeaderItem(9, __qtablewidgetitem31)
        self.tableStaff.setObjectName(u"tableStaff")
        self.tableStaff.setGeometry(QRect(0, 200, 861, 221))
        self.tableStaff.setStyleSheet(u"")
        self.tableStaff.setGridStyle(Qt.SolidLine)
        self.tableStaff.horizontalHeader().setDefaultSectionSize(85)
        self.insert_button_staff = QPushButton(self.page_5)
        self.insert_button_staff.setObjectName(u"insert_button_staff")
        self.insert_button_staff.setGeometry(QRect(90, 150, 81, 41))
        self.edit_button_staff = QPushButton(self.page_5)
        self.edit_button_staff.setObjectName(u"edit_button_staff")
        self.edit_button_staff.setGeometry(QRect(300, 150, 81, 41))
        self.delete_button_staff = QPushButton(self.page_5)
        self.delete_button_staff.setObjectName(u"delete_button_staff")
        self.delete_button_staff.setGeometry(QRect(490, 150, 81, 41))
        self.label_staff_id = QLabel(self.page_5)
        self.label_staff_id.setObjectName(u"label_staff_id")
        self.label_staff_id.setGeometry(QRect(20, 10, 51, 16))
        self.label_staff_hotel_id = QLabel(self.page_5)
        self.label_staff_hotel_id.setObjectName(u"label_staff_hotel_id")
        self.label_staff_hotel_id.setGeometry(QRect(20, 40, 71, 16))
        self.label_staff_firstname = QLabel(self.page_5)
        self.label_staff_firstname.setObjectName(u"label_staff_firstname")
        self.label_staff_firstname.setGeometry(QRect(20, 70, 81, 16))
        self.label_staff_lastname = QLabel(self.page_5)
        self.label_staff_lastname.setObjectName(u"label_staff_lastname")
        self.label_staff_lastname.setGeometry(QRect(20, 110, 81, 16))
        self.label_salary = QLabel(self.page_5)
        self.label_salary.setObjectName(u"label_salary")
        self.label_salary.setGeometry(QRect(290, 10, 61, 21))
        self.label_postion = QLabel(self.page_5)
        self.label_postion.setObjectName(u"label_postion")
        self.label_postion.setGeometry(QRect(290, 40, 47, 14))
        self.label_staff_birthdate = QLabel(self.page_5)
        self.label_staff_birthdate.setObjectName(u"label_staff_birthdate")
        self.label_staff_birthdate.setGeometry(QRect(290, 70, 101, 16))
        self.label_staff_phone = QLabel(self.page_5)
        self.label_staff_phone.setObjectName(u"label_staff_phone")
        self.label_staff_phone.setGeometry(QRect(290, 100, 51, 16))
        self.label_staff_email = QLabel(self.page_5)
        self.label_staff_email.setObjectName(u"label_staff_email")
        self.label_staff_email.setGeometry(QRect(570, 30, 47, 14))
        self.label_staff_hiredate = QLabel(self.page_5)
        self.label_staff_hiredate.setObjectName(u"label_staff_hiredate")
        self.label_staff_hiredate.setGeometry(QRect(570, 80, 81, 16))
        self.lineEdit_staff_id = QLineEdit(self.page_5)
        self.lineEdit_staff_id.setObjectName(u"lineEdit_staff_id")
        self.lineEdit_staff_id.setGeometry(QRect(112, 10, 121, 20))
        self.lineEdit_staff_hotel_id = QLineEdit(self.page_5)
        self.lineEdit_staff_hotel_id.setObjectName(u"lineEdit_staff_hotel_id")
        self.lineEdit_staff_hotel_id.setGeometry(QRect(112, 40, 121, 20))
        self.lineEdit_staff_firstname = QLineEdit(self.page_5)
        self.lineEdit_staff_firstname.setObjectName(u"lineEdit_staff_firstname")
        self.lineEdit_staff_firstname.setGeometry(QRect(112, 70, 121, 20))
        self.lineEdit_staff_lastname = QLineEdit(self.page_5)
        self.lineEdit_staff_lastname.setObjectName(u"lineEdit_staff_lastname")
        self.lineEdit_staff_lastname.setGeometry(QRect(112, 110, 121, 20))
        self.lineEdit_salary = QLineEdit(self.page_5)
        self.lineEdit_salary.setObjectName(u"lineEdit_salary")
        self.lineEdit_salary.setGeometry(QRect(402, 10, 121, 20))
        self.lineEdit_postion = QLineEdit(self.page_5)
        self.lineEdit_postion.setObjectName(u"lineEdit_postion")
        self.lineEdit_postion.setGeometry(QRect(402, 40, 121, 20))
        self.dateEdit_staff_birthdate = QDateEdit(self.page_5)
        self.dateEdit_staff_birthdate.setObjectName(u"dateEdit_staff_birthdate")
        self.dateEdit_staff_birthdate.setGeometry(QRect(399, 70, 121, 22))
        self.lineEdit_staff_phone = QLineEdit(self.page_5)
        self.lineEdit_staff_phone.setObjectName(u"lineEdit_staff_phone")
        self.lineEdit_staff_phone.setGeometry(QRect(402, 100, 121, 20))
        self.lineEdit_staff_email = QLineEdit(self.page_5)
        self.lineEdit_staff_email.setObjectName(u"lineEdit_staff_email")
        self.lineEdit_staff_email.setGeometry(QRect(670, 30, 113, 20))
        self.dateEdit_staff_hiredate = QDateEdit(self.page_5)
        self.dateEdit_staff_hiredate.setObjectName(u"dateEdit_staff_hiredate")
        self.dateEdit_staff_hiredate.setGeometry(QRect(670, 80, 110, 22))
        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)

        self.fetch_data(self.tableGuests, "Guest_id")
        self.fetch_data(self.tableBooking, "Booking_id")
        self.fetch_data(self.tableRoom, "Room_id")
        self.fetch_data(self.tablePayment, "payment_id")
        self.fetch_data(self.tableStaff, "staff_id")

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
        self.frist_name_label.setText(QCoreApplication.translate("MainWindow", u"first_name", None))
        self.last_name_label.setText(QCoreApplication.translate("MainWindow", u"last_name", None))
        self.birth_date_label.setText(QCoreApplication.translate("MainWindow", u"dateOfBirth", None))
        self.adress_label.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"phone", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.insert_button_guest.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.edit_button_guest.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button_guest.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem7 = self.tableBooking.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Booking_id", None));
        ___qtablewidgetitem8 = self.tableBooking.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Guest_id", None));
        ___qtablewidgetitem9 = self.tableBooking.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"room_id", None));
        ___qtablewidgetitem10 = self.tableBooking.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"checkInDate", None));
        ___qtablewidgetitem11 = self.tableBooking.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"CheckOutDate", None));
        ___qtablewidgetitem12 = self.tableBooking.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Totalprice", None));
        self.insert_button_booking.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.edit_button_booking.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button_booking.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_Booking.setText(QCoreApplication.translate("MainWindow", u"Booking_id", None))
        self.label_booking_guest.setText(QCoreApplication.translate("MainWindow", u"Guest_id", None))
        self.label_booking_room.setText(QCoreApplication.translate("MainWindow", u"room_id", None))
        self.label_checkin.setText(QCoreApplication.translate("MainWindow", u"checkInDate", None))
        self.label_checkout.setText(QCoreApplication.translate("MainWindow", u"CheckOutDate", None))
        self.label_totalprice.setText(QCoreApplication.translate("MainWindow", u"Totalprice", None))
        ___qtablewidgetitem13 = self.tableRoom.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Room_id", None));
        ___qtablewidgetitem14 = self.tableRoom.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Hotell_id", None));
        ___qtablewidgetitem15 = self.tableRoom.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Type_id", None));
        ___qtablewidgetitem16 = self.tableRoom.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"statue", None));
        self.insert_button_Room.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.edit_button_Room.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button_Room.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_Room_id.setText(QCoreApplication.translate("MainWindow", u"Room_id", None))
        self.label_Hotell_id.setText(QCoreApplication.translate("MainWindow", u"Hotell_id", None))
        self.label_Type_id.setText(QCoreApplication.translate("MainWindow", u"Type_id", None))
        self.label_statue.setText(QCoreApplication.translate("MainWindow", u"statue", None))
        self.comboBox_statue.setItemText(0, QCoreApplication.translate("MainWindow", u"luxury", None))
        self.comboBox_statue.setItemText(1, QCoreApplication.translate("MainWindow", u"economy", None))

        ___qtablewidgetitem17 = self.tablePayment.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"payment_id", None));
        ___qtablewidgetitem18 = self.tablePayment.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Booking_id", None));
        ___qtablewidgetitem19 = self.tablePayment.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem20 = self.tablePayment.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"paymentDate", None));
        ___qtablewidgetitem21 = self.tablePayment.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"paymentMethoud", None));
        self.insert_button_transactions.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.edit_button_transactions.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button_transactions.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_payment_id.setText(QCoreApplication.translate("MainWindow", u"payment_id", None))
        self.label_trans_booking_id.setText(QCoreApplication.translate("MainWindow", u"Booking_id", None))
        self.label_amount.setText(QCoreApplication.translate("MainWindow", u"Amount", None))
        self.label_paymentDate.setText(QCoreApplication.translate("MainWindow", u"paymentDate", None))
        self.label_paymentMethoud.setText(QCoreApplication.translate("MainWindow", u"paymentMethod", None))
        self.comboBox_paymentMethoud.setItemText(0, QCoreApplication.translate("MainWindow", u"Cash", None))
        self.comboBox_paymentMethoud.setItemText(1, QCoreApplication.translate("MainWindow", u"Visa", None))
        self.comboBox_paymentMethoud.setItemText(2, QCoreApplication.translate("MainWindow", u"InstaPay", None))

        ___qtablewidgetitem22 = self.tableStaff.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"staff_id", None));
        ___qtablewidgetitem23 = self.tableStaff.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"hotell_id", None));
        ___qtablewidgetitem24 = self.tableStaff.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"frist_name", None));
        ___qtablewidgetitem25 = self.tableStaff.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"last_name", None));
        ___qtablewidgetitem26 = self.tableStaff.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Salary", None));
        ___qtablewidgetitem27 = self.tableStaff.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Position", None));
        ___qtablewidgetitem28 = self.tableStaff.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Date_Of_Birth", None));
        ___qtablewidgetitem29 = self.tableStaff.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"phone", None));
        ___qtablewidgetitem30 = self.tableStaff.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem31 = self.tableStaff.horizontalHeaderItem(9)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Hire_Date", None));
        self.insert_button_staff.setText(QCoreApplication.translate("MainWindow", u"Insert", None))
        self.edit_button_staff.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.delete_button_staff.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_staff_id.setText(QCoreApplication.translate("MainWindow", u"staff_id", None))
        self.label_staff_hotel_id.setText(QCoreApplication.translate("MainWindow", u"hotell_id", None))
        self.label_staff_firstname.setText(QCoreApplication.translate("MainWindow", u"first_name", None))
        self.label_staff_lastname.setText(QCoreApplication.translate("MainWindow", u"last_name", None))
        self.label_salary.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.label_postion.setText(QCoreApplication.translate("MainWindow", u"Postion", None))
        self.label_staff_birthdate.setText(QCoreApplication.translate("MainWindow", u"Date_Of_Birth", None))
        self.label_staff_phone.setText(QCoreApplication.translate("MainWindow", u"phone", None))
        self.label_staff_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_staff_hiredate.setText(QCoreApplication.translate("MainWindow", u"Hire_Date", None))
    # retranslateUi
        self.insert_button_guest.clicked.connect(self.insert_row_guest)
        self.edit_button_guest.clicked.connect(self.edit_data_guest)
        self.delete_button_guest.clicked.connect(lambda: self.delete_data(self.tableGuests, self.getColName(self.tableGuests)))

        self.insert_button_booking.clicked.connect(self.insert_row_booking)
        self.edit_button_booking.clicked.connect(self.edit_data_booking)
        self.delete_button_booking.clicked.connect(lambda: self.delete_data(self.tableBooking, self.getColName(self.tableBooking)))

        self.insert_button_Room.clicked.connect(self.insert_row_room)
        self.edit_button_Room.clicked.connect(self.edit_data_room)
        self.delete_button_Room.clicked.connect(lambda: self.delete_data(self.tableRoom, self.getColName(self.tableRoom)))

        self.insert_button_transactions.clicked.connect(self.insert_row_payment)
        self.edit_button_transactions.clicked.connect(self.edit_data_payment)
        self.delete_button_transactions.clicked.connect(lambda: self.delete_data(self.tablePayment, self.getColName(self.tablePayment)))

        self.insert_button_staff.clicked.connect(self.insert_row_staff)
        self.edit_button_staff.clicked.connect(self.edit_data_staff)
        self.delete_button_staff.clicked.connect(lambda: self.delete_data(self.tableStaff, self.getColName(self.tableStaff)))

    def clear_inputs(self , table):
            self.getLineEdit(self.getColName(table)).clear()

    def insert_row_guest(self):
            try:
                    print("Getting data...")
                    guest_id = self.lineEdit_guest_id.text()
                    fname = self.lineEdit_frist_name.text()
                    lname = self.lineEdit_last_name.text()
                    date = self.dateEdit.date().toString('yyyy-MM-dd')
                    address = self.lineEdit_adress.text()
                    phone = self.lineEdit_phone.text()
                    email = self.lineEdit_email.text()

                    print("Inserting data into the database...")
                    query = QSqlQuery()
                    query.prepare(
                            "INSERT INTO guest (Guest_id, frist_name, last_name, dateOfBirth, adress, phone, Email) VALUES (?, ?, ?, ?, ?, ?, ?)")
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

    def edit_data_guest(self):
            try:
                    guest_id = self.lineEdit_guest_id.text()

                    if not guest_id:
                            print("No Guest ID provided")
                            return

                    # Search for the row with the given Guest_id
                    row_found = False
                    for row in range(self.tableGuests.rowCount()):
                            if self.tableGuests.item(row, 0) and self.tableGuests.item(row, 0).text() == guest_id:
                                    selected_row = row
                                    row_found = True
                                    break

                    if not row_found:
                            print("Guest ID not found in table")
                            return

                    # Populate data fields with existing data
                    print(selected_row)
                    print("Retrieving data")
                    self.tableGuests.item(selected_row, 1).text()
                    self.tableGuests.item(selected_row, 2).text()
                    self.tableGuests.item(selected_row, 3).text()
                    self.tableGuests.item(selected_row, 4).text()
                    self.tableGuests.item(selected_row, 5).text()
                    self.tableGuests.item(selected_row, 6).text()

                    print("Populating data")
                    newfn = self.lineEdit_frist_name.text()
                    newln = self.lineEdit_last_name.text()
                    newbd = self.dateEdit.date().toString('yyyy-MM-dd')
                    newad = self.lineEdit_adress.text()
                    newph = self.lineEdit_phone.text()
                    newem = self.lineEdit_email.text()

                    # Update the database
                    print("Updating data")
                    query = QSqlQuery()
                    query.prepare(
                            "UPDATE guest SET frist_name = ?, last_name = ?, dateOfBirth = ?, adress = ?, phone = ?, Email = ? WHERE Guest_id = ?")
                    query.addBindValue(newfn)
                    query.addBindValue(newln)
                    query.addBindValue(newbd)
                    query.addBindValue(newad)
                    query.addBindValue(newph)
                    query.addBindValue(newem)
                    query.addBindValue(guest_id)
                    query.exec()


                    if not query.exec():
                            print("SQL Error:", query.lastError().text())
                            return


                    # Refresh the table data to reflect changes
                    print("Refreshing table data")
                    self.fetch_data(self.tableGuests, self.getColName(self.tableGuests))

            except Exception as e:
                    print("Error:", e)

                ###########################################################
    def insert_row_booking(self):
            try:
                    print("Getting data...")
                    booking_id = self.lineEdit_booking.text()
                    guest_id = self.lineEdit_booking_guest.text()
                    room_id = self.lineEdit_booking_room.text()
                    checkInDate = self.dateEdit_checkin.date().toString('yyyy-MM-dd')
                    checkOutDate = self.dateEdit_checkout.date().toString('yyyy-MM-dd')
                    totalPrice = self.lineEdit_totalPrice.text()


                    print("Inserting data into the database...")
                    query = QSqlQuery()
                    query.prepare(
                            "INSERT INTO guest (Booking_id, Guest_id, room_id, checkInDate, CheckOutDate, Totalprice) VALUES (?, ?, ?, ?, ?, ?)")
                    query.addBindValue(booking_id)
                    query.addBindValue(guest_id)
                    query.addBindValue(room_id)
                    query.addBindValue(checkInDate)
                    query.addBindValue(checkOutDate)
                    query.addBindValue(totalPrice)


                    if query.exec():
                            print("Inserting data into QTableWidget...")
                            row_position = self.tableBooking.rowCount()
                            self.tableBooking.insertRow(row_position)

                            self.tableBooking.setItem(row_position, 0, QTableWidgetItem(booking_id))
                            self.tableBooking.setItem(row_position, 1, QTableWidgetItem(guest_id))
                            self.tableBooking.setItem(row_position, 2, QTableWidgetItem(room_id))
                            self.tableBooking.setItem(row_position, 3, QTableWidgetItem(checkInDate))
                            self.tableBooking.setItem(row_position, 4, QTableWidgetItem(checkOutDate))
                            self.tableBooking.setItem(row_position, 5, QTableWidgetItem(totalPrice))
                    else:
                            # Handle any errors, for example:
                            print("Error inserting data: ", query.lastError().text())
            except Exception as e:
                    print("Error:", e)

    def edit_data_booking(self):
            try:
                    booking_id = self.lineEdit_booking.text()

                    if not booking_id:
                            print("No Booking ID provided")
                            return

                    # Search for the row with the given Guest_id
                    row_found = False
                    for row in range(self.tableBooking.rowCount()):
                            if self.tableBooking.item(row, 0) and self.tableBooking.item(row, 0).text() == booking_id:
                                    selected_row = row
                                    row_found = True
                                    break

                    if not row_found:
                            print("Guest ID not found in table")
                            return

                    # Populate data fields with existing data
                    print(selected_row)
                    print("Retrieving data")
                    self.tableBooking.item(selected_row, 1).text()
                    self.tableBooking.item(selected_row, 2).text()
                    self.tableBooking.item(selected_row, 3).text()
                    self.tableBooking.item(selected_row, 4).text()
                    self.tableBooking.item(selected_row, 5).text()

                    print("Populating data")
                    newgi = self.lineEdit_booking_guest.text()
                    newri = self.lineEdit_booking_room.text()
                    newcid = self.dateEdit_checkin.date().toString('yyyy-MM-dd')
                    newcod = self.dateEdit_checkout.date().toString('yyyy-MM-dd')
                    newtp = self.lineEdit_totalPrice.text()

                    # Update the database
                    print("Updating data")
                    query = QSqlQuery()
                    query.prepare(
                            "UPDATE Booking SET Guest_id = ?, room_id = ?, checkInDate = ?, CheckOutDate = ?, Totalprice = ? WHERE Booking_id = ?")
                    query.addBindValue(newgi)
                    query.addBindValue(newri)
                    query.addBindValue(newcid)
                    query.addBindValue(newcod)
                    query.addBindValue(newtp)
                    query.addBindValue(booking_id)
                    query.exec()


                    if not query.exec():
                            print("SQL Error:", query.lastError().text())
                            return


                    # Refresh the table data to reflect changes
                    print("Refreshing table data")
                    self.fetch_data(self.tableBooking, self.getColName(self.tableBooking))

            except Exception as e:
                    print("Error:", e)

                ###########################################################
    def insert_row_room(self):
            try:
                    print("Getting data...")
                    Room_id = self.lineEdit_Room_id.text()
                    Hotel_id = self.lineEdit_Hotell_id.text()
                    Type_id = self.lineEdit_Type_id.text()
                    statue = self.comboBox_statue.currentText()

                    print("Inserting data into the database...")
                    query = QSqlQuery()
                    query.prepare(
                            "INSERT INTO room (Room_id, Hotell_id, Type_id, statue) VALUES (?, ?, ?, ?)")
                    query.addBindValue(Room_id)
                    query.addBindValue(Hotel_id)
                    query.addBindValue(Type_id)
                    query.addBindValue(statue)


                    if query.exec():
                            print("Inserting data into QTableWidget...")
                            row_position = self.tableRoom.rowCount()
                            self.tableGuests.insertRow(row_position)

                            self.tableRoom.setItem(row_position, 0, QTableWidgetItem(Room_id))
                            self.tableRoom.setItem(row_position, 1, QTableWidgetItem(Hotel_id))
                            self.tableRoom.setItem(row_position, 2, QTableWidgetItem(Type_id))
                            self.tableRoom.setItem(row_position, 3, QTableWidgetItem(statue))



                    else:
                            # Handle any errors, for example:
                            print("Error inserting data: ", query.lastError().text())
            except Exception as e:
                    print("Error:", e)

    def edit_data_room(self):
            try:
                    room_id = self.lineEdit_Room_id.text()

                    if not room_id:
                            print("No Room ID provided")
                            return

                    # Search for the row with the given Guest_id
                    row_found = False
                    for row in range(self.tableRoom.rowCount()):
                            if self.tableRoom.item(row, 0) and self.tableRoom.item(row, 0).text() == room_id:
                                    selected_row = row
                                    row_found = True
                                    break

                    if not row_found:
                            print("Room ID not found in table")
                            return

                    # Populate data fields with existing data
                    print(selected_row)
                    print("Retrieving data")
                    self.tableRoom.item(selected_row, 1).text()
                    self.tableRoom.item(selected_row, 2).text()
                    self.tableRoom.item(selected_row, 3).text()


                    print("Populating data")
                    newhi = self.lineEdit_Hotell_id.text()
                    newti = self.lineEdit_Type_id.text()
                    newst = self.comboBox_statue.currentText()


                    # Update the database
                    print("Updating data")
                    query = QSqlQuery()
                    query.prepare(
                            "UPDATE room SET Hotell_id = ?, Type_id = ?, statue = ? WHERE Room_id = ?")
                    query.addBindValue(newhi)
                    query.addBindValue(newti)
                    query.addBindValue(newst)
                    query.addBindValue(room_id)
                    query.exec()


                    if not query.exec():
                            print("SQL Error:", query.lastError().text())
                            return


                    # Refresh the table data to reflect changes
                    print("Refreshing table data")
                    self.fetch_data(self.tableRoom, self.getColName(self.tableRoom))

            except Exception as e:
                    print("Error:", e)

                ###########################################################
    def insert_row_payment(self):
            try:
                    print("Getting data...")
                    payment_id = self.lineEdit_payment_id.text()
                    booking_id = self.lineEdit_trans_booking_id.text()
                    amount = self.lineEdit_amount.text()
                    paymentDate = self.dateEdit_paymentDate.date().toString('yyyy-MM-dd')
                    paymentMethod = self.comboBox_paymentMethoud.currentText()

                    print("Inserting data into the database...")
                    query = QSqlQuery()
                    query.prepare(
                            "INSERT INTO payment (payment_id, Booking_id, Amount, paymentDate, paymentMethoud) VALUES (?, ?, ?, ?, ?)")
                    query.addBindValue(payment_id)
                    query.addBindValue(booking_id)
                    query.addBindValue(amount)
                    query.addBindValue(paymentDate)
                    query.addBindValue(paymentMethod)

                    if query.exec():
                            print("Inserting data into QTableWidget...")
                            row_position = self.tablePayment.rowCount()
                            self.tablePayment.insertRow(row_position)

                            self.tablePayment.setItem(row_position, 0, QTableWidgetItem(payment_id))
                            self.tablePayment.setItem(row_position, 1, QTableWidgetItem(booking_id))
                            self.tablePayment.setItem(row_position, 2, QTableWidgetItem(amount))
                            self.tablePayment.setItem(row_position, 3, QTableWidgetItem(paymentDate))
                            self.tablePayment.setItem(row_position, 4, QTableWidgetItem(paymentMethod))



                    else:
                            # Handle any errors, for example:
                            print("Error inserting data: ", query.lastError().text())
            except Exception as e:
                    print("Error:", e)

    def edit_data_payment(self):
            try:
                    payment_id = self.lineEdit_payment_id.text()

                    if not payment_id:
                            print("No Guest ID provided")
                            return

                    # Search for the row with the given Guest_id
                    row_found = False
                    for row in range(self.tablePayment.rowCount()):
                            if self.tablePayment.item(row, 0) and self.tablePayment.item(row, 0).text() == payment_id:
                                    selected_row = row
                                    row_found = True
                                    break

                    if not row_found:
                            print("Payment ID not found in table")
                            return

                    # Populate data fields with existing data
                    print(selected_row)
                    print("Retrieving data")
                    self.tablePayment.item(selected_row, 1).text()
                    self.tablePayment.item(selected_row, 2).text()
                    self.tablePayment.item(selected_row, 3).text()
                    self.tablePayment.item(selected_row, 4).text()


                    print("Populating data")
                    newbi = self.lineEdit_trans_booking_id.text()
                    newam = self.lineEdit_amount.text()
                    newpd = self.dateEdit_paymentDate.date().toString('yyyy-MM-dd')
                    newpm = self.comboBox_paymentMethoud.currentText()


                    # Update the database
                    print("Updating data")
                    query = QSqlQuery()
                    query.prepare(
                            "UPDATE payment SET Booking_id = ?, Amount = ?, paymentDate = ?, paymentMethoud = ? WHERE payment_id = ?")
                    query.addBindValue(newbi)
                    query.addBindValue(newam)
                    query.addBindValue(newpd)
                    query.addBindValue(newpm)
                    query.addBindValue(payment_id)
                    query.exec()


                    if not query.exec():
                            print("SQL Error:", query.lastError().text())
                            return


                    # Refresh the table data to reflect changes
                    print("Refreshing table data")
                    self.fetch_data(self.tablePayment, self.getColName(self.tablePayment))

            except Exception as e:
                    print("Error:", e)

                ###########################################################

    def insert_row_staff(self):
            try:
                    print("Getting data...")
                    staff_id = self.lineEdit_staff_id.text()
                    hotel_id = self.lineEdit_staff_hotel_id.text()
                    sfname = self.lineEdit_staff_firstname.text()
                    slname = self.lineEdit_staff_lastname.text()
                    salary = self.lineEdit_salary.text()
                    postion = self.lineEdit_postion.text()
                    sBirthDate = self.dateEdit_staff_birthdate.date().toString('yyyy-MM-dd')
                    sphone = self.lineEdit_staff_phone.text()
                    semail = self.lineEdit_staff_email.text()
                    sHireDate = self.dateEdit_staff_hiredate.date().toString('yyyy-MM-dd')

                    print("Inserting data into the database...")
                    query = QSqlQuery()
                    query.prepare(
                            "INSERT INTO staff (staff_id, hotel_id, frist_name, last_name, Salary, Position, Date_Of_Birth, phone, Email, Hire_Date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
                    query.addBindValue(staff_id)
                    query.addBindValue(hotel_id)
                    query.addBindValue(sfname)
                    query.addBindValue(slname)
                    query.addBindValue(salary)
                    query.addBindValue(postion)
                    query.addBindValue(sBirthDate)
                    query.addBindValue(sphone)
                    query.addBindValue(semail)
                    query.addBindValue(sHireDate)

                    if query.exec():
                            print("Inserting data into QTableWidget...")
                            row_position = self.tableStaff.rowCount()
                            self.tableStaff.insertRow(row_position)

                            self.tableStaff.setItem(row_position, 0, QTableWidgetItem(staff_id))
                            self.tableStaff.setItem(row_position, 1, QTableWidgetItem(hotel_id))
                            self.tableStaff.setItem(row_position, 2, QTableWidgetItem(sfname))
                            self.tableStaff.setItem(row_position, 3, QTableWidgetItem(slname))
                            self.tableStaff.setItem(row_position, 4, QTableWidgetItem(salary))
                            self.tableStaff.setItem(row_position, 5, QTableWidgetItem(postion))
                            self.tableStaff.setItem(row_position, 6, QTableWidgetItem(sBirthDate))
                            self.tableStaff.setItem(row_position, 7, QTableWidgetItem(sphone))
                            self.tableStaff.setItem(row_position, 8, QTableWidgetItem(semail))
                            self.tableStaff.setItem(row_position, 9, QTableWidgetItem(sHireDate))


                    else:
                            # Handle any errors, for example:
                            print("Error inserting data: ", query.lastError().text())
            except Exception as e:
                    print("Error:", e)

    def edit_data_staff(self):
            try:
                    staff_id = self.lineEdit_staff_id.text()

                    if not staff_id:
                            print("No Guest ID provided")
                            return

                    # Search for the row with the given Guest_id
                    row_found = False
                    for row in range(self.tableStaff.rowCount()):
                            if self.tableStaff.item(row, 0) and self.tableStaff.item(row, 0).text() == staff_id:
                                    selected_row = row
                                    row_found = True
                                    break

                    if not row_found:
                            print("Staff ID not found in table")
                            return

                    # Populate data fields with existing data
                    print(selected_row)
                    print("Retrieving data")
                    self.tableStaff.item(selected_row, 1).text()
                    self.tableStaff.item(selected_row, 2).text()
                    self.tableStaff.item(selected_row, 3).text()
                    self.tableStaff.item(selected_row, 4).text()
                    self.tableStaff.item(selected_row, 5).text()
                    self.tableStaff.item(selected_row, 6).text()
                    self.tableStaff.item(selected_row, 7).text()
                    self.tableStaff.item(selected_row, 8).text()
                    self.tableStaff.item(selected_row, 9).text()

                    print("Populating data")
                    newhi = self.lineEdit_staff_hotel_id.text()
                    newsfn = self.lineEdit_staff_firstname.text()
                    newsln = self.lineEdit_staff_lastname.text()
                    newsl = self.lineEdit_salary.text()
                    newpos = self.lineEdit_postion.text()
                    newsbd = self.dateEdit_staff_birthdate.date().toString('yyyy-MM-dd')
                    newsph = self.lineEdit_staff_phone.text()
                    newsem = self.lineEdit_staff_email.text()
                    newshd = self.dateEdit_staff_hiredate.date().toString('yyyy-MM-dd')



                    # Update the database
                    print("Updating data")
                    query = QSqlQuery()
                    query.prepare(
                            "UPDATE staff SET hotell_id , frist_name = ?, last_name = ?, Salary, Position, Date_Of_Birth = ?, phone = ?, Email = ?, Hire_Date = ? WHERE staff_id = ?")
                    query.addBindValue(newhi)
                    query.addBindValue(newsfn)
                    query.addBindValue(newsln)
                    query.addBindValue(newsl)
                    query.addBindValue(newpos)
                    query.addBindValue(newsbd)
                    query.addBindValue(newsph)
                    query.addBindValue(newsem)
                    query.addBindValue(newshd)
                    query.addBindValue(staff_id)
                    query.exec()


                    if not query.exec():
                            print("SQL Error:", query.lastError().text())
                            return


                    # Refresh the table data to reflect changes
                    print("Refreshing table data")
                    self.fetch_data(self.tableStaff, self.getColName(self.tableStaff))

            except Exception as e:
                    print("Error:", e)

                ###########################################################

    def delete_data(self, table_name, pColumn):

            try:
                    prim_id = self.getLineEdit(pColumn).text()

                    if not prim_id:
                            print("No Primary ID provided")
                            return

                    # Prepare and execute the delete query
                    query = QSqlQuery()
                    query.prepare(f"DELETE FROM {self.getTableName(table_name)} WHERE {pColumn} = ?")
                    query.addBindValue(prim_id)

                    if not query.exec():
                            print("SQL Error:", query.lastError().text())
                            return

                    print("Deleting data")
                    # Refresh the table data to reflect changes
                    self.fetch_data(table_name, self.getColName(table_name))

                    # Optionally, clear the input fields after deleting
                    self.clear_inputs(table_name)

            except Exception as e:
                    print("Error:", e)
    def getTableName(self, table):
            if table == self.tableGuests:
                    return "guest"
            elif table == self.tableBooking:
                    return "Booking"
            elif table == self.tableRoom:
                    return "room"
            elif table == self.tablePayment:
                    return "payment"
            elif table == self.tableStaff:
                    return "staff"

    def getColName(self, table):
            if table == self.tableGuests:
                    return "Guest_id"
            elif table == self.tableBooking:
                    return "Booking_id"
            elif table == self.tableRoom:
                    return "Room_id"
            elif table == self.tablePayment:
                    return "payment_id"
            elif table == self.tableStaff:
                    return "staff_id"

    def getLineEdit(self, pColumn):
            if pColumn == "Guest_id":
                    return self.lineEdit_guest_id
            elif pColumn == "Booking_id":
                    return self.lineEdit_booking
            elif pColumn == "Room_id":
                    return self.lineEdit_Room_id
            elif pColumn == "payment_id":
                    return self.lineEdit_payment_id
            elif pColumn == "staff_id":
                    return self.lineEdit_staff_id
    def fetch_data(self, table, pColumn):
            # Clear the table before inserting new rows
            table.setRowCount(0)

            query = QSqlQuery()
            if not query.exec(f"SELECT * FROM {self.getTableName(table)} ORDER BY {pColumn} ASC"):
                    print("SQL Error:", query.lastError().text())
                    return

            row = 0
            while query.next():
                    table.insertRow(row)
                    for col_index in range(query.record().count()):
                            value = query.value(col_index)

                            if isinstance(value, QDate):
                                    item = QTableWidgetItem(value.toString('yyyy-MM-dd'))
                            else:
                                    item = QTableWidgetItem(str(value))

                            table.setItem(row, col_index, item)
                    row += 1
                        ##########################################