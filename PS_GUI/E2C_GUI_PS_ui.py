# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'E2C_GUI_PS.ui'
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
        MainWindow.resize(1292, 907)
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
        self.gridLayout_2.setContentsMargins(6, 4, 5, 4)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 80))
        self.widget_2.setStyleSheet(u"background-color: rgb(4, 76, 184);\n"
"border-radius:10px;")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(400, 65))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: white;\n"
"border-radius:10px;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.publisher_button = QRadioButton(self.widget_2)
        self.publisher_button.setObjectName(u"publisher_button")
        self.publisher_button.setMaximumSize(QSize(400, 35))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.publisher_button.setFont(font1)
        self.publisher_button.setLayoutDirection(Qt.LeftToRight)
        self.publisher_button.setStyleSheet(u"color: white;")
        self.publisher_button.setIconSize(QSize(16, 16))
        self.publisher_button.setChecked(True)

        self.horizontalLayout_3.addWidget(self.publisher_button)

        self.subscriber_button = QRadioButton(self.widget_2)
        self.subscriber_button.setObjectName(u"subscriber_button")
        self.subscriber_button.setMaximumSize(QSize(400, 35))
        self.subscriber_button.setFont(font1)
        self.subscriber_button.setStyleSheet(u"color: white;")
        self.subscriber_button.setChecked(False)

        self.horizontalLayout_3.addWidget(self.subscriber_button)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

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

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.widget_2)

        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMouseTracking(True)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setSpacing(12)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(1, -1, -1, 10)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setSpacing(3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_96 = QLabel(self.page)
        self.label_96.setObjectName(u"label_96")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_96.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_96)

        self.label_97 = QLabel(self.page)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_97)

        self.label_98 = QLabel(self.page)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_98)

        self.label_99 = QLabel(self.page)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_99)

        self.label_100 = QLabel(self.page)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_100)

        self.label_101 = QLabel(self.page)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_101)

        self.label_102 = QLabel(self.page)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font2)

        self.verticalLayout_40.addWidget(self.label_102)


        self.horizontalLayout_36.addLayout(self.verticalLayout_40)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.broker_input = QLineEdit(self.page)
        self.broker_input.setObjectName(u"broker_input")
        font3 = QFont()
        font3.setPointSize(10)
        self.broker_input.setFont(font3)
        self.broker_input.setEchoMode(QLineEdit.Normal)
        self.broker_input.setReadOnly(False)
        self.broker_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.broker_input.setClearButtonEnabled(False)

        self.verticalLayout_41.addWidget(self.broker_input)

        self.port_input = QLineEdit(self.page)
        self.port_input.setObjectName(u"port_input")
        self.port_input.setFont(font3)

        self.verticalLayout_41.addWidget(self.port_input)

        self.cleanSession_input = QLineEdit(self.page)
        self.cleanSession_input.setObjectName(u"cleanSession_input")
        self.cleanSession_input.setFont(font3)

        self.verticalLayout_41.addWidget(self.cleanSession_input)

        self.topicqos_input = QLineEdit(self.page)
        self.topicqos_input.setObjectName(u"topicqos_input")
        self.topicqos_input.setFont(font3)

        self.verticalLayout_41.addWidget(self.topicqos_input)

        self.retain_input = QLineEdit(self.page)
        self.retain_input.setObjectName(u"retain_input")
        self.retain_input.setFont(font3)

        self.verticalLayout_41.addWidget(self.retain_input)

        self.username_input = QLineEdit(self.page)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setFont(font3)

        self.verticalLayout_41.addWidget(self.username_input)

        self.password_input = QLineEdit(self.page)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setFont(font3)

        self.verticalLayout_41.addWidget(self.password_input)


        self.horizontalLayout_36.addLayout(self.verticalLayout_41)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setSpacing(3)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_103 = QLabel(self.page)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_103)

        self.label_104 = QLabel(self.page)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_104)

        self.label_105 = QLabel(self.page)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_105)

        self.label_106 = QLabel(self.page)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_106)

        self.label_107 = QLabel(self.page)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_107)

        self.label_108 = QLabel(self.page)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_108)

        self.label_109 = QLabel(self.page)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_109)


        self.horizontalLayout_37.addLayout(self.verticalLayout_42)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.siteid_input = QLineEdit(self.page)
        self.siteid_input.setObjectName(u"siteid_input")
        self.siteid_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.siteid_input)

        self.direction_input = QLineEdit(self.page)
        self.direction_input.setObjectName(u"direction_input")
        self.direction_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.direction_input)

        self.batchsize_input = QLineEdit(self.page)
        self.batchsize_input.setObjectName(u"batchsize_input")
        self.batchsize_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.batchsize_input)

        self.initialdelay_input = QLineEdit(self.page)
        self.initialdelay_input.setObjectName(u"initialdelay_input")
        self.initialdelay_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.initialdelay_input)

        self.delay_input = QLineEdit(self.page)
        self.delay_input.setObjectName(u"delay_input")
        self.delay_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.delay_input)

        self.initialRetryDelay_input = QLineEdit(self.page)
        self.initialRetryDelay_input.setObjectName(u"initialRetryDelay_input")
        self.initialRetryDelay_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.initialRetryDelay_input)

        self.delayRetry_input = QLineEdit(self.page)
        self.delayRetry_input.setObjectName(u"delayRetry_input")
        self.delayRetry_input.setFont(font3)

        self.verticalLayout_43.addWidget(self.delayRetry_input)


        self.horizontalLayout_37.addLayout(self.verticalLayout_43)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setSpacing(3)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_110 = QLabel(self.page)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_110)

        self.label_111 = QLabel(self.page)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_111)

        self.label_112 = QLabel(self.page)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_112)

        self.label_113 = QLabel(self.page)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_113)

        self.label_114 = QLabel(self.page)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_114)

        self.label_115 = QLabel(self.page)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font2)

        self.verticalLayout_44.addWidget(self.label_115)


        self.horizontalLayout_38.addLayout(self.verticalLayout_44)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.dbhost_input = QLineEdit(self.page)
        self.dbhost_input.setObjectName(u"dbhost_input")
        self.dbhost_input.setFont(font3)

        self.verticalLayout_45.addWidget(self.dbhost_input)

        self.dbport_input = QLineEdit(self.page)
        self.dbport_input.setObjectName(u"dbport_input")
        self.dbport_input.setFont(font3)

        self.verticalLayout_45.addWidget(self.dbport_input)

        self.dbname_input = QLineEdit(self.page)
        self.dbname_input.setObjectName(u"dbname_input")
        self.dbname_input.setFont(font3)

        self.verticalLayout_45.addWidget(self.dbname_input)

        self.dbuser_input = QLineEdit(self.page)
        self.dbuser_input.setObjectName(u"dbuser_input")
        self.dbuser_input.setFont(font3)

        self.verticalLayout_45.addWidget(self.dbuser_input)

        self.dbpassword_input = QLineEdit(self.page)
        self.dbpassword_input.setObjectName(u"dbpassword_input")
        self.dbpassword_input.setFont(font3)

        self.verticalLayout_45.addWidget(self.dbpassword_input)

        self.passkey_input = QLineEdit(self.page)
        self.passkey_input.setObjectName(u"passkey_input")
        self.passkey_input.setFont(font3)

        self.verticalLayout_45.addWidget(self.passkey_input)


        self.horizontalLayout_38.addLayout(self.verticalLayout_45)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_38)


        self.gridLayout.addLayout(self.horizontalLayout_35, 0, 0, 1, 1)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(12)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setSpacing(3)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_116 = QLabel(self.page)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_116)

        self.label_117 = QLabel(self.page)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_117)

        self.label_118 = QLabel(self.page)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_118)

        self.label_119 = QLabel(self.page)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_119)

        self.label_120 = QLabel(self.page)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setFont(font2)

        self.verticalLayout_46.addWidget(self.label_120)


        self.horizontalLayout_40.addLayout(self.verticalLayout_46)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.HeartBeatAnalog_input = QLineEdit(self.page)
        self.HeartBeatAnalog_input.setObjectName(u"HeartBeatAnalog_input")
        self.HeartBeatAnalog_input.setFont(font3)

        self.verticalLayout_47.addWidget(self.HeartBeatAnalog_input)

        self.HeartBeatAnalogRetry_input = QLineEdit(self.page)
        self.HeartBeatAnalogRetry_input.setObjectName(u"HeartBeatAnalogRetry_input")
        self.HeartBeatAnalogRetry_input.setFont(font3)

        self.verticalLayout_47.addWidget(self.HeartBeatAnalogRetry_input)

        self.HeartBeatDiscrete_input = QLineEdit(self.page)
        self.HeartBeatDiscrete_input.setObjectName(u"HeartBeatDiscrete_input")
        self.HeartBeatDiscrete_input.setFont(font3)

        self.verticalLayout_47.addWidget(self.HeartBeatDiscrete_input)

        self.HeartBeatDiscreteRetry_input = QLineEdit(self.page)
        self.HeartBeatDiscreteRetry_input.setObjectName(u"HeartBeatDiscreteRetry_input")
        self.HeartBeatDiscreteRetry_input.setFont(font3)

        self.verticalLayout_47.addWidget(self.HeartBeatDiscreteRetry_input)

        self.HeartBeatListenerTimeDiff_input = QLineEdit(self.page)
        self.HeartBeatListenerTimeDiff_input.setObjectName(u"HeartBeatListenerTimeDiff_input")
        self.HeartBeatListenerTimeDiff_input.setFont(font3)

        self.verticalLayout_47.addWidget(self.HeartBeatListenerTimeDiff_input)


        self.horizontalLayout_40.addLayout(self.verticalLayout_47)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setSpacing(3)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_121 = QLabel(self.page)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font2)

        self.verticalLayout_48.addWidget(self.label_121)

        self.label_122 = QLabel(self.page)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font2)

        self.verticalLayout_48.addWidget(self.label_122)

        self.label_123 = QLabel(self.page)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font2)

        self.verticalLayout_48.addWidget(self.label_123)

        self.label_124 = QLabel(self.page)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font2)

        self.verticalLayout_48.addWidget(self.label_124)


        self.horizontalLayout_41.addLayout(self.verticalLayout_48)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.onDemandAnalogListenerTopic_input = QLineEdit(self.page)
        self.onDemandAnalogListenerTopic_input.setObjectName(u"onDemandAnalogListenerTopic_input")
        self.onDemandAnalogListenerTopic_input.setFont(font3)

        self.verticalLayout_49.addWidget(self.onDemandAnalogListenerTopic_input)

        self.onDemandAnalogPublishTopic_input = QLineEdit(self.page)
        self.onDemandAnalogPublishTopic_input.setObjectName(u"onDemandAnalogPublishTopic_input")
        self.onDemandAnalogPublishTopic_input.setFont(font3)

        self.verticalLayout_49.addWidget(self.onDemandAnalogPublishTopic_input)

        self.onDemandDiscreteListenerTopic_input = QLineEdit(self.page)
        self.onDemandDiscreteListenerTopic_input.setObjectName(u"onDemandDiscreteListenerTopic_input")
        self.onDemandDiscreteListenerTopic_input.setFont(font3)

        self.verticalLayout_49.addWidget(self.onDemandDiscreteListenerTopic_input)

        self.onDemandDiscretePublishTopic_input = QLineEdit(self.page)
        self.onDemandDiscretePublishTopic_input.setObjectName(u"onDemandDiscretePublishTopic_input")
        self.onDemandDiscretePublishTopic_input.setFont(font3)

        self.verticalLayout_49.addWidget(self.onDemandDiscretePublishTopic_input)


        self.horizontalLayout_41.addLayout(self.verticalLayout_49)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setSpacing(3)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_125 = QLabel(self.page)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font2)

        self.verticalLayout_50.addWidget(self.label_125)

        self.label_126 = QLabel(self.page)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font2)

        self.verticalLayout_50.addWidget(self.label_126)


        self.horizontalLayout_42.addLayout(self.verticalLayout_50)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.analogTopic_input = QLineEdit(self.page)
        self.analogTopic_input.setObjectName(u"analogTopic_input")
        self.analogTopic_input.setFont(font3)

        self.verticalLayout_51.addWidget(self.analogTopic_input)

        self.discreteTopic_input = QLineEdit(self.page)
        self.discreteTopic_input.setObjectName(u"discreteTopic_input")
        self.discreteTopic_input.setFont(font3)

        self.verticalLayout_51.addWidget(self.discreteTopic_input)


        self.horizontalLayout_42.addLayout(self.verticalLayout_51)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_42)


        self.gridLayout.addLayout(self.horizontalLayout_39, 1, 0, 1, 1)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setSpacing(4)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(2, 2, 2, 2)
        self.newproperty_button = QPushButton(self.page)
        self.newproperty_button.setObjectName(u"newproperty_button")
        self.newproperty_button.setMaximumSize(QSize(130, 28))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.newproperty_button.setFont(font4)
        self.newproperty_button.setLayoutDirection(Qt.LeftToRight)
        self.newproperty_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(28, 105, 202);\n"
"border-radius:5px;\n"
"")

        self.verticalLayout_52.addWidget(self.newproperty_button)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.key_input = QLineEdit(self.page)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setMaximumSize(QSize(170, 30))
        self.key_input.setFont(font3)
        self.key_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.key_input)

        self.value_input = QLineEdit(self.page)
        self.value_input.setObjectName(u"value_input")
        self.value_input.setMaximumSize(QSize(350, 30))
        self.value_input.setFont(font3)
        self.value_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.value_input)


        self.verticalLayout_52.addLayout(self.horizontalLayout_43)

        self.key_value_list = QListWidget(self.page)
        self.key_value_list.setObjectName(u"key_value_list")
        self.key_value_list.setMaximumSize(QSize(350, 100))
        self.key_value_list.setSizeIncrement(QSize(0, 0))
        self.key_value_list.setFont(font3)
        self.key_value_list.setLayoutDirection(Qt.LeftToRight)
        self.key_value_list.setSpacing(2)
        self.key_value_list.setViewMode(QListView.ListMode)

        self.verticalLayout_52.addWidget(self.key_value_list)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setSpacing(30)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.add_button = QPushButton(self.page)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMaximumSize(QSize(100, 35))
        self.add_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(1, 190, 8);\n"
"border-radius:5px;")

        self.horizontalLayout_45.addWidget(self.add_button)

        self.delete_button = QPushButton(self.page)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMaximumSize(QSize(100, 35))
        self.delete_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(218, 32, 32);\n"
"border-radius:5px;")

        self.horizontalLayout_45.addWidget(self.delete_button)


        self.horizontalLayout_44.addLayout(self.horizontalLayout_45)

        self.status_label = QLabel(self.page)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setFont(font1)
        self.status_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.status_label)

        self.save_button = QPushButton(self.page)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMaximumSize(QSize(100, 35))
        self.save_button.setFont(font4)
        self.save_button.setStyleSheet(u"border: 1px solid black;\n"
"border-radius:5px;\n"
"background-color: rgb(96, 171, 16);")

        self.horizontalLayout_44.addWidget(self.save_button)


        self.verticalLayout_52.addLayout(self.horizontalLayout_44)


        self.gridLayout.addLayout(self.verticalLayout_52, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setSpacing(3)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_127 = QLabel(self.page_2)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_127)

        self.label_128 = QLabel(self.page_2)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_128)

        self.label_132 = QLabel(self.page_2)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_132)

        self.label_133 = QLabel(self.page_2)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_133)

        self.label_142 = QLabel(self.page_2)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_142)

        self.label_143 = QLabel(self.page_2)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_143)

        self.label_144 = QLabel(self.page_2)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_144)

        self.label_145 = QLabel(self.page_2)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_145)

        self.label_156 = QLabel(self.page_2)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font2)

        self.verticalLayout_53.addWidget(self.label_156)


        self.horizontalLayout.addLayout(self.verticalLayout_53)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.sub_broker_input = QLineEdit(self.page_2)
        self.sub_broker_input.setObjectName(u"sub_broker_input")
        self.sub_broker_input.setFont(font3)
        self.sub_broker_input.setEchoMode(QLineEdit.Normal)
        self.sub_broker_input.setReadOnly(False)
        self.sub_broker_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.sub_broker_input.setClearButtonEnabled(False)

        self.verticalLayout_54.addWidget(self.sub_broker_input)

        self.sub_port_input = QLineEdit(self.page_2)
        self.sub_port_input.setObjectName(u"sub_port_input")
        self.sub_port_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_port_input)

        self.sub_username_input = QLineEdit(self.page_2)
        self.sub_username_input.setObjectName(u"sub_username_input")
        self.sub_username_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_username_input)

        self.sub_password_input = QLineEdit(self.page_2)
        self.sub_password_input.setObjectName(u"sub_password_input")
        self.sub_password_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_password_input)

        self.sub_initialdelay_input = QLineEdit(self.page_2)
        self.sub_initialdelay_input.setObjectName(u"sub_initialdelay_input")
        self.sub_initialdelay_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_initialdelay_input)

        self.sub_delay_input = QLineEdit(self.page_2)
        self.sub_delay_input.setObjectName(u"sub_delay_input")
        self.sub_delay_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_delay_input)

        self.sub_publishInterval_input = QLineEdit(self.page_2)
        self.sub_publishInterval_input.setObjectName(u"sub_publishInterval_input")
        self.sub_publishInterval_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_publishInterval_input)

        self.sub_publishRetryInterval_input = QLineEdit(self.page_2)
        self.sub_publishRetryInterval_input.setObjectName(u"sub_publishRetryInterval_input")
        self.sub_publishRetryInterval_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_publishRetryInterval_input)

        self.sub_direction_input = QLineEdit(self.page_2)
        self.sub_direction_input.setObjectName(u"sub_direction_input")
        self.sub_direction_input.setFont(font3)

        self.verticalLayout_54.addWidget(self.sub_direction_input)


        self.horizontalLayout.addLayout(self.verticalLayout_54)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setSpacing(3)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_139 = QLabel(self.page_2)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font2)

        self.verticalLayout_61.addWidget(self.label_139)

        self.label_140 = QLabel(self.page_2)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setFont(font2)

        self.verticalLayout_61.addWidget(self.label_140)

        self.label_141 = QLabel(self.page_2)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setFont(font2)

        self.verticalLayout_61.addWidget(self.label_141)

        self.label_146 = QLabel(self.page_2)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font2)

        self.verticalLayout_61.addWidget(self.label_146)

        self.label_147 = QLabel(self.page_2)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setFont(font2)

        self.verticalLayout_61.addWidget(self.label_147)


        self.horizontalLayout_50.addLayout(self.verticalLayout_61)

        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.sub_analogClientId_input = QLineEdit(self.page_2)
        self.sub_analogClientId_input.setObjectName(u"sub_analogClientId_input")
        self.sub_analogClientId_input.setFont(font3)

        self.verticalLayout_62.addWidget(self.sub_analogClientId_input)

        self.sub_discreteClientId_input = QLineEdit(self.page_2)
        self.sub_discreteClientId_input.setObjectName(u"sub_discreteClientId_input")
        self.sub_discreteClientId_input.setFont(font3)

        self.verticalLayout_62.addWidget(self.sub_discreteClientId_input)

        self.sub_heartBeatClient_input = QLineEdit(self.page_2)
        self.sub_heartBeatClient_input.setObjectName(u"sub_heartBeatClient_input")
        self.sub_heartBeatClient_input.setFont(font3)

        self.verticalLayout_62.addWidget(self.sub_heartBeatClient_input)

        self.sub_onDemandAnalogClient_input = QLineEdit(self.page_2)
        self.sub_onDemandAnalogClient_input.setObjectName(u"sub_onDemandAnalogClient_input")
        self.sub_onDemandAnalogClient_input.setFont(font3)

        self.verticalLayout_62.addWidget(self.sub_onDemandAnalogClient_input)

        self.sub_onDemandDiscreteClient_input = QLineEdit(self.page_2)
        self.sub_onDemandDiscreteClient_input.setObjectName(u"sub_onDemandDiscreteClient_input")
        self.sub_onDemandDiscreteClient_input.setFont(font3)

        self.verticalLayout_62.addWidget(self.sub_onDemandDiscreteClient_input)


        self.horizontalLayout_50.addLayout(self.verticalLayout_62)


        self.gridLayout_3.addLayout(self.horizontalLayout_50, 0, 1, 1, 1)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setSpacing(3)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_155 = QLabel(self.page_2)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_155)

        self.label_154 = QLabel(self.page_2)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_154)

        self.label_148 = QLabel(self.page_2)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_148)

        self.label_149 = QLabel(self.page_2)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_149)

        self.label_150 = QLabel(self.page_2)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_150)

        self.label_151 = QLabel(self.page_2)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_151)

        self.label_152 = QLabel(self.page_2)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_152)

        self.label_153 = QLabel(self.page_2)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_153)


        self.horizontalLayout_51.addLayout(self.verticalLayout_63)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.sub_dbDriver_input = QLineEdit(self.page_2)
        self.sub_dbDriver_input.setObjectName(u"sub_dbDriver_input")
        self.sub_dbDriver_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dbDriver_input)

        self.sub_dburl_input = QLineEdit(self.page_2)
        self.sub_dburl_input.setObjectName(u"sub_dburl_input")
        self.sub_dburl_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dburl_input)

        self.sub_dbHost_input = QLineEdit(self.page_2)
        self.sub_dbHost_input.setObjectName(u"sub_dbHost_input")
        self.sub_dbHost_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dbHost_input)

        self.sub_dbPort_input = QLineEdit(self.page_2)
        self.sub_dbPort_input.setObjectName(u"sub_dbPort_input")
        self.sub_dbPort_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dbPort_input)

        self.sub_dbName_input = QLineEdit(self.page_2)
        self.sub_dbName_input.setObjectName(u"sub_dbName_input")
        self.sub_dbName_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dbName_input)

        self.sub_dbUser_input = QLineEdit(self.page_2)
        self.sub_dbUser_input.setObjectName(u"sub_dbUser_input")
        self.sub_dbUser_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dbUser_input)

        self.sub_dbPassword_input = QLineEdit(self.page_2)
        self.sub_dbPassword_input.setObjectName(u"sub_dbPassword_input")
        self.sub_dbPassword_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_dbPassword_input)

        self.sub_passKey_input = QLineEdit(self.page_2)
        self.sub_passKey_input.setObjectName(u"sub_passKey_input")
        self.sub_passKey_input.setFont(font3)

        self.verticalLayout_64.addWidget(self.sub_passKey_input)


        self.horizontalLayout_51.addLayout(self.verticalLayout_64)


        self.gridLayout_3.addLayout(self.horizontalLayout_51, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setSpacing(3)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_129 = QLabel(self.page_2)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font2)

        self.verticalLayout_55.addWidget(self.label_129)

        self.label_130 = QLabel(self.page_2)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setFont(font2)

        self.verticalLayout_55.addWidget(self.label_130)

        self.label_131 = QLabel(self.page_2)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font2)

        self.verticalLayout_55.addWidget(self.label_131)

        self.label_134 = QLabel(self.page_2)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font2)

        self.verticalLayout_55.addWidget(self.label_134)


        self.horizontalLayout_47.addLayout(self.verticalLayout_55)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.sub_HeartBeatAnalog_input = QLineEdit(self.page_2)
        self.sub_HeartBeatAnalog_input.setObjectName(u"sub_HeartBeatAnalog_input")
        self.sub_HeartBeatAnalog_input.setFont(font3)

        self.verticalLayout_56.addWidget(self.sub_HeartBeatAnalog_input)

        self.sub_HeartBeatAnalogRetry_input = QLineEdit(self.page_2)
        self.sub_HeartBeatAnalogRetry_input.setObjectName(u"sub_HeartBeatAnalogRetry_input")
        self.sub_HeartBeatAnalogRetry_input.setFont(font3)

        self.verticalLayout_56.addWidget(self.sub_HeartBeatAnalogRetry_input)

        self.sub_HeartBeatDiscrete_input = QLineEdit(self.page_2)
        self.sub_HeartBeatDiscrete_input.setObjectName(u"sub_HeartBeatDiscrete_input")
        self.sub_HeartBeatDiscrete_input.setFont(font3)

        self.verticalLayout_56.addWidget(self.sub_HeartBeatDiscrete_input)

        self.sub_HeartBeatDiscreteRetry_input = QLineEdit(self.page_2)
        self.sub_HeartBeatDiscreteRetry_input.setObjectName(u"sub_HeartBeatDiscreteRetry_input")
        self.sub_HeartBeatDiscreteRetry_input.setFont(font3)

        self.verticalLayout_56.addWidget(self.sub_HeartBeatDiscreteRetry_input)


        self.horizontalLayout_47.addLayout(self.verticalLayout_56)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setSpacing(3)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_135 = QLabel(self.page_2)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font2)

        self.verticalLayout_57.addWidget(self.label_135)

        self.label_137 = QLabel(self.page_2)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font2)

        self.verticalLayout_57.addWidget(self.label_137)


        self.horizontalLayout_48.addLayout(self.verticalLayout_57)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.sub_onDemandAnalogListenerTopic_input = QLineEdit(self.page_2)
        self.sub_onDemandAnalogListenerTopic_input.setObjectName(u"sub_onDemandAnalogListenerTopic_input")
        self.sub_onDemandAnalogListenerTopic_input.setFont(font3)

        self.verticalLayout_58.addWidget(self.sub_onDemandAnalogListenerTopic_input)

        self.sub_onDemandDiscreteListenerTopic_input = QLineEdit(self.page_2)
        self.sub_onDemandDiscreteListenerTopic_input.setObjectName(u"sub_onDemandDiscreteListenerTopic_input")
        self.sub_onDemandDiscreteListenerTopic_input.setFont(font3)

        self.verticalLayout_58.addWidget(self.sub_onDemandDiscreteListenerTopic_input)


        self.horizontalLayout_48.addLayout(self.verticalLayout_58)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(3)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_136 = QLabel(self.page_2)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setFont(font2)

        self.verticalLayout_59.addWidget(self.label_136)

        self.label_138 = QLabel(self.page_2)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font2)

        self.verticalLayout_59.addWidget(self.label_138)


        self.horizontalLayout_49.addLayout(self.verticalLayout_59)

        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.sub_analogTopic_input = QLineEdit(self.page_2)
        self.sub_analogTopic_input.setObjectName(u"sub_analogTopic_input")
        self.sub_analogTopic_input.setFont(font3)

        self.verticalLayout_60.addWidget(self.sub_analogTopic_input)

        self.sub_discreteTopic_input = QLineEdit(self.page_2)
        self.sub_discreteTopic_input.setObjectName(u"sub_discreteTopic_input")
        self.sub_discreteTopic_input.setFont(font3)

        self.verticalLayout_60.addWidget(self.sub_discreteTopic_input)


        self.horizontalLayout_49.addLayout(self.verticalLayout_60)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_49)


        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setSpacing(4)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(2, 2, 2, 2)
        self.sub_newproperty_button = QPushButton(self.page_2)
        self.sub_newproperty_button.setObjectName(u"sub_newproperty_button")
        self.sub_newproperty_button.setMaximumSize(QSize(130, 28))
        self.sub_newproperty_button.setFont(font4)
        self.sub_newproperty_button.setLayoutDirection(Qt.LeftToRight)
        self.sub_newproperty_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(28, 105, 202);\n"
"border-radius:5px;\n"
"")

        self.verticalLayout_65.addWidget(self.sub_newproperty_button)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.sub_key_input = QLineEdit(self.page_2)
        self.sub_key_input.setObjectName(u"sub_key_input")
        self.sub_key_input.setMaximumSize(QSize(170, 30))
        self.sub_key_input.setFont(font3)
        self.sub_key_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.sub_key_input)

        self.sub_value_input = QLineEdit(self.page_2)
        self.sub_value_input.setObjectName(u"sub_value_input")
        self.sub_value_input.setMaximumSize(QSize(350, 30))
        self.sub_value_input.setFont(font3)
        self.sub_value_input.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.sub_value_input)


        self.verticalLayout_65.addLayout(self.horizontalLayout_52)

        self.sub_key_value_list = QListWidget(self.page_2)
        self.sub_key_value_list.setObjectName(u"sub_key_value_list")
        self.sub_key_value_list.setMaximumSize(QSize(350, 100))
        self.sub_key_value_list.setSizeIncrement(QSize(0, 0))
        self.sub_key_value_list.setFont(font3)
        self.sub_key_value_list.setLayoutDirection(Qt.LeftToRight)
        self.sub_key_value_list.setSpacing(2)
        self.sub_key_value_list.setViewMode(QListView.ListMode)

        self.verticalLayout_65.addWidget(self.sub_key_value_list)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setSpacing(30)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.sub_add_button = QPushButton(self.page_2)
        self.sub_add_button.setObjectName(u"sub_add_button")
        self.sub_add_button.setMaximumSize(QSize(100, 35))
        self.sub_add_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(1, 190, 8);\n"
"border-radius:5px;")

        self.horizontalLayout_54.addWidget(self.sub_add_button)

        self.sub_delete_button = QPushButton(self.page_2)
        self.sub_delete_button.setObjectName(u"sub_delete_button")
        self.sub_delete_button.setMaximumSize(QSize(100, 35))
        self.sub_delete_button.setStyleSheet(u"border: 1px solid black;\n"
"background-color: rgb(218, 32, 32);\n"
"border-radius:5px;")

        self.horizontalLayout_54.addWidget(self.sub_delete_button)


        self.horizontalLayout_53.addLayout(self.horizontalLayout_54)

        self.sub_status_label = QLabel(self.page_2)
        self.sub_status_label.setObjectName(u"sub_status_label")
        self.sub_status_label.setFont(font1)
        self.sub_status_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.sub_status_label)

        self.sub_save_button = QPushButton(self.page_2)
        self.sub_save_button.setObjectName(u"sub_save_button")
        self.sub_save_button.setMaximumSize(QSize(100, 35))
        self.sub_save_button.setFont(font4)
        self.sub_save_button.setStyleSheet(u"border: 1px solid black;\n"
"border-radius:5px;\n"
"background-color: rgb(96, 171, 16);")

        self.horizontalLayout_53.addWidget(self.sub_save_button)


        self.verticalLayout_65.addLayout(self.horizontalLayout_53)


        self.gridLayout_3.addLayout(self.verticalLayout_65, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Edge2Cloud Application", None))
        self.publisher_button.setText(QCoreApplication.translate("MainWindow", u"Publisher", None))
        self.subscriber_button.setText(QCoreApplication.translate("MainWindow", u"Subscriber", None))
        self.label_2.setText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"broker", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"cleanSession", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"topicQos", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"retain", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.broker_input.setInputMask("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"siteId", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"direction", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"batchSize", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"initialDelay", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"delay", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"initialRetryDelay", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"delayRetry", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"dbHost", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"dbPort", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"dbName", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"dbUser", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"dbPassword", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"passKey", None))
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"HeartBeatAnalog", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"HeartBeatAnalogRetry", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"HeartBeatDiscrete", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"HeartBeatDiscreteRetry", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"HeartBeatListenerTimeDiff", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"onDemandAnalogListenerTopic", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"onDemandAnalogPublishTopic", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"onDemandDiscreteListenerTopic", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"onDemandDiscretePublishTopic", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"analogTopic", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"discreteTopic", None))
        self.newproperty_button.setText(QCoreApplication.translate("MainWindow", u"New Property", None))
        self.key_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enetr Key", None))
        self.value_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Value", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.status_label.setText("")
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"broker", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"initialDelay", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"delay", None))
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"publishInterval", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"publishRetryInterval", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"direction", None))
        self.sub_broker_input.setInputMask("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"analogClientId", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"discreteClientId", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"heartBeatClient", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"onDemandAnalogClient", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"onDemandDiscreteClient", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"dbDriver", None))
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"dburl", None))
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"dbHost", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"dbPort", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"dbName", None))
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"dbUser", None))
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"dbPassword", None))
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"passKey", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"HeartBeatAnalog", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"HeartBeatAnalogRetry", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"HeartBeatDiscrete", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"HeartBeatDiscreteRetry", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"onDemandAnalogListenerTopic", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"onDemandDiscreteListenerTopic", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"analogTopic", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"discreteTopic", None))
        self.sub_newproperty_button.setText(QCoreApplication.translate("MainWindow", u"New Property", None))
        self.sub_key_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enetr Key", None))
        self.sub_value_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Value", None))
        self.sub_add_button.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.sub_delete_button.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.sub_status_label.setText("")
        self.sub_save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

