# First we need to import our libraries needed  for this demo
from turtle import title
from bs4 import BeautifulSoup 
import requests
import pandas as pd

#here we are requesting the webiste and storing it in a variable
url = "https://pogotrainer.club//"

results = requests.get(url)
doc = BeautifulSoup(results.content, "html.parser")
article = doc.find('div',attrs={'class': "col-md-8"})


trainer_names = []
trainer_num = []

for items in article.find_all('div',attrs={'class':"trainerContainer"}):
    trainer_names = items.find('h4',attrs={'class':"media-heading"}).text
    trainer_num = items.find('a',attrs={'class':"TClink"}).text

trainer_names.append(trainer_names)
trainer_num.append(trainer_num)

mylist = pd.DataFrame({'Trainer Names:':trainer_names, 'Trainer Numbers:':trainer_num})
mylist.to_csv("TrainerConnect.csv")















