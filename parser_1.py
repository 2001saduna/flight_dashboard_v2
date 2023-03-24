import re
from ast import literal_eval

textfile = 'junelogs.txt'
def readTextFile (textfile):
    flight_data = []
    with open(textfile, "r") as f:
        date_regex = re.compile('\d{2}\/\d{2}\/\d{2}')
        time_regex = re.compile('\d{2}:\d{2}:\d{2}')
        for line in f:
            individual_flight_data = {}
            tokens = [token.strip() for token in line.split(' - ')]
            try:
                date = re.search(date_regex, tokens[0]).group()
            except:
                continue
            time = re.search(time_regex, tokens[1]).group()
            location = literal_eval(tokens[2])
            longitude = location['gps']['longitude']
            latitude = location['gps']['latitude']

            if latitude == 0 and longitude == 0:
                continue

            altitude = location['gps']['altitude']
            individual_flight_data['date'] = date
            individual_flight_data['time'] = time
            individual_flight_data['longitude'] = longitude
            individual_flight_data['latitude'] = latitude
            individual_flight_data['altitude'] = altitude
            flight_data.append(individual_flight_data)

    return(flight_data)
