from posixpath import dirname
import wget
import requests
import os
from bs4 import BeautifulSoup


class Model():    

    def get_img_links(self, link):
        img_links = []

        page = requests.get(link).text
        parsed_page = BeautifulSoup(page, 'html.parser')
        
        for image in parsed_page.find_all('img'):
            img_links.append(image.get("src"))

        return img_links
    
    def get_pics_number(self, link):
        return len(self.get_img_links(link))

    def make_dir(self, dir_name):
        try: 
            os.mkdir(dir_name) 
        except OSError as error: 
            print(error)

    def download_img(self, link, name):
        try:
            wget.download(link, name)
        except OSError as e:
            print(e)

    def download_all(self, link, dir_name):

        try:
            self.make_dir(dirname)
        except:
            print("Already exists")

        img_links = self.get_img_links(link)

        for i in range(len(img_links)):
            self.download_img(img_links[i], "{}/{}.jpg".format(dir_name, i))