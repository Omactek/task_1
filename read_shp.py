import geopandas as gpd
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

data_path = r"data\ku_zizinikov\PARCELY_KN_P.shp"

data = gpd.read_file(data_path)

qpolygons_list = []

#iterate through polygons in data, creating QPolygonFs
for i in range(0,len(data)):
    polygon = data.get_geometry(0)[i]
    print(data.get_geometry(0)[i])
    
    q_polygon = QPolygonF()
    
    #iterate throught bounding points of a polygon, saving them in QPolygonF
    for x,y in polygon.exterior.coords:
        print(x, y)
        point = QPointF(x, y)
        q_polygon.append(point)
    qpolygons_list.append(q_polygon)    #append created polygon to the list of polygons
        
        
    
    