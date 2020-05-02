from django.shortcuts import render, redirect
from django.http import HttpResponse
from corona_website_app.models import Country, Dates
import json

def index(request):
    consolidated = Country.objects.all()

    context = {
        'consolidated' : consolidated
    } 
    
    return render(request, 'corona_website_app/index.html', context=context)


def charts(request):
    x_labels = Dates.objects.all()[0].dates
    countrys = Country.objects.all()

    cases_data = {}
    names = []
    for country in countrys:
        cases_data[country.name] = country.daily_confirmed_cases
        names.append(country.name)

    context = {
        'x_labels' : json.dumps(x_labels),
        'cases_data' : json.dumps(cases_data)
        'country_names' : names
    }

    return render(request, 'corona_website_app/charts.html', context=context)
