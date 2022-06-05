import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopy

data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\database\\animal_locations.csv")
print(data.info())
#Cols: key,species,latitude,longitude,type,date,info
#Important Cols: species, latitude, longitude, type?
#Important Geospacial data (We use the coords to collect this): 
#   Average temperature, humidity, altitude, from each long lat coordinate

#Output: We input Long Lat coordinates + species, using the coords we find the geospacial data, then we see if location is habitable by requested species.



from sklearn import preprocessing

data.drop("info", axis = 1, inplace = True)
data.drop("key", axis = 1, inplace = True)
data.drop("date", axis = 1, inplace = True)
label_encoder = preprocessing.LabelEncoder()
data["species"] = label_encoder.fit_transform(data["species"])
data["type"] = label_encoder.fit_transform(data["type"])

data.insert(3,"ave_temp")  
data.insert(4,"ave_humid")
data.insert(5,"altitude")


for x in range(len(data["latitude"])): #This would make multiple api calls to get the geospacial info for each datapoint
    print("API Call")

#Realized this won't work due to the not being an UNSUITABLE data points. Changing idea to show data  (Min temp, av temp, max tem etc) and a few graphs



    