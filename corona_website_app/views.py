from django.shortcuts import render, redirect
from django.http import HttpResponse
from corona_website_app.models import Country

def index(request):
    consolidated = Country.objects.all()

    context = {
        'consolidated' : consolidated
    } 
    
    return render(request, 'corona_website_app/index.html', context=context)
