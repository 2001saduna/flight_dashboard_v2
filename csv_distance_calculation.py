from math import asin, cos, sqrt
import parser_1

result = parser_1.readTextFile('junelogs.txt')


def get_coordinates(pos, result):
    lat = result[pos]['latitude']
    long = result[pos]['longitude']
    return lat, long


def calculate_distance():
    distance = []
    for i in range(0, len(result) - 1, 2):
        lat_1, long_1 = get_coordinates(i, result)
        lat_2, long_2 = get_coordinates(i + 1, result)

        p = 0.017453292519943295  # Pi/180
        a = 0.5 - cos((lat_2 - lat_1) * p) / 2 + cos(lat_1 * p) * cos(lat_2 * p) * (1 - cos((long_2 - long_1) * p)) / 2
        d = 12742 * asin(sqrt(a))  # 2*R*asin...
        distance.append(d)

    total_distance = sum(distance)
    rounded_total_distance = round(total_distance, 2)

    return rounded_total_distance
