from django.core.management.base import BaseCommand
from corona_website_app.models import Country
import pandas as pd
import urllib.request

class Command(BaseCommand):
    def get_data(self, data_url):
        csv = urllib.request.urlretrieve(data_url)

        data = pd.read_csv(csv[0])

        countries = list(set(data['Country/Region']))
        countries.sort()

        ret = {}
        for country in countries:
            filtered = data[(data['Country/Region'] == country)]
            # total = sum(filtered['4/26/20'])
            total = sum(filtered[filtered.columns[-1]])
            ret[country] = total

        return ret


    def handle(self, *args, **kwargs):
        Country.objects.all().delete()

        cases_by_country = self.get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

        deaths_by_country = self.get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

        recoveries_by_country = self.get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

        countries = [i for i in cases_by_country]

        consolidated = []

        for country in countries:
            new_country = Country(
                name = country,
                num_cases = cases_by_country[country],
                num_recoveries = recoveries_by_country[country],
                num_deaths = deaths_by_country[country],
            )

            # consolidated.append(new_country)
            new_country.save()
