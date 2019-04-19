import googlemaps 

from datetime import datetime 

gmaps = googlemaps.Client(key='AIzaSyCvRQF16JMKd8Mj2oZ88b2DM-RHrpIKatQ')

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall", "Parramatta, NSW", mode="transit", departure_time=now)

print (type(directions_result))
