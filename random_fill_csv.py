import pandas
from csv import writer
import random

#This file fills the CSV so we have something to show
animal_list = ["Fire Ant", "Wolf", "Fallow Deer", "Roe Deer", "Stoat", "Fire Salamander", "Ortolan Bunting", "European Viper", "Rabbit", "Hare", "Badger", "Woodpecker"]
plant_list = ["Daisy", "Yellow Water-Lily", "Japanese Knotweed", "Myriophyllum Verticillatum", "Gentiana Pneumonanthe"]

for x in range(500): #animals
    with open("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv", 'a', newline="") as f_object:
        writer_object = writer(f_object)
        data_list = [x, random.choice(animal_list), round(random.uniform(47.009, 52.0000000),5), round(random.uniform(4.00000, 18.2452345),5), "Animal","06/05/2022", "Placeholder Info"] # key,species,latitude,longitude,type,date,info
        writer_object.writerow(data_list)
        f_object.close()
for x in range(500,1000): #plants
    with open("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv", 'a', newline="") as f_object:
        writer_object = writer(f_object)
        data_list = [x, random.choice(plant_list), round(random.uniform(47.009, 52.0000000),5), round(random.uniform(4.000000, 28.00024),5), "Plant","06/05/2022", "Placeholder Info"] # key,species,latitude,longitude,type,date,info
        writer_object.writerow(data_list)
        f_object.close()        