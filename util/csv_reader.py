import csv

from env import root_path
from model.hash_map import HashMap


def parse_string_cvs(file_path, x=0, y=1):
    hashmap = HashMap()
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            hashmap.add(row[x], row[y])
    return hashmap


def parse_cvs(file_path, x=0, y=1):
    hashmap = HashMap()
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            hashmap.add(int(row[x]), row[y])
    return hashmap


def reverse_parse_cvs(file_path, x=1, y=0):
    hashmap = HashMap()
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            hashmap.add(row[x], int(row[y]))
    return hashmap


def parse_package_file():
    hashmap = HashMap()
    with open(root_path + '/data/wgups_package_file.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            hashmap.add(int(row[0]), (row[1], row[2], row[4], row[5], row[6]))
    return hashmap
