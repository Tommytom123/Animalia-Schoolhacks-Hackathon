from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "0966db99-36b6-41c0-b0bd-be21894ceb60"

from animalia import routes