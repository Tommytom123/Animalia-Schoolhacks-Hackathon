from flask import Flask, render_template, request, jsonify
import pandas as pd
import csv
from animalia import app

@app.route("/", methods=["GET", "POST"])
def home():                              
    if request.method == "POST":
        # key,species,latitude,longitude,type,info
        print("i got here wooohoo")
        print(request.form["species"])
        csv.writer(open("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv", "a+")).writerow(
            [
                3,
                request.form["species"],
                request.form["lat"],
                request.form["long"],
                request.form["animal"],
                request.form["description"]
            ]
        )
        return render_template("Home.html")
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
            'extra_info' : data["info"][key]
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
