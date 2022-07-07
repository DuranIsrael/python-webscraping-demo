# First we need to import our libraries needed  for this demo
from bs4 import BeautifulSoup 
import requests
import pandas as pd

#here we are requesting the webiste and storing it in a variable
url = "https://pogotrainer.club//"

results = requests.get(url)
results.raise_for_status() #this will print in error should there be an issue with the website
doc = BeautifulSoup(results.text, "html.parser") #taking the results of the url and puttiin it in text format
trainers = doc.find('article').find_all('div', class_="media") #specifiying the class that i want soup to find with the particular class name.

trainer_names=[]
trainer_codes=[]

for trainer in trainers:
    trainer_name = trainer.find('h4', class_="media-heading").text
    trainer_code = trainer.find('a', class_="TCLink").text
    print(trainer_name, trainer_code)

    trainer_names.append(trainer_name)
    trainer_codes.append(trainer_code)
    
    
mylist = pd.DataFrame({'Trainer Names:':trainer_names, 'Trainer Numbers:':trainer_codes})
mylist.to_csv("TrainerConnect.csv")















