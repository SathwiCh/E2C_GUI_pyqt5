import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QLineEdit, QListWidget
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import configparser
from E2C_GUI_PS import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.key_value_list.itemDoubleClicked.connect(self.edit_item)
        # self.ui.sub_key_value_list.itemDoubleClicked.connect(self.edit_item)
        self.ui.key_value_list.itemDoubleClicked.connect(self.edit_item)
        self.ui.sub_key_value_list.itemDoubleClicked.connect(self.edit_item)

#PUBLISHER
#######################################################################
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.publisher_button.setChecked(True)
        self.ui.key_input.setHidden(True)
        self.ui.value_input.setHidden(True)

        # Connect the "Save" button to the save function
        self.ui.save_button.clicked.connect(self.save_values_publisher)
        self.ui.add_button.clicked.connect(self.add_key_value_pair_publisher)
        self.ui.newproperty_button.clicked.connect(self.show_input_fields_publisher)
        self.ui.delete_button.clicked.connect(self.delete_selected_item_publisher)

        config_file_path = 'C:\\Users\\20339181\\OneDrive - L&T Construction\\Documents\\Pyqt5_GUI\\publisher_GUI\\config.properties'
        # Load the properties file
        self.config = configparser.ConfigParser()
        # self.config.read('config.properties')
        self.config.read(config_file_path)

        # Set initial values in the UI from the properties file
        self.ui.broker_input.setText(self.config.get('Broker', 'broker'))
        self.ui.port_input.setText(self.config.get('Broker', 'port'))
        self.ui.cleanSession_input.setText(self.config.get('Broker','cleanSession'))
        self.ui.topicqos_input.setText(self.config.get('Broker', 'topicQos'))
        self.ui.retain_input.setText(self.config.get('Broker', 'retain'))
        self.ui.username_input.setText(self.config.get('Broker', 'username'))
        self.ui.password_input.setText(self.config.get('Broker', 'password'))       
        self.ui.siteid_input.setText(self.config.get('Data', 'siteId'))
        self.ui.direction_input.setText(self.config.get('Data', 'direction'))
        self.ui.batchsize_input.setText(self.config.get('Data', 'batchSize'))
        # self.ui.publishinterval_input.setText(self.config.get('Data', 'publishinterval'))
        # self.ui.publishretryinterval_input.setText(self.config.get('Data', 'publishretryinterval'))
        self.ui.initialdelay_input.setText(self.config.get('Data', 'initialDelay'))
        self.ui.delay_input.setText(self.config.get('Data', 'delay'))
        self.ui.initialRetryDelay_input.setText(self.config.get('Data', 'initialRetryDelay'))
        self.ui.delayRetry_input.setText(self.config.get('Data', 'delayRetry'))
        self.ui.HeartBeatListenerTimeDiff_input.setText(self.config.get('Data', 'heartBeatListenerTimeDifference'))
        self.ui.HeartBeatAnalog_input.setText(self.config.get('HeartBeatTopics', 'heartBeatAnalog'))
        self.ui.HeartBeatAnalogRetry_input.setText(self.config.get('HeartBeatTopics', 'heartBeatAnalogRetry'))
        self.ui.HeartBeatDiscrete_input.setText(self.config.get('HeartBeatTopics', 'heartBeatDiscrete'))
        self.ui.HeartBeatDiscreteRetry_input.setText(self.config.get('HeartBeatTopics', 'heartBeatDiscreteRetry'))      
        self.ui.dbhost_input.setText(self.config.get('Database', 'dbHost'))
        self.ui.dbport_input.setText(self.config.get('Database', 'dbPort'))
        self.ui.dbname_input.setText(self.config.get('Database', 'dbName'))
        self.ui.dbuser_input.setText(self.config.get('Database', 'dbUser'))
        self.ui.dbpassword_input.setText(self.config.get('Database', 'dbPassword'))
        self.ui.passkey_input.setText(self.config.get('Database', 'passKey'))
        self.ui.analogTopic_input.setText(self.config.get('DataTopics', 'analogTopic'))
        self.ui.discreteTopic_input.setText(self.config.get('DataTopics', 'discreteTopic'))
        self.ui.onDemandAnalogListenerTopic_input.setText(self.config.get('OnDemandTopics', 'onDemandAnalogListenerTopic'))
        self.ui.onDemandAnalogPublishTopic_input.setText(self.config.get('OnDemandTopics', 'onDemandAnalogPublishTopic'))
        self.ui.onDemandDiscreteListenerTopic_input.setText(self.config.get('OnDemandTopics', 'onDemandDiscreteListenerTopic'))
        self.ui.onDemandDiscretePublishTopic_input.setText(self.config.get('OnDemandTopics', 'onDemandDiscretePublishTopic'))
#####################################################################################

# SUBSCRIBER
#####################################################################################
        self.ui.sub_key_input.setHidden(True)
        self.ui.sub_value_input.setHidden(True)

        self.ui.sub_save_button.clicked.connect(self.save_values_subscriber)
        self.ui.sub_add_button.clicked.connect(self.add_key_value_pair_subscriber)
        self.ui.sub_newproperty_button.clicked.connect(self.show_input_fields_subscriber)
        self.ui.sub_delete_button.clicked.connect(self.delete_selected_item_subscriber) 

        config_file_path_sub = 'C:\\Users\\20339181\\OneDrive - L&T Construction\\Documents\\Pyqt5_GUI\\subscriber_GUI\\config.properties'
        # Load the properties file
        self.config1 = configparser.ConfigParser()
        # self.config.read('config.properties')
        self.config1.read(config_file_path_sub)

        self.ui.sub_broker_input.setText(self.config1.get('BrokerData', 'broker'))
        self.ui.sub_port_input.setText(self.config1.get('BrokerData', 'port'))
        self.ui.sub_username_input.setText(self.config1.get('BrokerData', 'username'))
        self.ui.sub_password_input.setText(self.config1.get('BrokerData', 'password'))
        self.ui.sub_initialdelay_input.setText(self.config1.get('BrokerData', 'initialDelay'))
        self.ui.sub_delay_input.setText(self.config1.get('BrokerData', 'delay'))
        self.ui.sub_publishInterval_input.setText(self.config1.get('BrokerData', 'publishInterval'))
        self.ui.sub_publishRetryInterval_input.setText(self.config1.get('BrokerData', 'publishRetryInterval'))
        self.ui.sub_direction_input.setText(self.config1.get('BrokerData','direction'))
        self.ui.sub_HeartBeatAnalog_input.setText(self.config1.get('HeartBeatTopics', 'heartBeatAnalog'))
        self.ui.sub_HeartBeatAnalogRetry_input.setText(self.config1.get('HeartBeatTopics', 'heartBeatAnalogRetry'))
        self.ui.sub_HeartBeatDiscrete_input.setText(self.config1.get('HeartBeatTopics', 'heartBeatDiscrete'))
        self.ui.sub_HeartBeatDiscreteRetry_input.setText(self.config1.get('HeartBeatTopics', 'heartBeatDiscreteRetry'))
        self.ui.sub_onDemandAnalogListenerTopic_input.setText(self.config1.get('OnDemandTopics', 'onDemandAnalogListenerTopic'))
        self.ui.sub_onDemandDiscreteListenerTopic_input.setText(self.config1.get('OnDemandTopics', 'onDemandDiscreteListenerTopic'))
        self.ui.sub_analogTopic_input.setText(self.config1.get('DataTopics', 'analogTopic'))
        self.ui.sub_discreteTopic_input.setText(self.config1.get('DataTopics', 'discreteTopic'))
        self.ui.sub_analogClientId_input.setText(self.config1.get('ClientIds', 'analogClientId'))
        self.ui.sub_discreteClientId_input.setText(self.config1.get('ClientIds', 'discreteClientId'))
        self.ui.sub_heartBeatClient_input.setText(self.config1.get('ClientIds', 'heartBeatClient'))
        self.ui.sub_onDemandAnalogClient_input.setText(self.config1.get('ClientIds', 'onDemandAnalogClient'))
        self.ui.sub_onDemandDiscreteClient_input.setText(self.config1.get('ClientIds', 'onDemandDiscreteClient'))
        self.ui.sub_dbDriver_input.setText(self.config1.get('Database', 'dbDriver'))
        self.ui.sub_dburl_input.setText(self.config1.get('Database', 'dburl'))
        self.ui.sub_dbHost_input.setText(self.config1.get('Database', 'dbHost'))
        self.ui.sub_dbPort_input.setText(self.config1.get('Database', 'dbPort'))
        self.ui.sub_dbName_input.setText(self.config1.get('Database', 'dbName'))
        self.ui.sub_dbUser_input.setText(self.config1.get('Database', 'dbUser'))
        self.ui.sub_dbPassword_input.setText(self.config1.get('Database', 'dbPassword'))
        self.ui.sub_passKey_input.setText(self.config1.get('Database', 'passKey'))

    def on_publisher_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(0)    
    def on_subscriber_button_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(1)   
   
    def show_input_fields_publisher(self):
        # Show the input fields when the button is clicked
        self.ui.key_input.setHidden(False)
        self.ui.value_input.setHidden(False)
    def show_input_fields_subscriber(self):
        # Show the input fields when the button is clicked
        self.ui.sub_key_input.setHidden(False)
        self.ui.sub_value_input.setHidden(False)
    
    def add_key_value_pair_publisher(self):
        key = self.ui.key_input.text()
        value = self.ui.value_input.text()
        # if key and value:
        #     self.ui.key_value_list.addItem(f"{key}: {value}")
        #     # Clear the input fields
        if not key or not value:
            # Display a warning message
            QMessageBox.warning(self, 'Warning', 'Both key and value must be filled.')
            return  # Don't add an empty key-value pair
        self.ui.key_value_list.addItem(f"{key}: {value}")
        self.ui.key_input.clear()
        self.ui.value_input.clear()
    def add_key_value_pair_subscriber(self):
        key = self.ui.sub_key_input.text()
        value = self.ui.sub_value_input.text()
        if not key or not value:
            # Display a warning message
            QMessageBox.warning(self, 'Warning', 'Both key and value must be filled.')
            return  # Don't add an empty key-value pair
        self.ui.sub_key_value_list.addItem(f"{key}: {value}")
        self.ui.sub_key_input.clear()
        self.ui.sub_value_input.clear()
    
    def save_values_publisher(self):   
        broker = self.ui.broker_input.text()
        port = self.ui.port_input.text()
        cleanSession = self.ui.cleanSession_input.text()
        retain = self.ui.retain_input.text()
        topicqos = self.ui.topicqos_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()        
        siteid = self.ui.siteid_input.text()
        direction = self.ui.direction_input.text()
        batchsize = self.ui.batchsize_input.text()
        initialdelay = self.ui.initialdelay_input.text()
        delay = self.ui.delay_input.text()
        initialRetryDelay = self.ui.initialRetryDelay_input.text()
        delayRetry = self.ui.delayRetry_input.text()
        dbhost = self.ui.dbhost_input.text()
        dbport = self.ui.dbport_input.text()
        dbname = self.ui.dbname_input.text()
        dbuser = self.ui.dbuser_input.text()
        dbpassword = self.ui.dbpassword_input.text()
        passkey = self.ui.passkey_input.text()
        HeartBeatAnalog = self.ui.HeartBeatAnalog_input.text()
        HeartBeatAnalogRetry = self.ui.HeartBeatAnalogRetry_input.text()
        HeartBeatDiscrete = self.ui.HeartBeatDiscrete_input.text()
        HeartBeatDiscreteRetry = self.ui.HeartBeatDiscreteRetry_input.text()
        HeartBeatListenerTimeDiff = self.ui.HeartBeatListenerTimeDiff_input.text()
        onDemandAnalogListenerTopic = self.ui.onDemandAnalogListenerTopic_input.text()
        onDemandAnalogPublishTopic = self.ui.onDemandAnalogPublishTopic_input.text()
        onDemandDiscreteListenerTopic = self.ui.onDemandDiscreteListenerTopic_input.text()
        onDemandDiscretePublishTopic = self.ui.onDemandDiscretePublishTopic_input.text()
        analogTopic = self.ui.analogTopic_input.text()
        discreteTopic = self.ui.discreteTopic_input.text()
        # Update the properties in the config object
        self.config.set('Broker', 'broker', broker)
        self.config.set('Broker', 'port', port)
        self.config.set('Broker', 'cleanSession', cleanSession)
        self.config.set('Broker', 'topicQos', topicqos)
        self.config.set('Broker', 'retain', retain)
        self.config.set('Broker', 'username', username)
        self.config.set('Broker', 'password', password)         
        self.config.set('Data', 'siteId', siteid)
        self.config.set('Data', 'direction', direction)
        self.config.set('Data', 'batchSize', batchsize)
        self.config.set('Data', 'initialDelay', initialdelay)
        self.config.set('Data', 'delay', delay)
        self.config.set('Data', 'initialRetryDelay', initialRetryDelay)
        self.config.set('Data', 'delayRetry', delayRetry)
        self.config.set('Data', 'heartBeatListenerTimeDifference', HeartBeatListenerTimeDiff)       
        self.config.set('Database', 'dbHost', dbhost)
        self.config.set('Database', 'dbPort', dbport)
        self.config.set('Database', 'dbName', dbname)
        self.config.set('Database', 'dbUser', dbuser)
        self.config.set('Database', 'dbPassword', dbpassword)
        self.config.set('Database', 'passKey', passkey)
        self.config.set('HeartBeatTopics', 'heartBeatAnalog', HeartBeatAnalog)
        self.config.set('HeartBeatTopics', 'heartBeatAnalogRetry', HeartBeatAnalogRetry)
        self.config.set('HeartBeatTopics', 'heartBeatDiscrete', HeartBeatDiscrete)
        self.config.set('HeartBeatTopics', 'heartBeatDiscreteRetry', HeartBeatDiscreteRetry)
        self.config.set('OnDemandTopics', 'onDemandAnalogListenerTopic', onDemandAnalogListenerTopic)
        self.config.set('OnDemandTopics', 'onDemandAnalogPublishTopic', onDemandAnalogPublishTopic)
        self.config.set('OnDemandTopics', 'onDemandDiscreteListenerTopic', onDemandDiscreteListenerTopic)
        self.config.set('OnDemandTopics', 'onDemandDiscretePublishTopic', onDemandDiscretePublishTopic)
        self.config.set('DataTopics', 'analogTopic', analogTopic)
        self.config.set('DataTopics', 'analogTopic', discreteTopic)      
        # Write the updated properties to the properties file
        with open('C:\\Users\\20339181\\OneDrive - L&T Construction\\Documents\\Pyqt5_GUI\\publisher_GUI\\config.properties', 'w') as configfile:
            self.config.write(configfile)
            for index in range(self.ui.key_value_list.count()):
                item = self.ui.key_value_list.item(index)
                key_value = item.text()
                configfile.write(key_value + '\n')
        # Provide feedback to the user
        self.ui.status_label.setText('Values saved successfully!')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.clear_status_message)
        self.timer.start(3000)
    def save_values_subscriber(self):   
        broker = self.ui.sub_broker_input.text()
        port = self.ui.sub_port_input.text()
        publishInterval= self.ui.sub_publishInterval_input.text()
        publishRetryInterval = self.ui.sub_publishRetryInterval_input.text()
        username = self.ui.sub_username_input.text()
        password = self.ui.sub_password_input.text()        
        direction = self.ui.sub_direction_input.text()
        initialdelay = self.ui.sub_initialdelay_input.text()
        delay = self.ui.sub_delay_input.text()
        dbDriver = self.ui.sub_dbDriver_input.text()
        dburl = self.ui.sub_dburl_input.text()
        dbHost = self.ui.sub_dbHost_input.text()
        dbPort = self.ui.sub_dbPort_input.text()
        dbName = self.ui.sub_dbName_input.text()
        dbUser = self.ui.sub_dbUser_input.text()
        dbPassword = self.ui.sub_dbPassword_input.text()
        passKey = self.ui.sub_passKey_input.text()
        HeartBeatAnalog = self.ui.sub_HeartBeatAnalog_input.text()
        HeartBeatAnalogRetry = self.ui.sub_HeartBeatAnalogRetry_input.text()
        HeartBeatDiscrete = self.ui.sub_HeartBeatDiscrete_input.text()
        HeartBeatDiscreteRetry = self.ui.sub_HeartBeatDiscreteRetry_input.text()
        onDemandAnalogListenerTopic = self.ui.sub_onDemandAnalogListenerTopic_input.text()
        onDemandDiscreteListenerTopic = self.ui.sub_onDemandDiscreteListenerTopic_input.text()
        analogTopic = self.ui.sub_analogTopic_input.text()
        discreteTopic = self.ui.sub_discreteTopic_input.text()
        analogClientId = self.ui.sub_analogClientId_input.text()
        discreteClientId = self.ui.sub_discreteClientId_input.text()
        heartBeatClient = self.ui.sub_heartBeatClient_input.text()
        onDemandAnalogClient = self.ui.sub_onDemandAnalogClient_input.text()
        onDemandDiscreteClient = self.ui.sub_onDemandDiscreteClient_input.text()
        # Update the properties in the config object
        self.config1.set('BrokerData', 'broker', broker)
        self.config1.set('BrokerData', 'port', port)
        self.config1.set('BrokerData', 'publishInterval', publishInterval)
        self.config1.set('BrokerData', 'publishRetryInterval', publishRetryInterval)
        self.config1.set('BrokerData', 'direction', direction)
        self.config1.set('BrokerData', 'username', username)
        self.config1.set('BrokerData', 'password', password)         
        self.config1.set('BrokerData', 'initialDelay', initialdelay)
        self.config1.set('BrokerData', 'delay', delay)
        self.config1.set('Database', 'dbDriver', dbDriver)
        self.config1.set('Database', 'dburl', dburl)
        self.config1.set('Database', 'dbHost', dbHost)
        self.config1.set('Database', 'dbPort', dbPort)
        self.config1.set('Database', 'dbName', dbName)
        self.config1.set('Database', 'dbUser', dbUser)
        self.config1.set('Database', 'dbPassword', dbPassword)
        self.config1.set('Database', 'passKey', passKey)
        self.config1.set('HeartBeatTopics', 'heartBeatAnalog', HeartBeatAnalog)
        self.config1.set('HeartBeatTopics', 'heartBeatAnalogRetry', HeartBeatAnalogRetry)
        self.config1.set('HeartBeatTopics', 'heartBeatDiscrete', HeartBeatDiscrete)
        self.config1.set('HeartBeatTopics', 'heartBeatDiscreteRetry', HeartBeatDiscreteRetry)
        self.config1.set('OnDemandTopics', 'onDemandAnalogListenerTopic', onDemandAnalogListenerTopic)
        self.config1.set('OnDemandTopics', 'onDemandDiscreteListenerTopic', onDemandDiscreteListenerTopic)
        self.config1.set('DataTopics', 'analogTopic', analogTopic)
        self.config1.set('DataTopics', 'analogTopic', discreteTopic)
        self.config1.set('ClientIds','analogClientId',analogClientId)     
        self.config1.set('ClientIds','discreteClientId',discreteClientId) 
        self.config1.set('ClientIds','heartBeatClient',heartBeatClient) 
        self.config1.set('ClientIds','onDemandAnalogClient',onDemandAnalogClient) 
        self.config1.set('ClientIds','onDemandDiscreteClient',onDemandDiscreteClient)  
        # Write the updated properties to the properties file
        with open('C:\\Users\\20339181\\OneDrive - L&T Construction\\Documents\\Pyqt5_GUI\\subscriber_GUI\\config.properties', 'w') as configfile:
            self.config1.write(configfile)
            for index in range(self.ui.sub_key_value_list.count()):
                item = self.ui.sub_key_value_list.item(index)
                key_value = item.text()
                configfile.write(key_value + '\n')
        # Provide feedback to the user
        self.ui.sub_status_label.setText('Values saved successfully!')
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.clear_status_message)
        self.timer.start(3000)
    
    def clear_status_message(self):
        self.ui.status_label.clear()
        self.ui.sub_status_label.clear()
    def delete_selected_item_publisher(self):
        selected_item = self.ui.key_value_list.currentItem()
        if selected_item is not None:
            row = self.ui.key_value_list.row(selected_item)
            self.ui.key_value_list.takeItem(row)
    def delete_selected_item_subscriber(self):
        selected_item = self.ui.sub_key_value_list.currentItem()
        if selected_item is not None:
            row = self.ui.sub_key_value_list.row(selected_item)
            self.ui.sub_key_value_list.takeItem(row)


    def edit_item(self, item):
        editor = QLineEdit(item.text())
        editor.setAlignment(Qt.AlignLeft)
        editor.editingFinished.connect(lambda: self.save_edit(item, editor))

        self.ui.key_value_list.setItemWidget(item, editor)
        self.ui.sub_key_value_list.setItemWidget(item, editor)  # Edit both lists

    def save_edit(self, item, editor):
        edited_text = editor.text()
        item.setText(edited_text)
        self.ui.key_value_list.setItemWidget(item, None)
        self.ui.sub_key_value_list.setItemWidget(item, None)

######################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
