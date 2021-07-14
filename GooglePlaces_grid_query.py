# Import external libraries
import googlemaps
import pandas as pd
import os, glob

# Replace your personal API-key to make successfull calls
# for more information on how to obtain a key visit: https://developers.google.com/maps/documentation/places/web-service/get-api-key
API_KEY = "#"

# Make subdirectories for output files 
subdir = "output"
subsubdir = "data_type"

main = os.getcwd()

try:
	os.mkdir(os.path.join(main, subdir))
except:
	print("subdir already existing")

try:
	os.mkdir(os.path.join(main, subdir, subsubdir))
except:
	print("subsubdir already existing")

# Define locations 
df_grid = pd.read_csv('data/location_grid_DUMMY.csv', sep=';')

# Define dataframe 
df_category = pd.read_csv('data/types_selection_DUMMY.csv', sep=';')
for i in df_category.index:

	if df_category['Select'][i] == 'yes':

		type_i = df_category['Type-Places'][i]
		category = df_category['Category'][i]

		df = pd.DataFrame()
		
		
		for i in df_grid.index:
			grid_lng = df_grid['lng'][i]
			grid_lat = df_grid['lat'][i]
			
			lat_lng = str(grid_lat) + ',' + str(grid_lng)
			
			gmaps = googlemaps.Client(key=API_KEY)
			
			places_result = gmaps.places_nearby(location=lat_lng, radius=1000, open_now=False, type='type_i')
			
			stored_results = places_result['results']
			
			for j in range(len(stored_results)):
				dict = stored_results[j]
				lat = dict['geometry']['location']['lat']
				lng = dict['geometry']['location']['lng']
				name = dict['name']
				place_id = dict['place_id']

				df = df.append({'lat' : lat, 'lng' : lng, 'name' : name, 'place_id' : place_id, 'type' : type_i, 'cat' : category}, ignore_index=True)

				# Remove duplicates based on place_id
				df = df.drop_duplicates(subset=['place_id'], keep=False)

		type_file = str(type_i) + '.csv'
		df.to_csv(os.path.join(subdir, subsubdir, type_file))
		print(type_i + "___exported")

	else:		
		next

# Merge types_*.csv into one
all_files = glob.glob(os.path.join(subdir, subsubdir, "*.csv"))

df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)

df_merged.to_csv(os.path.join(subdir, "places.csv"), sep=";")
