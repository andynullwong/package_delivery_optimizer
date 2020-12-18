import math

from dao.hub_dao import get_distance_to_hub, id_hub_map
from env import root_path, default_hub
from util.csv_reader import parse_cvs, reverse_parse_cvs

package_id_address_map = parse_cvs(root_path + '/data/wgups_package_file.csv')
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
