import requests, json

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
APICall = requests.get("https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.4369&lon=24.7535", headers=headers)

WeatherList = json.loads(APICall.content)['properties']['timeseries']

Count = 0
for w in WeatherList:
    Count += 1
    datetimeList = w['time'].split('T')
    timeList = list(datetimeList[1])
    timeList.remove('Z')
    timeList = ''.join(timeList).split(':')
    timeList[0] = str(int(timeList[0]) + 2)
    datetime = datetimeList[0] + 'T' + ':'.join(timeList) + ':'
    data = w['data']['instant']['details']

    print(datetime)
    print("Air pressure -> {} hPa".format(data["air_pressure_at_sea_level"]))
    print("Air temperature -> {} C*".format(data["air_temperature"]))
    print("Cloud area fraction -> {} %".format(data["cloud_area_fraction"]))
    try:  
        print("Precipitation amount -> {} mm".format(data["precipitation_amount"]))
    except:
        pass
    print("Relative humidity -> {} %".format(data["relative_humidity"]))
    print("Wind from direction -> {} degrees".format(data["wind_from_direction"]))
    print("Wind speed -> {} m/s".format(data["wind_speed"]))
    
    if Count == 10:
        break
