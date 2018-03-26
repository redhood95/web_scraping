#importing required libraries
import urllib.request as jk
from bs4  import BeautifulSoup
from os.path  import basename
import requests
import os

#setting the page from where you want to download images
websiteCode = jk.urlopen("http://www.imfdb.org/wiki/Category:Assault_Rifle").read()
soup = BeautifulSoup(websiteCode,"lxml")

images = []
images = soup.findAll('img')

link = []

# generating list of url of he images
for image in images:
    link.append(image.get('src'))

str1 = 'http://www.imfdb.org'
link_final = []  
for l in link:
    link_final.append(str1+l)

#downloading the images 

for link in link_final:
        with open(basename(link), "wb") as f:
            f.write(requests.get(link).content)


