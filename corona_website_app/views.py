from django.shortcuts import render, redirect
from django.http import HttpResponse
from .get_data import get_data, Country

def index(request):
    cases_by_country = get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

    deaths_by_country = get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

    recoveries_by_country = get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

    countries = [i for i in cases_by_country]

    consolidated = []

    for country in countries:
        new_country = Country(
            country, 
            cases_by_country[country],
            recoveries_by_country[country],
            deaths_by_country[country],
        )

        consolidated.append(new_country)

    context = {
        'consolidated' : consolidated
    } 
    
    return render(request, 'corona_website_app/index.html', context=context)
