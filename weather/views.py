from django.shortcuts import render, redirect
import requests
from .models import City
from .forms import FormCity
from django import forms


def index(request):
    api_key = '08ae63f38a38e5e1d0cbe0d927d5ceff'
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'

    if request.method == 'POST':
        form = FormCity(request.POST) 
        if form.is_valid():
            form.save()

    if request.method == 'POST':
        if 'action' in request.POST:
            city_name = request.POST['action']
            try:
                city_to_delete = City.objects.get(name=city_name)
                city_to_delete.delete()
            except City.DoesNotExist:
                pass  

        return redirect('home')

    form = FormCity()

    cities = City.objects.all()
    weather_data = []
    for city in cities:
        city_weather = requests.get(base_url.format(city.name, api_key)).json()

        weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon':city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)
    context = {'weather_data': weather_data, 'form': form}
    
    return render(request,'index.html', context)

