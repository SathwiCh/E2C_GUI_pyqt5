import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
import configparser
from E2C_GUI import Ui_MainWindow

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.key_input.setHidden(True)
        self.ui.value_input.setHidden(True)

        # Connect the "Save" button to the save function
        self.ui.save_button.clicked.connect(self.save_values)
        self.ui.add_button.clicked.connect(self.add_key_value_pair)
        self.ui.newproperty_button.clicked.connect(self.show_input_fields)
        self.ui.delete_button.clicked.connect(self.delete_selected_item)

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
                
    def show_input_fields(self):
        # Show the input fields when the button is clicked
        self.ui.key_input.setHidden(False)
        self.ui.value_input.setHidden(False)

    def add_key_value_pair(self):
        key = self.ui.key_input.text()
        value = self.ui.value_input.text()
        if key and value:
            self.ui.key_value_list.addItem(f"{key}: {value}")
            # Clear the input fields
            self.ui.key_input.clear()
            self.ui.value_input.clear()

    def save_values(self):   
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
        # publishinterval = self.ui.publishinterval_input.text()
        # publishretryinterval = self.ui.publishretryinterval_input.text()
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
        # self.config.set('Data', 'publishinterval', publishinterval)
        # self.config.set('Data', 'publishretryinterval', publishretryinterval)
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

    def clear_status_message(self):
        self.ui.status_label.clear()
    def delete_selected_item(self):
        selected_item = self.ui.key_value_list.currentItem()
        if selected_item is not None:
            row = self.ui.key_value_list.row(selected_item)
            self.ui.key_value_list.takeItem(row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
