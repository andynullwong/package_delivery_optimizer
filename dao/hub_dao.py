import csv

from env import root_path
from util.csv_reader import parse_cvs, parse_string_cvs
from model.hash_map import HashMap

id_hub_map = parse_cvs(root_path + '/data/wgups_hub_file.csv')
address_hub_map = parse_string_cvs(root_path + '/data/wgups_hub_file.csv', 2, 1)


# Helper function to lookup distance between two locations
def get_distance_to_hub(current_hub_name, next_hub_name):
    distance = distance_matrix.get(current_hub_name).get(next_hub_name)
    if distance is not None:
        return float(distance)
    else:
        return 0.0


# 2D HashMap to create a matrix of distances between every combination of two hubs
def get_distance_hashmap():
    distance_hm = HashMap()
    for hub in id_hub_map:
        distance_hm.add(hub[1], HashMap())

    with open(root_path + '/data/wgups_distance_table.csv') as distance_csv:
        csv_reader = csv.reader(distance_csv)
        for distance_id, distance_list in enumerate(csv_reader):
            location1 = id_hub_map.get(distance_id)

            for idx, distance in enumerate(distance_list):
                location2 = id_hub_map.get(idx)
                if distance != '' and distance != '0.0':
                    distance_hm.get(location1).add(location2, distance)
                    distance_hm.get(location2).add(location1, distance)
    return distance_hm


distance_matrix = get_distance_hashmap()
