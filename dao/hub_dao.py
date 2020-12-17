import csv

from env import root_path
from util.csv_reader import parse_cvs
from model.hash_map import HashMap

hub_hashmap = parse_cvs(root_path + '/data/wgups_hub_file.csv')
address_to_hub_hashmap = parse_cvs(root_path + '/data/wgups_hub_file.csv', True)


def get_distance_hashmap():
    # Initialize Empty nested hashmap
    distance_hm = HashMap()
    for hub in hub_hashmap:
        distance_hm.add(hub[1], HashMap())

    with open(root_path + '/data/wgups_distance_table.csv') as distance_csv:
        csv_reader = csv.reader(distance_csv)
        for distance_id, distance_list in enumerate(csv_reader):
            location1 = hub_hashmap.get(distance_id)

            for idx, distance in enumerate(distance_list):
                location2 = hub_hashmap.get(idx)
                if distance != '' and distance != '0.0':
                    distance_hm.get(location1).add(location2, distance)
                    distance_hm.get(location2).add(location1, distance)
    return distance_hm


distance_matrix = get_distance_hashmap()

# print(hub_hashmap.get(0))  # Western Governors University
# print(distance_matrix.get('Western Governors University').get('Cottonwood Regional Softball Complex'))  # 1.9
# print(address_to_hub_hashmap.get('195 W Oakland Ave'))  # South Salt Lake Public Works
