# _author = Won Joo Lee

import json
import urllib.parse
import urllib.request

MAPQUEST_API_KEY = 'ljA2ixNy0JufkQNV2It9cIb8dljyrtTh'
MAPQUEST_BASE_URL = 'http://open.mapquestapi.com/directions/v2/route?'

MAPQUEST_ELEVATION_BASE_URL = 'http://open.mapquestapi.com/elevation/v1/profile?'

def create_search_url(locations: list) -> str:
    '''
    creates search url for non-elevation json, using urrlib.parse.encode
    '''
    query_parameters = [
        ('key', MAPQUEST_API_KEY), ('ambiguities', 'ignore'),
        ('from', locations[0])]
    for i in range(1, len(locations)):
        query_parameters.append(('to', locations[i]))
    return MAPQUEST_BASE_URL + urllib.parse.urlencode(query_parameters)

def create_elevation_search_url(latlong_list: list) -> list:
    '''
    creates a list of elevation json urls, each url having
    ONE PAIR of latlong
    '''

    all_urls = []

    for i in range(0, len(latlong_list), 2):
        query_parameters = [
            ('key', MAPQUEST_API_KEY)]
        query_parameters.append(('latLngCollection',
                                 (str(latlong_list[i]) + ',' + str(latlong_list[i+1]))))
        all_urls.append(MAPQUEST_ELEVATION_BASE_URL +urllib.parse.urlencode(query_parameters))
                                
        
    return all_urls

def receive_response(url: str) -> 'json':
    '''
    given the url of the json, returns the json
    '''
    data = None
    try:
        data = urllib.request.urlopen(url)
        json_text = data.read().decode(encoding = 'utf-8')
        return json.loads(json_text)
    finally:
        if data != None:
            data.close()



