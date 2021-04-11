# Import external libraries
import googlemaps
import pandas as pd
import os, glob

subdir = 'output/type_data/'

# Define locations 
df_grid = pd.read_csv('data/location_grid.csv', sep=';')

# Define dataframe 
df_category = pd.read_csv('data/types_selection.csv', sep=';')
for i in df_category.index:

	if df_category['Select'][i] == 'no':
		next

	type_i = df_category['Type-Places'][i]
	category = df_category['Category'][i]
	
	df = pd.DataFrame()
	
	for i in df_grid.index:
		grid_lng = df_grid['lng'][i]
		grid_lat = df_grid['lat'][i]
		
		lat_lng = str(grid_lat) + ',' + str(grid_lng)
		
		API_KEY = "AIzaSyDnOul-4GRXiQGTcMXeqiEsHzOe4jeILNA"
		gmaps = googlemaps.Client(key=API_KEY)
		
		#print(lat_lng + type_i)
		places_result = gmaps.places_nearby(location=lat_lng, radius=1000, open_now=False, type=type_i)
		
		stored_results = places_result['results']
		
		for j in range(len(stored_results)):
			dict = stored_results[j]
			lat = dict['geometry']['location']['lat']
			lng = dict['geometry']['location']['lng']
			name = dict['name']
			place_id = dict['place_id']
			df = df.append({'lat' : lat, 'lng' : lng, 'name' : name, 'place_id' : place_id, 'type' : type_i, 'cat' : category}, ignore_index=True)

	type_file = subdir + str(type_i) + '.csv'		
	df.to_csv(type_file)
	print('loop:' + str(i))

# Merge types_*.csv into one
all_files = glob.glob(os.path.join(subdir, "*.csv"))

df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged   = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv( "output/places.csv", sep=";")