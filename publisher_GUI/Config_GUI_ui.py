# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config_GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(778, 791)
        self.save_button = QPushButton(Dialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(310, 680, 75, 23))
        self.status_label = QLabel(Dialog)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(250, 730, 241, 31))
        self.key_value_list = QListWidget(Dialog)
        self.key_value_list.setObjectName(u"key_value_list")
        self.key_value_list.setGeometry(QRect(450, 130, 241, 91))
        self.add_button = QPushButton(Dialog)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(700, 150, 71, 23))
        self.add_input_fields = QPushButton(Dialog)
        self.add_input_fields.setObjectName(u"add_input_fields")
        self.add_input_fields.setGeometry(QRect(450, 50, 101, 23))
        self.key_input = QLineEdit(Dialog)
        self.key_input.setObjectName(u"key_input")
        self.key_input.setGeometry(QRect(450, 90, 91, 21))
        self.value_input = QLineEdit(Dialog)
        self.value_input.setObjectName(u"value_input")
        self.value_input.setGeometry(QRect(560, 90, 131, 21))
        self.delete_button = QPushButton(Dialog)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(700, 180, 71, 23))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(31, 41, 401, 601))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 4, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px;")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout.addWidget(self.label_15)

        self.label_16 = QLabel(self.widget)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout.addWidget(self.label_19)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.broker_input = QLineEdit(self.widget)
        self.broker_input.setObjectName(u"broker_input")

        self.verticalLayout_2.addWidget(self.broker_input)

        self.port_input = QLineEdit(self.widget)
        self.port_input.setObjectName(u"port_input")

        self.verticalLayout_2.addWidget(self.port_input)

        self.username_input = QLineEdit(self.widget)
        self.username_input.setObjectName(u"username_input")

        self.verticalLayout_2.addWidget(self.username_input)

        self.password_input = QLineEdit(self.widget)
        self.password_input.setObjectName(u"password_input")

        self.verticalLayout_2.addWidget(self.password_input)

        self.siteid_input = QLineEdit(self.widget)
        self.siteid_input.setObjectName(u"siteid_input")

        self.verticalLayout_2.addWidget(self.siteid_input)

        self.retain_input = QLineEdit(self.widget)
        self.retain_input.setObjectName(u"retain_input")

        self.verticalLayout_2.addWidget(self.retain_input)

        self.topicqos_input = QLineEdit(self.widget)
        self.topicqos_input.setObjectName(u"topicqos_input")

        self.verticalLayout_2.addWidget(self.topicqos_input)

        self.direction_input = QLineEdit(self.widget)
        self.direction_input.setObjectName(u"direction_input")

        self.verticalLayout_2.addWidget(self.direction_input)

        self.batchsize_input = QLineEdit(self.widget)
        self.batchsize_input.setObjectName(u"batchsize_input")

        self.verticalLayout_2.addWidget(self.batchsize_input)

        self.publishinterval_input = QLineEdit(self.widget)
        self.publishinterval_input.setObjectName(u"publishinterval_input")

        self.verticalLayout_2.addWidget(self.publishinterval_input)

        self.publishretryinterval_input = QLineEdit(self.widget)
        self.publishretryinterval_input.setObjectName(u"publishretryinterval_input")

        self.verticalLayout_2.addWidget(self.publishretryinterval_input)

        self.initialdelay_input = QLineEdit(self.widget)
        self.initialdelay_input.setObjectName(u"initialdelay_input")

        self.verticalLayout_2.addWidget(self.initialdelay_input)

        self.delay_input = QLineEdit(self.widget)
        self.delay_input.setObjectName(u"delay_input")

        self.verticalLayout_2.addWidget(self.delay_input)

        self.dbhost_input = QLineEdit(self.widget)
        self.dbhost_input.setObjectName(u"dbhost_input")

        self.verticalLayout_2.addWidget(self.dbhost_input)

        self.dbport_input = QLineEdit(self.widget)
        self.dbport_input.setObjectName(u"dbport_input")

        self.verticalLayout_2.addWidget(self.dbport_input)

        self.dbname_input = QLineEdit(self.widget)
        self.dbname_input.setObjectName(u"dbname_input")

        self.verticalLayout_2.addWidget(self.dbname_input)

        self.dbuser_input = QLineEdit(self.widget)
        self.dbuser_input.setObjectName(u"dbuser_input")

        self.verticalLayout_2.addWidget(self.dbuser_input)

        self.dbpassword_input = QLineEdit(self.widget)
        self.dbpassword_input.setObjectName(u"dbpassword_input")

        self.verticalLayout_2.addWidget(self.dbpassword_input)

        self.passkey_input = QLineEdit(self.widget)
        self.passkey_input.setObjectName(u"passkey_input")

        self.verticalLayout_2.addWidget(self.passkey_input)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.status_label.setText("")
        self.add_button.setText(QCoreApplication.translate("Dialog", u"Add ", None))
        self.add_input_fields.setText(QCoreApplication.translate("Dialog", u"New Property", None))
        self.delete_button.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Broker", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Port", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"UserName", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"siteId", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Retain", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"TopicQos", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Direction", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"BatchSize", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"publish Interval", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"publish Retry Interval", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Initial Delay", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Delay", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"dbHost", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"dbPort", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"dbName", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"dbUser", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"dbPassword", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"PassKey", None))
    # retranslateUi

