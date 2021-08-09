from django.shortcuts import render
from . import config


def home(request):
    import json
    import requests

    api_request = requests.get(config.API_URL)
    print(api_request)
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error ...'
    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
