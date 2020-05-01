from django.core.management.base import BaseCommand
from corona_website_app.models import Country, Dates
import urllib.request
import pandas as pd

class Command(BaseCommand):
    def get_data(self, data_url):
        csv = urllib.request.urlretrieve(data_url)

        data = pd.read_csv(csv[0])

        countries = list(set(data['Country/Region']))
        countries.sort()

        ret = {}
        for country in countries:
            filtered = data[(data['Country/Region'] == country)]
            total = sum(filtered[filtered.columns[-1]])
            ret[country] = total

        return ret


    def handle(self, *args, **kwargs):
        Country.objects.all().delete()
        Dates.objects.all().delete()

        daily_confirmed_cases = urllib.request.urlretrieve('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

        cases_by_country = self.get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

        deaths_by_country = self.get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

        recoveries_by_country = self.get_data('https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')

        countries = [i for i in cases_by_country]

        daily_confirmed_cases = pd.read_csv(daily_confirmed_cases[0])
        new_dates = Dates(dates=list(daily_confirmed_cases.columns[4:])).save()

        for country in countries:
            daily_country_cases = daily_confirmed_cases[daily_confirmed_cases['Country/Region'] == country]
            daily_country_cases = daily_country_cases.drop(columns=daily_country_cases.columns[0:4])

            dates = list(daily_country_cases.columns)
            cases = daily_country_cases.values.tolist()[0]
            daily_country_cases = [str(dates[i]) + ' ' + str(cases[i]) for i in range(0, len(dates))]

            new_country = Country(
                name = country,
                num_cases = cases_by_country[country],
                num_recoveries = recoveries_by_country[country],
                num_deaths = deaths_by_country[country],
                daily_confirmed_cases = daily_country_cases,
            )

            new_country.save()
            
