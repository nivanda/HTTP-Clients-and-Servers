import imp
from flask import Flask, jsonify
import requests, json

app = Flask(__name__)

@app.route('/')
def WeatherForecast():
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    APICall = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.4369&lon=24.7535", headers=headers)


    WeatherList = json.loads(APICall.content)['properties']['timeseries']

    Count = 0
    Output = []
    for w in WeatherList:
        Count += 1
        datetimeList = w['time'].split('T')
        timeList = list(datetimeList[1])
        timeList.remove('Z')
        timeList = ''.join(timeList).split(':')
        timeList[0] = str(int(timeList[0]) + 2)
        datetime = datetimeList[0] + 'T' + ':'.join(timeList) + ':'
        data = w['data']['instant']['details']
        cloudData = None
        if data["cloud_area_fraction"] < 40:
            cloudData = "Clear sky"
        if data["cloud_area_fraction"] >= 40 and data["cloud_area_fraction"] < 60:
            cloudData = "Partially cloudy"
        if data["cloud_area_fraction"] >= 60:
            cloudData = "Cloudy"

        WeatherString = datetime + " | Air pressure -> {} hPa | Temperature -> {} *C | Sky -> {} | Humidity -> {} % | Wind direction -> {}* | Wind speed -> {} m/s".format(data["air_pressure_at_sea_level"], data["air_temperature"], cloudData, data["relative_humidity"], data["wind_from_direction"], data["wind_speed"])
        Output.append(WeatherString)
        
        if Count == 10:
            break
    
    return jsonify({'WeatherForecast': Output})


if __name__ == '__main__':
    app.debug = True
    app.run()