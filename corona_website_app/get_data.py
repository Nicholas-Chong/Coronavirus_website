import pandas as pd
import urllib.request

class Country():
    def __init__(self, name, cases, recoveries, deaths):
        self.name = name
        self.num_cases = cases
        self.num_recoveries = recoveries
        self.num_deaths = deaths


def get_data(data_url):
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


