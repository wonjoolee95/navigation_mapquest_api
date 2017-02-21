# Won Joo Lee

import classes
import mapquest_api

def receive_locations() -> list:
    '''
    returns a list of locations with that many inputs
    '''
    locations = []
    locations.append(input("FROM: "))
    locations.append(input("TO: "))
    return locations

def receive_commands(mapquest_json, elevation_json_list) -> list:
    '''
    returns a list of duck-typable class constructors,
    which does not need to specify which classes since
    all class values can be duck-typed by the fucntion print_data()
    '''
    final_commands = []
    commands = ["STEPS", "LATLONG", "TOTALDISTANCE", "TOTALTIME"]
    for command in commands:
        if command == 'STEPS':
            final_commands.append(classes.Steps(mapquest_json))
        elif command == 'LATLONG':
            final_commands.append(classes.Latlong(mapquest_json))
        elif command == 'TOTALDISTANCE':
            final_commands.append(classes.Totaldistance(mapquest_json))
        elif command == 'TOTALTIME':
            final_commands.append(classes.Totaltime(mapquest_json))
        elif command == 'ELEVATION':
            final_commands.append(classes.Elevation(elevation_json_list))
    return final_commands
                                  
def receive_mapquest_json(locations: list) -> 'two jsons':
    '''
    given the list of places, returns two things:
    1. one normal (direction) mapquest_json
    2. a LIST of elevation json for each location
    '''
    elevation_json_list = []

    mapquest_json = mapquest_api.receive_response(
        mapquest_api.create_search_url(locations))
    elevation_urls = mapquest_api.create_elevation_search_url(
            classes.Latlong(mapquest_json).latlong_list())
    for url in elevation_urls:
        elevation_json_list.append(mapquest_api.receive_response(url))
        
    return mapquest_json, elevation_json_list

def run_user_interface() -> None:
    '''
    main user interface function;
    calls appropriate fucntions to produce final data;
    has a try, except structure to catch a very general failure
    '''
    print()
    print('Welcome to the GPS system!')
    print()
    try:                                
        locations = receive_locations()
        print()
        mapquest_json, elevation_json_list = receive_mapquest_json(locations)                
        commands = receive_commands(mapquest_json, elevation_json_list)
        print()
        for i in commands:
            i.print_data()
            print()
        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
        print()
    except:
        print('Error; please run the program again.')


if __name__ == '__main__':
    run_user_interface()
