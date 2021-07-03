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

    def download(self, img_links):

        try: 
            os.mkdir("./Downloads") 
        except OSError as error: 
            print(error)

        for i in range(len(img_links)):
            wget.download(img_links[i], "Downloads/{}.jpg".format(i))


# m = Model()
# m.download(m.parse("https://unsplash.com/s/photos/cute-cat"))
# m.download(m.parse("http://all-free-download.com/wallpapers/nature-wallpaper.html"))
