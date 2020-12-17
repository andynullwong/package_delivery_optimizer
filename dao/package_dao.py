from main import root_path
from util.csv_reader import parse_cvs

package_hashmap = parse_cvs(root_path+'/data/wgups_package_file.csv')

print(package_hashmap.get(1))  # 195 W Oakland Ave
