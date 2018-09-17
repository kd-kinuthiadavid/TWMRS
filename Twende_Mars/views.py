from django.shortcuts import render
import requests as getter
from django.contrib.auth.decorators import login_required



# Create your views here.
def welcome(request):
    title = 'Welcome'
    return render(request, 'welcome.html', locals())

def photos(request):
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'welcome.html', locals())

@login_required
def september_first(request):
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2018-9-1&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'september.html', locals())

@login_required
def navcam(request):
    cmr = 'navcam'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=navcam&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'searching.html', locals())

@login_required
def fhaz(request):
    cmr = 'fhaz'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'fhaz.html', locals())

@login_required
def mast(request):
    cmr = 'mast'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&camera=mast&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'mast.html', locals())

@login_required
def chemcam(request):
    cmr = 'chemcam'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=chemcam&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'chemcam.html', locals())

@login_required
def mahli(request):
    cmr = 'mahli'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=mahli&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'mahli.html', locals())

@login_required
def mardi(request):
    cmr = 'mardi'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=MARDI&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'mardi.html', locals())

@login_required
def rhaz(request):
    cmr = 'rhaz'
    response = getter.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=rhaz&api_key=97Df6qNjaKOwkQRo3epJlGQfq41KjXcuwaQhosQP')
    data = response.json()
    images = data['photos']
    return render(request, 'rhaz.html', locals())




