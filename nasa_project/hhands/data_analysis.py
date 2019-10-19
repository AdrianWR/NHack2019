import pandas as pd
import requests


def getClimaticEvents():
    climate_events = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events').json()
    print(climate_events)