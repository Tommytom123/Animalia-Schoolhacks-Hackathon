from flask import Flask, render_template, request, jsonify
import pandas as pd


app = Flask(__name__)

@app.route("/")
def home():                              #Main Page
    return render_template("Home.html")

@app.route("/fetch", methods=["GET", "POST"])
def fetch():                              #Request specific animal data
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\database\\animal_locations.csv")
        key = jsonData["key"]
        return {
            'species' : data["animal"][key],
            'type' : data["type"][key],
            'extra_info' : data["info"][key]
        }
    return render_template("Home.html")

@app.route("/all_data", methods=["GET", "POST"])
def all_data():                              #Request specific animal data
    if request.method == "POST":
        data = pd.read_csv("C:\\Users\\Tom Brouwers\\Documents\\Python\\Animalia\\Animalia-Schoolhacks-Hackathon\\database\\animal_locations.csv")
        data.drop("info", axis = 1, inplace = True)
        data_json = data.to_json(None, indent = 1, orient = 'records')
        print(data_json)
        return data_json
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)
