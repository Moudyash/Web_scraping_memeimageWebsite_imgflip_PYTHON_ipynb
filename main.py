import requests
import shutil
import time
from bs4 import BeautifulSoup
import json
import os
import csv
from pathlib import Path


filecsv = open('meme.csv', 'w', encoding='utf8')

# Set the URL you want to webscrape from
url = 'https://imgflip.com/?page='
try:
    os.mkdir("images")
except FileExistsError:
    shutil.rmtree("/content/images")
    os.makedirs("images")
file = open('meme.json', 'w', encoding='utf8')
file.write('[\n')
data = {}
csv_columns = ['author', 'title', 'img']
writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
writer.writeheader()

for page in range(1, 11):
    print('---', page, '---')
    r = requests.get(url + str(page))
    print(url + str(page))
    soup = BeautifulSoup(r.content, "html.parser")
    ancher = soup.find_all('div', {'class': "base-unit clearfix"})
    i = 0
    for pt in ancher:
        try:
            img = pt.find('img', {'class': 'base-img'})['src']
        except TypeError:
            try:
                img = pt.find('video', {'class': 'base-img ctx-gif'})['data-src']
            except TypeError:
                img = "img not availabe"
        try:
            title = pt.find('h2', {'class': 'base-unit-title'}).find('a').get_text()
        except AttributeError:
            title = 'not availabe'
        try:
            author = pt.find('a', {'class': 'u-username'}).get_text()
        except AttributeError:
            author = 'not availabe'

        if img != "img not availabe":
            resource = requests.get("http:" + img)
            # print("status_code",resource.status_code)
            if (img.endswith(".jpg")):
                output = open("images/" + title.replace('/', "") + str(page) + author + ".jpg", "wb")
            else:
                output = open("images/" + title.replace('/', "") + str(page) + author + ".gif", "wb")
            output.write(resource.content)

            output.close()
        else:
            print("img not availabe")
        print("image: " + "https:" + img)
        print("title: ", title)
        print("author: ", author)

        writer.writerow({'author': author.strip('\r\n'), "title": title, "img": img})

        data['img'] = img
        data['title'] = title
        data['author'] = author
        json_data = json.dumps(data, ensure_ascii=False)
        file.write(json_data)
        file.write(",\n")
file.write("\n]")
# defining the api-endpoint
filecsv.close()
file.close()

print(len(os.listdir('/content/images')), "images are extracted")
