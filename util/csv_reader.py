import csv

from util.hash_map import HashMap


def get_hub_hashmap():
    hub_hm = HashMap()
    with open('../data/wgups_hub_file.csv') as hub_csv:
        csv_reader = csv.reader(hub_csv)
        for row in csv_reader:
            hub_hm.add(int(row[0]), row[1])
    return hub_hm


def get_hubs():
    return hub_hashmap


def get_iterable_hubs():
    hubs_array = []
    for i in range(len(get_hubs())):
        hubs_array.append(get_hubs().get(i))
    return hubs_array


def get_distance_hashmap():
    # Initialize Empty nested hashmap
    distance_hm = HashMap()
    for hub in get_iterable_hubs():
        distance_hm.add(hub, HashMap())

    with open('../data/wgups_distance_table.csv') as distance_csv:
        csv_reader = csv.reader(distance_csv)
        for distance_id, distance_list in enumerate(csv_reader):
            location1 = hub_hashmap.get(distance_id)

            for idx, distance in enumerate(distance_list):
                location2 = hub_hashmap.get(idx)
                if distance != '' and distance != '0.0':
                    distance_hm.get(location1).add(location2, distance)
                    distance_hm.get(location2).add(location1, distance)
    return distance_hm


hub_hashmap = get_hub_hashmap()
distance_matrix = get_distance_hashmap()


def get_distance_matrix():
    return distance_matrix
