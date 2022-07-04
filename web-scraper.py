# First we need to import our libraries needed  for this demo
from turtle import title
from bs4 import BeautifulSoup 
import requests
import pandas as pd

#here we are requesting the webiste and storing it in a variable
url = "https://pogotrainer.club//"

results = requests.get(url)

doc = BeautifulSoup(results.content, "html.parser")
article = BeautifulSoup.find('div',attrs={'class': "col-md-8"})


trainer_names = []
trainer_num = []

for items in article.findAll('div',attrs={'class': "trainerContainer"}):
    trainer_names = items.find('h4',attrs={'class': "media-heading"}).text
    trainer_num = items.find('a',attrs={'title': "Copy Trainer Code"}).text

    trainer_names.append(trainer_names)
    trainer_num.appende(trainer_num)

mylist=pd.DataFrame({'Trainer Name:':trainer_names, 'Trainer Numbers:':trainer_num})
mylist.to.csv("TrainerConnect.csv")















