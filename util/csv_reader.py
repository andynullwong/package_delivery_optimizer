import csv

from model.hash_map import HashMap


def parse_cvs(file_path, invert=False):
    hashmap = HashMap()
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if invert:
                hashmap.add(row[2], row[1])
            else:
                hashmap.add(int(row[0]), row[1])
    return hashmap
