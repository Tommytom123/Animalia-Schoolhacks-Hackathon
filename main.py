from flask import Flask, render_template, request
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
        key = data["key"]
        print("KEYS", key)
        animal = data["animal"][key-1]
        print("ANIMAL", animal)
        return {
            'response' : animal
        }
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)
