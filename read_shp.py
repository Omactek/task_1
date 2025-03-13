import geopandas as gpd

data_path = r"data\ku_zizinikov\PARCELY_KN_P.shp"

data = gpd.read_file(data_path)

print(data.get_geometry(0)[0])