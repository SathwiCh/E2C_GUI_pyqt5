import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
import configparser
from Config_GUI import Ui_Dialog
class MyApp(QDialog):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.key_input.setHidden(True)
        self.ui.value_input.setHidden(True)

        # Connect the "Save" button to the save function
        self.ui.save_button.clicked.connect(self.save_values)
        self.ui.add_button.clicked.connect(self.add_key_value_pair)
        self.ui.add_input_fields.clicked.connect(self.show_input_fields)
        self.ui.delete_button.clicked.connect(self.delete_selected_item)

        # Load the properties file
        self.config = configparser.ConfigParser()
        self.config.read('config.properties')

        # Set initial values in the UI from the properties file
        self.ui.broker_input.setText(self.config.get('Broker', 'broker'))
        self.ui.port_input.setText(self.config.get('Broker', 'port'))
        self.ui.username_input.setText(self.config.get('Broker', 'username'))
        self.ui.password_input.setText(self.config.get('Broker', 'password'))
        self.ui.siteid_input.setText(self.config.get('Broker', 'siteid'))
        self.ui.retain_input.setText(self.config.get('Broker', 'retain'))
        self.ui.topicqos_input.setText(self.config.get('Broker', 'topicqos'))
        self.ui.direction_input.setText(self.config.get('Broker', 'direction'))
        self.ui.batchsize_input.setText(self.config.get('Broker', 'batchsize'))
        self.ui.publishinterval_input.setText(self.config.get('Broker', 'publishinterval'))
        self.ui.publishretryinterval_input.setText(self.config.get('Broker', 'publishretryinterval'))
        self.ui.initialdelay_input.setText(self.config.get('Broker', 'initialdelay'))
        self.ui.delay_input.setText(self.config.get('Broker', 'delay'))
        self.ui.dbhost_input.setText(self.config.get('Database', 'dbhost'))
        self.ui.dbport_input.setText(self.config.get('Database', 'dbport'))
        self.ui.dbname_input.setText(self.config.get('Database', 'dbname'))
        self.ui.dbuser_input.setText(self.config.get('Database', 'dbuser'))
        self.ui.dbpassword_input.setText(self.config.get('Database', 'dbpassword'))
        self.ui.passkey_input.setText(self.config.get('Database', 'passkey'))
         
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
        # Get values from the UI
        broker = self.ui.broker_input.text()
        port = self.ui.port_input.text()
        username = self.ui.username_input.text()
        password = self.ui.password_input.text()
        siteid = self.ui.siteid_input.text()
        retain = self.ui.retain_input.text()
        topicqos = self.ui.topicqos_input.text()
        direction = self.ui.direction_input.text()
        batchsize = self.ui.batchsize_input.text()
        publishinterval = self.ui.publishinterval_input.text()
        publishretryinterval = self.ui.publishretryinterval_input.text()
        initialdelay = self.ui.initialdelay_input.text()
        delay = self.ui.delay_input.text()
        dbhost = self.ui.dbhost_input.text()
        dbport = self.ui.dbport_input.text()
        dbname = self.ui.dbname_input.text()
        dbuser = self.ui.dbuser_input.text()
        dbpassword = self.ui.dbpassword_input.text()
        passkey = self.ui.passkey_input.text()

        # Update the properties in the config object
        self.config.set('Broker', 'broker', broker)
        self.config.set('Broker', 'port', port)
        self.config.set('Broker', 'username', username)
        self.config.set('Broker', 'password', password)
        self.config.set('Broker', 'siteid', siteid)
        self.config.set('Broker', 'retain', retain)
        self.config.set('Broker', 'topicqos', topicqos)
        self.config.set('Broker', 'direction', direction)
        self.config.set('Broker', 'batchsize', batchsize)
        self.config.set('Broker', 'publishinterval', publishinterval)
        self.config.set('Broker', 'publishretryinterval', publishretryinterval)
        self.config.set('Broker', 'initialdelay', initialdelay)
        self.config.set('Broker', 'delay', delay)
        self.config.set('Database', 'dbhost', dbhost)
        self.config.set('Database', 'dbport', dbport)
        self.config.set('Database', 'dbname', dbname)
        self.config.set('Database', 'dbuser', dbuser)
        self.config.set('Database', 'dbpassword', dbpassword)
        self.config.set('Database', 'passkey', passkey)

        # Write the updated properties to the properties file
        with open('config.properties', 'w') as configfile:
            self.config.write(configfile)
            for index in range(self.ui.key_value_list.count()):
                item = self.ui.key_value_list.item(index)
                key_value = item.text()
                configfile.write(key_value + '\n')

        # Provide feedback to the user
        self.ui.status_label.setText('Values saved successfully!')

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
