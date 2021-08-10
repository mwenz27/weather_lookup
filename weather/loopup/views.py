from django.shortcuts import render
from . import config


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        print(zipcode)
        api_url = config.API_URL
        # removing the old zip code
        api_url = api_url[0:90] + zipcode + api_url[-57:]
        api_request = requests.get(api_url)
        print(api_request)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error ...'

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 to 50 Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "51 to 100 Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 to 150 Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "sunhealthy"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 to 200 Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "vunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"
        else:
            category_description = "Error in api call"
            category_color = "red"

        return render(request, 'home.html', {'api': api,
                                         'category_description': category_description,
                                         'category_color': category_color,
                                              })

    else:
        # get request
        api_request = requests.get(config.API_URL)
        print(api_request)
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = 'Error ...'

        if api[0]['Category']['Name'] == "Good":
            category_description = "0 to 50 Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "51 to 100 Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "101 to 150 Members of sensitive groups may experience health effects. The general public is less likely to be affected."
            category_color = "sunhealthy"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "151 to 200 Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "Health alert: The risk of health effects is increased for everyone."
            category_color = "vunhealthy"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_description = "Health warning of emergency conditions: everyone is more likely to be affected."
            category_color = "hazardous"
        else:
            category_description = "Error in api call"
            category_color = "red"

    return render(request, 'home.html', {'api': api,
                                         'category_description': category_description,
                                         'category_color': category_color
                                         })


def about(request):
    return render(request, 'about.html', {})
