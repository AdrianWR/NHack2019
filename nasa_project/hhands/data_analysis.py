import pandas as pd
import requests, json

# NASA Natural Disasters Climatic Database Raw Data
CLIMATIC_DATABASE_URL = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'

def getClimaticEvents():
    headers = {'Content-Type': 'application/json'}
    response = requests.get(CLIMATIC_DATABASE_URL, headers = headers)
    response.raise_for_status()
    climatic_events = response.json()
    print(climatic_events)
    pass


# Test Area
if __name__ == "__main__":
    getClimaticEvents()
    pass
    
    