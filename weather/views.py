import os
import requests
from django.shortcuts import render
# from .models import City
from .weather_forms import CityForm

API_KEY = os.environ.get('API_KEY')


def index(request):

    # cities = City.objects.all()

    weather_data = []
    if request.method == 'POST':
        city = request.POST.get('city')
    else:
        city = 'Saint Petersburg'

    weather_request = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    )
    print(weather_request.status_code)
    if weather_request.status_code == 200:
        response = weather_request.json()

        city_weather = {
            'city': str(city).title(),
            'temperature': int(response['main']['temp']),
            'feels_like': int(response['main']['feels_like']),
            'description': str(response['weather'][0]['description']).title(),
            'icon': response['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    form = CityForm()
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)
