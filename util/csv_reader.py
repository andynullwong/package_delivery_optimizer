import csv

from util.hash_map import HashMap


def parse_cvs(file_path):
    hashmap = HashMap()
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            hashmap.add(int(row[0]), row[1])
    return hashmap
