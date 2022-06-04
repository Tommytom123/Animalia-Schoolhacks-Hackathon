import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\database\\animal_locations.csv")
print(data.info())

from sklearn import preprocessing

data.drop("info", axis = 1, inplace = True)
data.drop("key", axis = 1, inplace = True)
label_encoder = preprocessing.LabelEncoder()
data["species"] = label_encoder.fit_transform(data["species"])
data["type"] = label_encoder.fit_transform(data["type"])

print(data.info())

x = data[["species", "type"]]
y = data[["latitude", "longitude"]]
data.drop("latitude", axis = 1, inplace = True)
data.drop("longitude", axis = 1, inplace = True)
