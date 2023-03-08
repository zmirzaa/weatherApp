from flask_app import app 
from flask import render_template,render_template, request, redirect, session
import os
import requests 


BASE_URL = "https://api.openweathermap.org/data/2.5"



@app.route('/')
def dashboard(): 
    return render_template("index.html")




@app.route('/search', methods=['POST'])
def getWeather():
    zip_code = request.form['zip']
    r = requests.get(f"{BASE_URL}/weather?zip={zip_code}&units=imperial&appid={os.environ.get('FLASK_APP_API_KEY')}")
    
    session["temp"] = "{0:.2f}".format(r.json()['main']['temp']) 
    session["weather"]= r.json()["weather"][0]["main"]
    session["city"]= r.json()["name"]

    return redirect('/weather')

@app.route('/weather')
def weather(): 
    return render_template("weather.html")