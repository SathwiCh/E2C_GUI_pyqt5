# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'E2C_GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

import Logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1294, 880)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setContentsMargins(6, 0, 5, 4)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 2, 2)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 72))
        self.widget_2.setStyleSheet(u"background-color: rgb(4, 76, 184);\n"
"border-radius:10px;")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white;\n"
"border-radius:10px;")

        self.horizontalLayout_10.addWidget(self.label)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(180, 55))
        self.label_2.setMaximumSize(QSize(300, 55))
        self.label_2.setStyleSheet(u"border-radius:5px;")
        self.label_2.setFrameShape(QFrame.WinPanel)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setPixmap(QPixmap(u":/Lnt/Logo1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.horizontalLayout_10.addWidget(self.label_2)


        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, -1, -1, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_3.setFont(font1)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout.addWidget(self.label_9)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.broker_input = QLineEdit(self.widget)
        self.broker_input.setObjectName(u"broker_input")
        self.broker_input.setEchoMode(QLineEdit.Normal)
        self.broker_input.setReadOnly(False)
        self.broker_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.broker_input.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.broker_input)

        self.port_input = QLineEdit(self.widget)
        self.port_input.setObjectName(u"port_input")

        self.verticalLayout_2.addWidget(self.port_input)

        self.cleanSession_input = QLineEdit(self.widget)
        self.cleanSession_input.setObjectName(u"cleanSession_input")

        self.verticalLayout_2.addWidget(self.cleanSession_input)

        self.topicqos_input = QLineEdit(self.widget)
        self.topicqos_input.setObjectName(u"topicqos_input")

        self.verticalLayout_2.addWidget(self.topicqos_input)

        self.retain_input = QLineEdit(self.widget)
        self.retain_input.setObjectName(u"retain_input")

        self.verticalLayout_2.addWidget(self.retain_input)

        self.username_input = QLineEdit(self.widget)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout_2.addWidget(self.username_input)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout_2.addWidget(self.password_input)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.label_17.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_19)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_20)

        self.label_21 = QLabel(self.widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_22)

        self.label_23 = QLabel(self.widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.verticalLayout_5.addWidget(self.label_23)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.siteid_input = QLineEdit(self.widget)
        self.siteid_input.setObjectName(u"siteid_input")

        self.verticalLayout_6.addWidget(self.siteid_input)

        self.direction_input = QLineEdit(self.widget)
        self.direction_input.setObjectName(u"direction_input")

        self.verticalLayout_6.addWidget(self.direction_input)

        self.batchsize_input = QLineEdit(self.widget)
        self.batchsize_input.setObjectName(u"batchsize_input")

        self.verticalLayout_6.addWidget(self.batchsize_input)

        self.initialdelay_input = QLineEdit(self.widget)
        self.initialdelay_input.setObjectName(u"initialdelay_input")

        self.verticalLayout_6.addWidget(self.initialdelay_input)

        self.delay_input = QLineEdit(self.widget)
        self.delay_input.setObjectName(u"delay_input")

        self.verticalLayout_6.addWidget(self.delay_input)

        self.initialRetryDelay_input = QLineEdit(self.widget)
        self.initialRetryDelay_input.setObjectName(u"initialRetryDelay_input")

        self.verticalLayout_6.addWidget(self.initialRetryDelay_input)

        self.delayRetry_input = QLineEdit(self.widget)
        self.delayRetry_input.setObjectName(u"delayRetry_input")

        self.verticalLayout_6.addWidget(self.delayRetry_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_24 = QLabel(self.widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_25)

        self.label_26 = QLabel(self.widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.verticalLayout_7.addWidget(self.label_27)


        self.horizontalLayout_5.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.dbhost_input = QLineEdit(self.widget)
        self.dbhost_input.setObjectName(u"dbhost_input")

        self.verticalLayout_8.addWidget(self.dbhost_input)

        self.dbport_input = QLineEdit(self.widget)
        self.dbport_input.setObjectName(u"dbport_input")

        self.verticalLayout_8.addWidget(self.dbport_input)

        self.dbname_input = QLineEdit(self.widget)
        self.dbname_input.setObjectName(u"dbname_input")

        self.verticalLayout_8.addWidget(self.dbname_input)

        self.dbuser_input = QLineEdit(self.widget)
        self.dbuser_input.setObjectName(u"dbuser_input")

        self.verticalLayout_8.addWidget(self.dbuser_input)

        self.dbpassword_input = QLineEdit(self.widget)
        self.dbpassword_input.setObjectName(u"dbpassword_input")

        self.verticalLayout_8.addWidget(self.dbpassword_input)

        self.passkey_input = QLineEdit(self.widget)
        self.passkey_input.setObjectName(u"passkey_input")

        self.verticalLayout_8.addWidget(self.passkey_input)


        self.horizontalLayout_5.addLayout(self.verticalLayout_8)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.horizontalLayout_11, 1, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_10.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_13)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_14)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.HeartBeatAnalog_input = QLineEdit(self.widget)
        self.HeartBeatAnalog_input.setObjectName(u"HeartBeatAnalog_input")

        self.verticalLayout_4.addWidget(self.HeartBeatAnalog_input)

        self.HeartBeatAnalogRetry_input = QLineEdit(self.widget)
        self.HeartBeatAnalogRetry_input.setObjectName(u"HeartBeatAnalogRetry_input")

        self.verticalLayout_4.addWidget(self.HeartBeatAnalogRetry_input)

        self.HeartBeatDiscrete_input = QLineEdit(self.widget)
        self.HeartBeatDiscrete_input.setObjectName(u"HeartBeatDiscrete_input")

        self.verticalLayout_4.addWidget(self.HeartBeatDiscrete_input)

        self.HeartBeatDiscreteRetry_input = QLineEdit(self.widget)
        self.HeartBeatDiscreteRetry_input.setObjectName(u"HeartBeatDiscreteRetry_input")

        self.verticalLayout_4.addWidget(self.HeartBeatDiscreteRetry_input)

        self.HeartBeatListenerTimeDiff_input = QLineEdit(self.widget)
        self.HeartBeatListenerTimeDiff_input.setObjectName(u"HeartBeatListenerTimeDiff_input")

        self.verticalLayout_4.addWidget(self.HeartBeatListenerTimeDiff_input)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_28 = QLabel(self.widget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_28)

        self.label_29 = QLabel(self.widget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_29)

        self.label_30 = QLabel(self.widget)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_30)

        self.label_31 = QLabel(self.widget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.verticalLayout_9.addWidget(self.label_31)


        self.horizontalLayout_6.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.onDemandAnalogListenerTopic_input = QLineEdit(self.widget)
        self.onDemandAnalogListenerTopic_input.setObjectName(u"onDemandAnalogListenerTopic_input")

        self.verticalLayout_10.addWidget(self.onDemandAnalogListenerTopic_input)

        self.onDemandAnalogPublishTopic_input = QLineEdit(self.widget)
        self.onDemandAnalogPublishTopic_input.setObjectName(u"onDemandAnalogPublishTopic_input")

        self.verticalLayout_10.addWidget(self.onDemandAnalogPublishTopic_input)

        self.onDemandDiscreteListenerTopic_input = QLineEdit(self.widget)
        self.onDemandDiscreteListenerTopic_input.setObjectName(u"onDemandDiscreteListenerTopic_input")

        self.verticalLayout_10.addWidget(self.onDemandDiscreteListenerTopic_input)

        self.onDemandDiscretePublishTopic_input = QLineEdit(self.widget)
        self.onDemandDiscretePublishTopic_input.setObjectName(u"onDemandDiscretePublishTopic_input")

        self.verticalLayout_10.addWidget(self.onDemandDiscretePublishTopic_input)


        self.horizontalLayout_6.addLayout(self.verticalLayout_10)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_32 = QLabel(self.widget)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_32)

        self.label_33 = QLabel(self.widget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.verticalLayout_11.addWidget(self.label_33)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.analogTopic_input = QLineEdit(self.widget)
        self.analogTopic_input.setObjectName(u"analogTopic_input")

        self.verticalLayout_12.addWidget(self.analogTopic_input)

        self.discreteTopic_input = QLineEdit(self.widget)
        self.discreteTopic_input.setObjectName(u"discreteTopic_input")

        self.verticalLayout_12.addWidget(self.discreteTopic_input)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_7)


        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.newproperty_button = QPushButton(self.widget)
        self.newproperty_button.setObjectName(u"newproperty_button")
        self.newproperty_button.setMaximumSize(QSize(130, 28))
        self.newproperty_button.setFont(font1)
        self.newproperty_button.setLayoutDirection(Qt.LeftToRight)
        self.newproperty_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(28, 105, 202);\n"
"border-radius:5px;\n"
"")

        self.verticalLayout_13.addWidget(self.newproperty_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.key_input = QLineEdit(self.widget)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setMaximumSize(QSize(170, 30))
        self.key_input.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout.addWidget(self.key_input)

        self.value_input = QLineEdit(self.widget)
        self.value_input.setObjectName(u"value_input")
        self.value_input.setMaximumSize(QSize(350, 30))

        self.horizontalLayout.addWidget(self.value_input)


        self.verticalLayout_13.addLayout(self.horizontalLayout)

        self.key_value_list = QListWidget(self.widget)
        self.key_value_list.setObjectName(u"key_value_list")
        self.key_value_list.setMaximumSize(QSize(350, 100))
        self.key_value_list.setSizeIncrement(QSize(0, 0))
        self.key_value_list.setLayoutDirection(Qt.LeftToRight)
        self.key_value_list.setSpacing(2)
        self.key_value_list.setViewMode(QListView.ListMode)

        self.verticalLayout_13.addWidget(self.key_value_list)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(30)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.add_button = QPushButton(self.widget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMaximumSize(QSize(100, 35))
        self.add_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(1, 190, 8);\n"
"border-radius:5px;")

        self.horizontalLayout_8.addWidget(self.add_button)

        self.delete_button = QPushButton(self.widget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMaximumSize(QSize(100, 35))
        self.delete_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(218, 32, 32);\n"
"border-radius:5px;")

        self.horizontalLayout_8.addWidget(self.delete_button)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)

        self.status_label = QLabel(self.widget)
        self.status_label.setObjectName(u"status_label")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.status_label.setFont(font4)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.status_label)

        self.save_button = QPushButton(self.widget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMaximumSize(QSize(100, 35))
        self.save_button.setFont(font1)
        self.save_button.setStyleSheet(u"border: 1px solid black;\n"
"border-radius:5px;\n"
"background-color: rgb(96, 171, 16);")

        self.horizontalLayout_9.addWidget(self.save_button)


        self.verticalLayout_13.addLayout(self.horizontalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout_13, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Edge2Cloud Application", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"broker", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"cleanSession", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"topicQos", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"retain", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.broker_input.setInputMask("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"siteId", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"direction", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"batchSize", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"initialDelay", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"delay", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"initialRetryDelay", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"delayRetry", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"dbHost", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"dbPort", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"dbName", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"dbUser", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"dbPassword", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"passKey", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"HeartBeatAnalog", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"HeartBeatAnalogRetry", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"HeartBeatDiscrete", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"HeartBeatDiscreteRetry", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"HeartBeatListenerTimeDiff", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"onDemandAnalogListenerTopic", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"onDemandAnalogPublishTopic", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"onDemandDiscreteListenerTopic", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"onDemandDiscretePublishTopic", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"analogTopic", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"discreteTopic", None))
        self.newproperty_button.setText(QCoreApplication.translate("MainWindow", u"New Property", None))
        self.key_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enetr Key", None))
        self.value_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Value", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.status_label.setText("")
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

