from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def view():
    if request.method=="POST":
        city=request.form['city']
        country= request.form['country']
        degree=request.form['degree']


        api_key= 'd7f87c0f3113a79b1d53bcde799a17e0'

        weather_url= requests.get(f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')
        weather_data=weather_url.json() 
        # print(weather_data)
        Current_temperature= int(weather_data['main']['temp'])
        wind_speed=weather_data['wind']['speed']
        Humidity_level=weather_data['main']['humidity']
        return render_template("show.html", Current_temperature=Current_temperature,humidity=Humidity_level, wind_speed=wind_speed,degree=degree,city=city)
    return render_template("view.html")    

app.run(debug=True)