from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():                                     #Main Page
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)
