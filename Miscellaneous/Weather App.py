import requests
import json
from datetime import date
import urllib.parse


accuweatherAPIKey = "0gBRfz2py0kc5Ouvkt7uJT4F5eAJHyqK"
mapboxAccessToken = "pk.eyJ1IjoibmZzaWx2ZWlyYSIsImEiOiJjbDRtemZoZDcxNGhvM2dwYjBjbmI4czB5In0.IhnWZqJ7DPwTHlFVO4w6Hg"
days_in_week = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']


def fetchCoordinates():

    r = requests.get("http://www.geoplugin.net/json.gp")

    if (r.status_code != 200):

        print("Não foi possível obter a localização.")
        return None

    else:

        try:

            localization = json.loads(r.text)
            coords = {}
            coords["lat"] = localization["geoplugin_latitude"]
            coords["long"] = localization["geoplugin_longitude"]
            
            return coords

        except:

            return None


def fetchLocalCode(lat,long):

    locationAPIUrl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
    + "search?apikey=" + accuweatherAPIKey \
    + "&q=" + lat + "%2C" + long + "&language=pt-br"

    r = requests.get(locationAPIUrl)

    if (r.status_code != 200):

        print("Não foi possível obter o código do local.")
        return None

    else:

        try:

            locationResponse = json.loads(r.text)
            locationInfo = {}
            locationInfo["locationName"] = locationResponse['LocalizedName'] + ", " \
                        + locationResponse['AdministrativeArea']['LocalizedName'] + ". "\
                        + locationResponse['Country']['LocalizedName']
            locationInfo["locationCode"] = locationResponse['Key']
            
            return locationInfo

        except:

            return None
        

def fetchCurrentWeather(locationCode, locationName):

    CurrentConditionsAPIUrl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                              + locationCode + "?apikey=" + accuweatherAPIKey \
                              + "&language=pt-br"

    r = requests.get(CurrentConditionsAPIUrl)

    if (r.status_code != 200):
        print("Não foi possível obter o clima atual.")
        return None

    else:

        try:

            CurrentConditionsResponse = json.loads(r.text)
            weatherInfo = {}
            weatherInfo["weatherText"] = CurrentConditionsResponse[0]['WeatherText']
            weatherInfo["temperature"] = CurrentConditionsResponse[0]['Temperature']['Metric']['Value']
            weatherInfo["locationName"] = locationName

            return weatherInfo

        except:

            return None


def fetchFiveDayForecast(locationCode):

    DailyAPIUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
                              + locationCode + "?apikey=" + accuweatherAPIKey \
                              + "&language=pt-br&metric=true"

    r = requests.get(DailyAPIUrl)

    if (r.status_code != 200):
        print("Não foi possível obter o clima atual.")
        return None

    else:

        try:

            DailyResponse = json.loads(r.text)
            FiveDayWeatherInfo = []

            for day in DailyResponse['DailyForecasts']:

                dailyWeather = {}
                dailyWeather['max'] = day['Temperature']['Maximum']['Value']
                dailyWeather['min'] = day['Temperature']['Minimum']['Value']
                dailyWeather['weather'] = day['Day']['IconPhrase']
                weekDay = int(date.fromtimestamp(day['EpochDate']).strftime("%w"))
                dailyWeather['day'] = days_in_week[weekDay]
                FiveDayWeatherInfo.append(dailyWeather)
            
            return FiveDayWeatherInfo

        except:

            return None


def showForecast(lat, long):

    try:

        location = fetchLocalCode(lat,long)
        currentWeather = fetchCurrentWeather(location['locationCode'], location['locationName'])
        print("Clima atual em: " + currentWeather['locationName'])
        print(currentWeather['weatherText'])
        print("Temperatura: " + str(currentWeather['temperature']) + "\xb0" + "C")

    except:

        print("Erro ao obter o clima atual.")
        
    
    option = input("\nDeseja ver a previsão para os próximos dias?(s ou n): ").lower()

    if option == "s":

        print("\nClima para hoje e para os próximos dias:\n")
        
        try:

            FiveDayForecast = fetchFiveDayForecast(location['locationCode'])
            for day in FiveDayForecast:
                print(day['day'])
                print("Mínima: " + str(day['min']) + "\xb0" + "C")
                print("Máxima: " + str(day['max']) + "\xb0" + "C")
                print("Clima: " + day['weather'])
                print("-------------------------")

        except:

            print("Erro ao obter a previsão para os próximos dias.")


def searchLocation(location):

    _location = urllib.parse.quote(location)
    mapboxGeocodingUrl = "https://api.mapbox.com/geocoding/v5/mapbox.places/" \
        + _location + ".json?access_token=" + mapboxAccessToken

    r = requests.get(mapboxGeocodingUrl)

    if (r.status_code != 200):

        print("Não foi possível obter o clima atual.")
        return None

    else:

        try:

            MapboxResponse = json.loads(r.text)
            coordinates = {}
            coordinates['lat'] = str(MapboxResponse['features'][0]['geometry']['coordinates'][1])
            coordinates['long'] = str(MapboxResponse['features'][0]['geometry']['coordinates'][0])
            return coordinates

        except:

            print("Erro na pesquisa de local.")


#Program starts here

try:

    coordinates = fetchCoordinates()
    showForecast(coordinates['lat'], coordinates['long'])

    keepgoing = "s"

    while keepgoing == "s":

        keepgoing = input("\nDeseja consultar a previsão de outro local?(s ou n): ").lower()

        if keepgoing != "s":

            break
        location = input("Digite a cidade e o estado: ")

        try:

            coordinates = searchLocation(location)
            showForecast(coordinates['lat'], coordinates['long'])

        except:

            print("Não foi possível obter a previsão para este local.")

except:
    
    print("Erro ao processar a solicitação. Entre em contato com o suporte.")