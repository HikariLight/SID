from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QProgressBar
import sys

class View(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.initUI()

        self.controller = controller

    def initUI(self):

        self.setWindowTitle("Simple Images Downloader")

        self.link_title = QLabel('Enter link here')
        self.link_title.move(173, 362)

        # self.link_input = QLineEdit(self)
        # self.link_input.move(372, 344)

        # self.dir_title = QLabel('Pick save directory')
        # self.dir_title.move(173, 465)
        
        # self.dir_input = QLineEdit(self)
        # self.dir_input.move(372, 465)

        self.btn = QPushButton('Download', self)
        self.btn.move(440, 627)
        self.btn.clicked.connect(self.download)

        self.setGeometry(300, 300, 1149, 888)
        self.setWindowTitle('Simple Image Downloader')
        self.show()

    def download(self):
        self.controller.download()
    
app = QApplication(sys.argv)

window = View()
window.show()

app.exec()