from django.shortcuts import render, redirect
from django.http import HttpResponse
from corona_website_app.models import Country, Dates
import json

def index(request):
    consolidated = Country.objects.all()
    last_updated = str(Dates.objects.all()[0].dates[-1])

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


def individual_chart(request):
    country_to_chart = request.COOKIES['indv_country_to_chart']
    country_to_chart = Country.objects.filter(name=country_to_chart).values()

    x_labels = Dates.objects.all()[0].dates

    context = {
        'x_labels' : json.dumps(x_labels),
        'country' : json.dumps(country_to_chart),
    }

    return render(request, 'corona_website_app/chart_individual.html', context=context)
