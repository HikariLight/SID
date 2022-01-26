from model import Model

class Controller:
    def __init__(self):
        self.model = Model()

    def download(self, link, dir_name):
        self.model.download(link, dir_name)