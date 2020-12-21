from model.hash_map import HashMap
from model.package import Package

package_history = HashMap()


def add(package_id, package: Package):
    package_history.add(package_id, package)


def get(package_id) -> Package:
    return package_history.get(package_id)


def history(package_id, timestamp):
    package = get(package_id)
    print("Package ID:", package.get_id())
    print("Package Address:", package.get_address())
    print("Package Deadline:", package.get_deadline())
    print("Package Zipcode:", package.get_zipcode())
    print("Package Weight:", package.get_weight())
    print("Package Status", package.get_status(timestamp))
