from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QProgressBar, QLineEdit
from PyQt6.QtGui import QFont

class View(QMainWindow):

    def __init__(self, controller):
        super().__init__()
        self.initUI()
        self.controller = controller

    def initUI(self):

        self.setWindowTitle("SID")

        self.setStyleSheet(open("style.css").read())

        self.title = QLabel(self)
        self.title.setText("Simple Image Downloader")
        self.title.setFont(QFont("Helvetica", 24))
        self.title.adjustSize()
        self.title.move(345, 146)

        self.link_title = QLabel(self)
        self.link_title.setText("Link")
        self.link_title.move(250, 270)

        self.link_input = QLineEdit(self)
        self.link_input.setGeometry(380, 270, 300, 30)

        self.dir_title = QLabel(self)
        self.dir_title.setText("Destination")
        self.dir_title.move(250, 400)
        
        self.dir_input = QLineEdit(self)
        self.dir_input.setGeometry(380, 400, 300, 30)

        self.btn = QPushButton('Download', self)
        self.btn.move(420, 550)
        self.btn.resize(150, 50)
        self.btn.clicked.connect(self.download)

        self.setGeometry(300, 300, 960, 720)
        self.setWindowTitle('SID')

        self.show()

    def download(self):
        try:
            self.controller.download(self.link_input.text(), self.dir_input.text())
        except Exception as e:
            print(e)
