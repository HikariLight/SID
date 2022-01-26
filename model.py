import wget
import requests
import os
from bs4 import BeautifulSoup


class Model():    

    def parse(self, link):
        img_links = []

        page = requests.get(link).text
        parsed_page = BeautifulSoup(page, 'html.parser')
        
        for image in parsed_page.find_all('img'):
            img_links.append(image.get("src"))

        return img_links

    def download(self, link, dir_name):
        try: 
            os.mkdir(dir_name) 
        except OSError as error: 
            print(error)

        img_links = self.parse(link)

        for i in range(len(img_links)):
            wget.download(img_links[i], "{}/{}.jpg".format(dir_name, i))
