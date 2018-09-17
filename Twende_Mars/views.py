from django.shortcuts import render
import requests as getter


# Create your views here.
def welcome(request):
    title = 'Welcome'
    return render(request, 'welcome.html', locals())

def photos(request):
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'welcome.html', locals())
