from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    data = {}
    if request.method == "POST":
        city_name = request.POST["search-city"]
        json_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name.lower()}&appid=5bbc1acec51d4e6e1a1a397973e0a2a0").json()
        if json_data["cod"] != "404":
            data = {
                "city_name" : city_name.title(),
                "country_code" : str(json_data["sys"]["country"]),
                "coordinates" : str(json_data["coord"]["lon"]) + " " + str(json_data["coord"]["lat"]),
                "temp" : str(round(json_data["main"]["temp"] - 273.15, 2)) + "'C",
                "pressure" : str(json_data["main"]["pressure"]),
                "humidity" : str(json_data["main"]["humidity"])
            }
        else:
            data = {
                "city_name" : "City Not Found"
            }
    else:
        city_name = ""
    return render(request, "index.html", data)
