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
    x_labels = Dates.objects.all()[0].dates[0:2]

    context = {
        'x_labels' : json.dump(x_labels),
    }

    return render(request, 'corona_website_app/charts.html', context=context)
