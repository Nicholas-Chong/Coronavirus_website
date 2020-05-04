from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('charts', views.charts, name='charts'),
    path('individual_chart', views.individual_chart, name='individual_chart'),
    path('about', views.about, name='about'),
]
