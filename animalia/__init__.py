from flask import Flask

app = Flask(__name__)

from animalia import forms
from animalia import routes