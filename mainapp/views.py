from django.shortcuts import render,redirect

from .models import cities
import requests

# Create your views here.

def homepage(request):
    api_key = "cabf962b328913196eb7308d584ad604"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}'
    weatherdata=[]

    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            addcity=cities.objects.create(city=city)
            addcity.save()
            return redirect('/')

    citieslist=cities.objects.all()
    for city in citieslist:
        get_weather=requests.get(url.format(city,api_key)).json()
        print(get_weather)
        try:
            weather={
                'city':city,
                'temp':get_weather['main']['temp'],
                'desc':get_weather['weather'][0]['description'],
                'icon':get_weather['weather'][0]['icon'],
            }
            weatherdata.append(weather)
        except :
            pass
    context={'weatherdata':weatherdata}
    print(context)
    return render(request,'weatherpage.html',context)