import requests
from django.shortcuts import render
from .models import City


def index(request):
    url = ' http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=45fb2035cf13c4adfd3f6a6dc978fad3'
    city = 'Dhaka'

    if request.method == 'POST':
        city = request.POST.get('data')

    r = requests.get(url.format(city)).json()
    
    if r['cod'] == '404':
        context = {
            'city': request.POST.get('data')
        }
        return render(request, 'weather_app/error.html', context)
    

    city_weather = {
        'city' : city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'] 
    }


    context = {
        'city': city_weather
    }
    
    return render(request, 'weather_app/weather.html', context)