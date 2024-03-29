import json
import requests

# NASA Natural Disasters Climatic Database Raw Data
CLIMATIC_DATABASE_URL = 'https://eonet.sci.gsfc.nasa.gov/api/v2.1/events'


def getClimaticEvents(n):
    headers = {'Content-Type': 'application/json'}
    response = requests.get(CLIMATIC_DATABASE_URL + '?limit=' + str(n), headers=headers)
    response.raise_for_status()
    climatic_events = response.json()

    d = {'type': 'FeatureCollection', 'features': []}
    for i in range(n):
        d['features'].append({'type': 'Feature',
                              'geometry': {'type': climatic_events['events'][i]['geometries'][0]['type'],
                                           'coordinates': climatic_events['events'][i]['geometries'][0]['coordinates']},
                              'properties': {'event_id': climatic_events['events'][i]['id'],
                                             'event_title': climatic_events['events'][i]['title'],
                                             'event_date': climatic_events['events'][i]['geometries'][0]['date'],
                                             'event_category': climatic_events['events'][i]['categories'][0]['title']
                                             }})
    return json.dumps(d, indent=2)


# Test Area
if __name__ == "__main__":
    print(getClimaticEvents(10))
    pass
