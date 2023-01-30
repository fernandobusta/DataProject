# pip install googlemaps
# pip install prettyprint

import googlemaps
import pprint
import time # to pause the script for a few seconds to let the next page token run
from apiK import * # This imports the api key from my secret file

# import function to return api key

# Define our API key
API_KEY = api_key()

# Define our clients
gmaps = googlemaps.Client(key = API_KEY) # authenticate to make a request

# Define our Search
# Change the location to your liking
places_result = gmaps.places_nearby(location='52.83910519419793, -6.9262904520866595', radius = 40000, open_now = False, type = 'cafe')


# Pause the script for 3 seconds
#time.sleep(3)
#		This is because the next page results aren't loaded in the database yet
# Get the next 20 results
#places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])

#pprint.pprint(places_result)



# Loop through each place in the results
for place in places_result['results']:

	# Define  my place id
	my_place_id = place['place_id']

	# Define the fields we want sent back to us
	my_fields = ['name', 'formatted_phone_number', 'type']

	# make a request for the details
	place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

	# print results
	print(place_details)
