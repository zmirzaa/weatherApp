from datetime import datetime
from flask_app import app 
from flask import render_template,render_template, request, redirect, session
import os
import requests 


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"



@app.route('/')
def dashboard(): 
    return render_template("index.html")




@app.route('/search', methods=['POST'])
def getWeather():
    city_name = request.form['city']
    state_code = request.form['state']
    r = requests.get(f"{BASE_URL}q={city_name},{state_code},&units=imperial&appid={os.environ.get('FLASK_APP_API_KEY')}").json()
    if r['cod'] == '404': 
        print("Sorry, city not found.")
    else:
        session["temp"] = "{0:.2f}".format(r['main']['temp']) 
        session["weather"]= r["weather"][0]["description"]
        session["city"]= r["name"]
        session['icon'] = r['weather'][0]['icon']
        session['dateTime'] = datetime.now().strftime("%b %d %Y | %I:%M %p")
    return redirect('/weather')

@app.route('/weather')
def weather(): 
    return render_template("weather.html")