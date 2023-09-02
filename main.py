import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QFileDialog

class FileTransferApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Transfer')
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.source_button = QPushButton('Select Source Folder')
        self.source_button.clicked.connect(self.select_source_folder)

        self.destination_button = QPushButton('Select Destination Folder')
        self.destination_button.clicked.connect(self.select_destination_folder)

        self.transfer_button = QPushButton('Transfer Files')
        self.transfer_button.clicked.connect(self.transfer_files)

        layout.addWidget(self.source_button)
        layout.addWidget(self.destination_button)
        layout.addWidget(self.transfer_button)

        central_widget.setLayout(layout)

    def select_source_folder(self):
        self.source_folder = QFileDialog.getExistingDirectory(self, 'Select Source Folder')
        print(f"Source Folder: {self.source_folder}")

    def select_destination_folder(self):
        self.destination_folder = QFileDialog.getExistingDirectory(self, 'Select Destination Folder')
        print(f"Destination Folder: {self.destination_folder}")

    def transfer_files(self):
        if hasattr(self, 'source_folder') and hasattr(self, 'destination_folder'):
            source_files = os.listdir(self.source_folder)
            for file_name in source_files:
                source_path = os.path.join(self.source_folder, file_name)
                destination_path = os.path.join(self.destination_folder, file_name)
                try:
                    if os.path.isfile(source_path):
                        shutil.copy2(source_path, destination_path)  # Change to shutil.move if you want to move instead of copy
                except Exception as e:
                    print(f"Error transferring {file_name}: {e}")
            print("Files transferred!")
        else:
            print("Please select source and destination folders first.")
        print("Files transferred!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileTransferApp()
    window.show()
    sys.exit(app.exec_())
