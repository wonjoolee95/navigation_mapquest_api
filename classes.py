# _author = Won Joo Lee


class Steps:
    '''
    class of STEPS command, has the duck-typable function print_data()
    '''
    def __init__(self, mapquest_json):
        self._mapquest_json = mapquest_json
    def print_data(self):
        print('DIRECTIONS')
        for i in self._mapquest_json['route']['legs']:
            for j in i['maneuvers']:
                print(j['narrative'])


class Latlong:
    '''
    class of LLATLONG command, have 2 functions:
    1. duck-typable fuction print_data()
    2. latlong_list function, which returns a list of lat and long
    of locations when given a list of locations in str
    e.g., Latlong(['Irvine', 'LA']).latlong_list   --->   [-123.123, 123.123]
    '''
    def __init__(self, mapquest_json):
        self._mapquest_json = mapquest_json
        self._latlong_list = []
    def print_data(self):
        print('LATLONGS')
        for i in self._mapquest_json['route']['locations']:
            if i['latLng']['lat'] >= 0:
                    print('{:5.2f} N'.format(i['latLng']['lat']), end = ' ')
            else:
                    print('{:5.2f} S'.format(abs(i['latLng']['lat'])), end = ' ')
            if i['latLng']['lng'] >= 0:
                    print('{:5.2f} E'.format(i['latLng']['lng']))
            else:
                    print('{:5.2f} W'.format(abs(i['latLng']['lng'])))
    def latlong_list(self) -> list:
        for i in self._mapquest_json['route']['locations']:
            self._latlong_list.append(i['latLng']['lat'])
            self._latlong_list.append(i['latLng']['lng'])
        return self._latlong_list
                    


class Totaldistance:
    '''
    class of TOTALDISTANCE command, has the duck-typable function print_data()
    '''
    def __init__(self, mapquest_json):
        self._mapquest_json = mapquest_json
    def print_data(self):
        print('TOTAL DISTANCE: {:.0f} miles'.format(self._mapquest_json['route']['distance']))

        
class Totaltime:
    '''
    class of TOTALTIME command, has the duck-typable function print_data()
    '''
    def __init__(self, mapquest_json):
        self._mapquest_json = mapquest_json
    def print_data(self):
        print('TOTAL TIME: {:.0f} minutes'.format(self._mapquest_json['route']['time']/60))


class Elevation:
    '''
    class of ELEVATION command, has te duck-typable function print_data()
    '''
    def __init__(self, elevation_mapquest_json_list):
        self._elevation_mapquest_json_list = elevation_mapquest_json_list
    def print_data(self):
        print('ELEVATIONS')
        for i in self._elevation_mapquest_json_list:
            print('{:.0f}'.format(i['elevationProfile'][0]['height'] * 3.28))

            
