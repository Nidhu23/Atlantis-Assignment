import re

import geopy.distance


def find_next_closest_city(gps_coordinates, current_city, cities_covered):
    shortest_distance = None
    closest_city = None
    for city, coords in gps_coordinates.items():
        if city in cities_covered:
            continue
        if not closest_city:
            closest_city = city
            shortest_distance = geopy.distance.geodesic(gps_coordinates[current_city], gps_coordinates[city]).miles
        else:
            temp_distance = geopy.distance.geodesic(gps_coordinates[current_city], gps_coordinates[city]).miles
            if temp_distance < shortest_distance:
                shortest_distance = temp_distance
                closest_city = city
    return closest_city


def get_path_to_travel():
    travel_path = cities_to_travel[0]
    start_city = cities_to_travel[0]
    current_city = start_city
    cities_covered = []
    while len(cities_to_travel) > len(cities_covered):
        if start_city not in cities_covered:
            cities_covered.append(start_city)
        closest_city = find_next_closest_city(gps_coordinates, current_city, cities_covered)
        travel_path += " to {}".format(closest_city)
        current_city = closest_city
        cities_covered.append(current_city)
    return travel_path


if __name__ == "__main__":
    gps_coordinates = {}
    cities_to_travel = ["A", "B", "C", "D"]
    for key in cities_to_travel:
        latitude, longitude = input("City {}: ".format(key)).split(',')
        gps_coordinates[key] = (
            float(re.findall("\d+\.\d+", latitude)[0]) * (-1 if re.search('[swSW]', latitude) else 1),
            float(re.findall("\d+\.\d+", longitude)[0]) * (-1 if re.search('[swSW]', longitude) else 1))
    print("Output {}".format(get_path_to_travel()))
