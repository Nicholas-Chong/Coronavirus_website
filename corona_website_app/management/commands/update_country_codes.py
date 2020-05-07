from django.core.management.base import BaseCommand
from corona_website_app.models import Country, Dates
import urllib.request
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = urllib.request.urlretrieve('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv')
        data = pd.read_csv(data[0])
        data = data.drop(columns=['alpha-2', 'country-code', 'iso_3166-2', 'region', 'sub-region', 'intermediate-region', 'region-code', 'sub-region-code', 'intermediate-region-code'])

        # print(data.query('name == "Afghanistan"'))
        country_list = data.name.to_list()

        for conutry in Country.objects.all():
            if country.name in country_list:
                query_string = 'name == "' + country.name + '"'
                print(data.query(query_string))