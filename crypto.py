import urllib.request

from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
import os
from flask.globals import current_app
from flask.helpers import send_from_directory
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

#Initializing flask app
app=Flask(__name__)

app.config["SECRET_KEY"] = 'k9239'




#crypto
url = "https://api.lunarcrush.com/v2?data=assets&key={API_KEY_HERE}&symbol=BTC"
x=urllib.request.urlopen(url).read()
print(x)