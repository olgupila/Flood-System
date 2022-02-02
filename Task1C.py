from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

stations = build_station_list()
x = stations_within_radius(stations, (52.2053, 0.1218), 10)
b = []
for station in x:
    b.append(station.name)
b.sort()
print(b)

