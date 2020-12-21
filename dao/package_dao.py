import math

from dao.hub_dao import get_distance_to_hub
from env import root_path, default_hub
from model.clock import clock
from model.package import Package
from util.csv_reader import reverse_parse_cvs, parse_package_file

package_id_address_map = parse_package_file()
package_address_id_map = reverse_parse_cvs(root_path + '/data/wgups_package_file.csv')


def get_nearest_package(current_hub, van_payload):
    next_hub_name = None
    next_hub_distance = math.inf

    if len(van_payload) > 0:
        for package in van_payload:
            package_hub = package.get_hub_name()
            destination_distance = get_distance_to_hub(current_hub, package_hub)
            if destination_distance < next_hub_distance:
                next_hub_name = package_hub
                next_hub_distance = destination_distance
        return next_hub_name, next_hub_distance
    else:
        default_distance = get_distance_to_hub(current_hub, default_hub)
        return default_hub, default_distance


def load_packages_in_van(van_id, van, package_list: list[int]):
    van_loaded = [False, False, False]

    def load():
        if not van_loaded[van_id - 1]:
            for package_id in package_list:
                package_address = package_id_address_map.get(package_id)
                package = Package(package_id, package_address)
                package.set_enroute(clock.get_time())
                van.add(package)
            van_loaded[van_id - 1] = True

    return load
