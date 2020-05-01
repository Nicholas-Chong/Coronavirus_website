import plotly.express as px
import pandas as pd
from django.core.management.base import BaseCommand
import urllib.request

class Command(BaseCommand):
    def create_graph(self, data):
        xy = {'Date' : data.columns, 'Number of Cases' : data.iloc[0]}
        xy = pd.DataFrame(data=xy)

        fig = px.line(xy, x='Date', y='Number of Cases')
        # fig.show()

    def handle():
        csv = urllib.request.urlretrieve('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        data = pd.read_csv(csv[0])

        for country in set(data['Country/Region']):
            # print(country)
            country_data = data[data['Country/Region'] == country]
            country_data = country_data.drop(columns=us.columns[0:4])

            create_graph(country_data)