from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)



@app.route('/', methods = ['GET', 'POST'])
def index():
    #runs when form is submitted
    if request.method == "POST":
        #Received data from HTML form
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        api_key = "9e5557f9a8df83fbb035ba18ffbec788"
        
        #Used for having separate layout from US and Other Countries and request metric/imperial units accordingly
        if state == '':
            weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric')
            unit= 'C'
        else:
            weather_url = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={api_key}&units=imperial')
            unit = 'F'

        weather_data = weather_url.json()

        #Could pass as an object to render_template(), left here for visibility
        temp = round(weather_data['main']['temp'])
        icon = weather_data['weather'][0]['icon']
        icon = 'http://openweathermap.org/img/w/' + icon + '.png'
        description = weather_data['weather'][0]['description']
        feels_like = round(weather_data['main']['feels_like'])

        if state == '':
            return render_template('result.html', unit=unit, temp=temp, feels_like=feels_like, description=description, icon=icon, city=city, country=country)
        else:
            return render_template('result_us.html', unit=unit, temp=temp, feels_like=feels_like, description=description, icon=icon, city=city, state=state, country=country)
    #Initial return when page is launched with no form submission
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
