import csv_distance_calculation
import csv_filtering_to_time
import json
from flight_path_3d import map3D
from flight_path_2d import map2D

flight_distance = csv_distance_calculation.calculate_distance()
flight_time = csv_filtering_to_time.calculate_time()
map3D('junelogs.txt')
map2D('junelogs.txt')

output = {
    'flight_distance': flight_distance,
    'flight_time': flight_time,
}

with open('flight_details.json', 'w') as fp:
    json.dump(output, fp)

# TODO
# Code > Reformat Code ( cleans thr formatting the code) _/
# Do the same change to 2D file _/
# Clean up the front-end
# Add option to have 2d or 3d and options between flights
# Request access to other text files
# In main change all methods to have a single file input
