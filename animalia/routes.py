from flask import Flask, render_template, request, jsonify
import pandas as pd
from csv import writer
from animalia import app

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

@app.route("/submit", methods=["GET", "POST"])
def submit():                              #Request specific animal data
    if request.method == "POST":
        print("Arrived")
        data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv")
        with open("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\animalia\\database\\animal_locations.csv", 'a') as f_object:
            writer_object = writer(f_object)
            jsonData = request.get_json()
            print(jsonData)
            data_list = [len(data["key"]),jsonData["species"],jsonData["lat"],jsonData["long"],jsonData["type"],jsonData["description"]]
            writer_object.writerow(data_list)
            f_object.close()

        return "success"
    return render_template("Home.html")