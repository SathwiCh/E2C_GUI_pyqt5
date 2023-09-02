import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog, QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt

class FileTransferApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Transfer')
        self.setGeometry(100, 100, 400, 300)  # Adjusted window height for list widget

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.source_button = QPushButton('Select Source Folder')
        self.source_button.clicked.connect(self.select_source_folder)

        self.destination_button = QPushButton('Select Destination Folder')
        self.destination_button.clicked.connect(self.select_destination_folder)

        self.file_list_widget = QListWidget()

        self.transfer_button = QPushButton('Transfer Selected Files')
        self.transfer_button.clicked.connect(self.transfer_files)

        layout.addWidget(self.source_button)
        layout.addWidget(self.destination_button)
        layout.addWidget(self.file_list_widget)  # Adding the list widget to layout
        layout.addWidget(self.transfer_button)

        central_widget.setLayout(layout)

        self.source_folder = None
        self.destination_folder = None

    def select_source_folder(self):
        self.source_folder = QFileDialog.getExistingDirectory(self, 'Select Source Folder')
        self.update_file_list()
        print(f"Source Folder: {self.source_folder}")

    def select_destination_folder(self):
        self.destination_folder = QFileDialog.getExistingDirectory(self, 'Select Destination Folder')
        print(f"Destination Folder: {self.destination_folder}")

    def update_file_list(self):
        self.file_list_widget.clear()
        if self.source_folder:
            source_files = os.listdir(self.source_folder)
            for file_name in source_files:
                item = QListWidgetItem(file_name)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Unchecked)
                self.file_list_widget.addItem(item)

    def transfer_files(self):
        if self.source_folder and self.destination_folder:
            for row in range(self.file_list_widget.count()):
                item = self.file_list_widget.item(row)
                if item.checkState() == Qt.Checked:
                    file_name = item.text()
                    source_path = os.path.join(self.source_folder, file_name)
                    destination_path = os.path.join(self.destination_folder, file_name)
                    try:
                        if os.path.isfile(source_path):
                            shutil.copy2(source_path, destination_path)
                            print(f"Transferred: {file_name}")
                    except Exception as e:
                        print(f"Error transferring {file_name}: {e}")
            print("File transfer complete.")
        else:
            print("Please select source and destination folders first.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileTransferApp()
    window.show()
    sys.exit(app.exec_())
