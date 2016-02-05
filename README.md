# navigation_mapquest_api
A simple navigation system written in Python, using the free API from mapquest.com.

Download all files in the same folder the run the ' user_interface.py ' file to run the program.

The purpose of the program was to practice simple interactions of API using python; therefore, the program does not catch extensive exceptions. The inputs must be typed precisely.

Sample interaction (note the precise input):

>>>


Welcome to the GPS system!

How many locations will the trip consist? 2

Please enter the address: 113 Oxford Irvine, CA 92612
Please enter the address: 1858 W. Falmouth Anaheim, CA 92801

How many types of data do you want? 
Options: STEPS, LATLONG, TOTALDISTANCE, TOTALTIME, ELEVATION 
(Enter a number): 5

Please enter your #1 desired data type: 
Options: STEPS, LATLONG, TOTALDISTANCE, TOTALTIME, ELEVATION 
Type precisely: STEPS
Please enter your #2 desired data type: 
Options: STEPS, LATLONG, TOTALDISTANCE, TOTALTIME, ELEVATION 
Type precisely: LATLONG
Please enter your #3 desired data type: 
Options: STEPS, LATLONG, TOTALDISTANCE, TOTALTIME, ELEVATION 
Type precisely: TOTALDISTANCE
Please enter your #4 desired data type: 
Options: STEPS, LATLONG, TOTALDISTANCE, TOTALTIME, ELEVATION 
Type precisely: TOTALTIME
Please enter your #5 desired data type: 
Options: STEPS, LATLONG, TOTALDISTANCE, TOTALTIME, ELEVATION 
Type precisely: ELEVATION

DIRECTIONS
Start out going northwest on Columbia toward Georgetown.
Turn right onto Harvard Ave.
Turn left onto Culver Dr.
Merge onto I-405/San Diego Fwy.
Take the Jamboree Rd exit, EXIT 7.
Turn right onto Jamboree Rd.
Stay straight to go onto CA-261 Toll/Eastern Transportation Corridor. Continue to follow Eastern Transportation Corridor (Portions toll).
Merge onto CA-91/Riverside Fwy via EXIT 39A;39B toward Riverside.
Merge onto I-15 E via EXIT 51 (Passing through Nevada and Arizona, then crossing into Utah).
Merge onto I-70 E via EXIT 132 (Crossing into Colorado).
Take the US-36 exit, EXIT 316.
Turn left onto US-36/N Main St. Continue to follow US-36 (Crossing into Kansas).
Welcome to US.

LATLONGS
33.65 N 117.83 W
39.78 N 100.45 W

TOTAL DISTANCE: 1272 miles

TOTAL TIME: 1144 minutes

ELEVATIONS
112
2732

Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors

>>> 
