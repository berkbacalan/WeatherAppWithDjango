import json

from django.http import HttpResponse
from django.shortcuts import render
import requests
from .forms import CityForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=d86bb93c9e284ec4a23211421212104&q={}&fx=yes&cc=no&mca=no&format=json&num_of_days=5'

    city=request.POST.get('City','Ankara')
    re = requests.get(url.format(city)).text
    #d = re.content.decode('utf-8')
    r = json.loads(re)
    #print(r.text)

    print(r)

    city_weather_1 = {
        'city' : city,
        'temperature' : r['data']['weather'][0]['avgtempC'],
        'description' : r['data']['weather'][0]['hourly'][0]['weatherDesc'][0]['value'],
        'icon' : r['data']['weather'][0]['hourly'][0]['weatherIconUrl'][0]['value'],
    }

    city_weather_2 = {
        'city': city,
        'temperature': r['data']['weather'][1]['avgtempC'],
        'description': r['data']['weather'][1]['hourly'][0]['weatherDesc'][0]['value'],
        'icon': r['data']['weather'][1]['hourly'][0]['weatherIconUrl'][0]['value'],
    }

    city_weather_3 = {
        'city': city,
        'temperature': r['data']['weather'][2]['avgtempC'],
        'description': r['data']['weather'][2]['hourly'][0]['weatherDesc'][0]['value'],
        'icon': r['data']['weather'][2]['hourly'][0]['weatherIconUrl'][0]['value'],
    }

    city_weather_4 = {
        'city': city,
        'temperature': r['data']['weather'][3]['avgtempC'],
        'description': r['data']['weather'][3]['hourly'][0]['weatherDesc'][0]['value'],
        'icon': r['data']['weather'][3]['hourly'][0]['weatherIconUrl'][0]['value'],
    }

    city_weather_5 = {
        'city': city,
        'temperature': r['data']['weather'][4]['avgtempC'],
        'description': r['data']['weather'][4]['hourly'][0]['weatherDesc'][0]['value'],
        'icon': r['data']['weather'][4]['hourly'][0]['weatherIconUrl'][0]['value'],
    }



    context = {'city_weather1' : city_weather_1,
               'city_weather2' : city_weather_2,
               'city_weather3' : city_weather_3,
               'city_weather4' : city_weather_4,
               'city_weather5' : city_weather_5}

    return render(request,'weather.html',context)

HttpResponse('Hello')