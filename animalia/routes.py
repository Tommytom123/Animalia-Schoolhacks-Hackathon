from typing import KeysView
from flask import Flask, render_template, request, jsonify
import pandas as pd
from csv import writer
from animalia import app
import random

@app.route("/")
def home():                              
    return render_template("Home.html")

@app.route("/fetch", methods=["GET", "POST"])
def fetch():                              #Request specific animal data
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv")
        key = jsonData["key"]
        return {
            'species' : data["species"][key],
            'type' : data["type"][key],
            'extra_info' : data["info"][key],
            'date' : data["date"][key],
            'long' : data["longitude"][key],
            'lat' : data["latitude"][key]
        }
    return render_template("Home.html")

@app.route("/all_data", methods=["GET", "POST"])
def all_data():                              #Request specific animal data
    if request.method == "POST":
        data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv")
        data.drop("info", axis = 1, inplace = True)
        data_json = data.to_json(None, indent = 1, orient = 'records')
        #print(data_json)
        return data_json
    return render_template("Home.html")      

@app.route("/submit", methods=["GET", "POST"])
def submit():                              #Request specific animal data
    if request.method == "POST":
        print("Arrived")
        data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv")
        with open("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv", 'a', newline="") as f_object:
            writer_object = writer(f_object)
            jsonData = request.get_json()
            print(jsonData)
            data_list = [len(data["key"]),jsonData["species"],jsonData["lat"],jsonData["long"],jsonData["type"],jsonData["date"],jsonData["description"]]
            writer_object.writerow(data_list)
            f_object.close()

        return "success"
    return render_template("Home.html")

@app.route("/search", methods=["GET", "POST"])
def search():                              #Search for all occurences of animal 
    if request.method == "POST":
        lat_list = []
        long_list = []
        species_list = []
        jsonData = request.get_json()
        csv_data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv")
        for x in range(len(csv_data["key"])):
            if jsonData["species_search"] in csv_data["species"][x]:
                lat_list.append(csv_data["latitude"][x])
                long_list.append(csv_data["longitude"][x])
                species_list.append(csv_data["species"][x])
        #keys_list.to_json(None, indent = 1, orient = 'records')
        if len(lat_list) > 21: #If the list is too large, get random values
            combined = list(zip(lat_list, long_list, species_list))
            random.shuffle(combined)
            lat_list, long_list, species_list = zip(*combined)
        return {
            'species' : species_list,
            'lats' : lat_list,
            'longs' : long_list
        }
    return render_template("Home.html")

