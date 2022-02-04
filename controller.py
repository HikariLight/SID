from PyQt6.QtWidgets import QApplication
from view import View
from model import Model
import sys

class Controller:
    def __init__(self):
        self.model = Model()
    
    def initUI(self):
        app = QApplication(sys.argv)
        self.view = View(self)
        self.view.show()
        app.exec()
    
    def getPicsNumber(self, link):
        return self.model.get_pics_number(link)

    def download_all(self, link, dir_name):
        self.model.download_all(link, dir_name)