from dao.history_dao import history
from model.clock import string_to_timestamp


def lookup():
    is_active = input("\nWould you like to lookup a package (Y/N)? ")
    while is_active == "Y":
        package_id = input("\nEnter Package ID: ")
        raw_timestamp = input("\nEnter a time (ie: 11:11:00): ")
        timestamp = string_to_timestamp("2020-01-01 " + raw_timestamp)
        history(int(package_id), timestamp)
        is_active = input("\nWould you like to lookup another package (Y/N)? ")
