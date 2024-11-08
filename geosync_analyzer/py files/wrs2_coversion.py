import sys
import json
import geopandas as gpd
from shapely.geometry import Point


wrs2_shapefile_d = 'py files/WRS2_descending_0'
wrs2_d = gpd.read_file(wrs2_shapefile_d)

wrs_shape_file_a = 'py files/WRS2_ascending_0'
wrs2_a = gpd.read_file(wrs_shape_file_a)

def latlong_to_wrs2_path_row_d(latitude, longitude):
    point = Point(longitude, latitude)
    
    for _, row in wrs2_d.iterrows():
        if row['geometry'].contains(point):
            path = row['PATH']
            row_number = row['ROW']
            return path, row_number
    
    return None, None  


def latlong_to_wrs2_path_row_a(latitude, longitude):
    point = Point(longitude, latitude)
    
    
    for _, row in wrs2_a.iterrows():
        if row['geometry'].contains(point):
            path = row['PATH']
            row_number = row['ROW']
            return path, row_number
    
    return None, None  



    
if __name__ == "__main__":
    latitude = float(sys.argv[1])
    longitude = float(sys.argv[2])
    path_d, row_d = latlong_to_wrs2_path_row_d(latitude, longitude)
    path_a,row_a=latlong_to_wrs2_path_row_a(latitude, longitude)

    result = {
        "ascending": {"path": path_a, "row": row_a},
        "descending": {"path": path_d, "row": row_d}
    }

    print(json.dumps(result))