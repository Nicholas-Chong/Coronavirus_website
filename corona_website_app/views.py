from django.shortcuts import render, redirect
from django.http import HttpResponse
from corona_website_app.models import Country, Dates
import json

def index(request):
    consolidated = Country.objects.all()
    last_updated = str(Dates.objects.all()[0][-1])

    context = {
        'consolidated' : consolidated,
        'last_updated' : last_updated,
    } 
    
    return render(request, 'corona_website_app/index.html', context=context)


def charts(request):
    x_labels = Dates.objects.all()[0].dates
    countrys = list(Country.objects.all().values())

    # cases_data = {}
    # names = []
    # for country in countrys:
    #     cases_data[country.name] = country.daily_confirmed_cases
    #     names.append(country.name)

    context = {
        'x_labels' : json.dumps(x_labels),
        'countries_json' : json.dumps(countrys),
        'countries' : countrys
    }

    return render(request, 'corona_website_app/charts.html', context=context)
