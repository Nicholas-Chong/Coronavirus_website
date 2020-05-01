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
    x_labels = json.dump(Dates.objects.all()[0].dates)

    context = {
        'x_labels' : x_labels,
    }

    return render(request, 'corona_website_app/charts.html', context=context)
