import geopandas as gpd
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

def load_shapefile(data_path):
    data = gpd.read_file(data_path)

    qpolygons_list = []

    #finding min and max coordinates (for drawing)
    min_x, min_y, max_x, max_y = data.total_bounds
    #iterate through polygons in data, creating QPolygonFs
    for i in range(0,len(data)):
        polygon = data.get_geometry(0)[i]
        
        q_polygon = QPolygonF()
        
        #iterate throught bounding points of a polygon, saving them in QPolygonF, 
        # rescaling the coordinates to make the polygons visible in the canvas
        for x,y in polygon.exterior.coords:
            x = (x - min_x) * 0.1
            y = (max_y - y) * 0.1
            point = QPointF(x, y)
            q_polygon.append(point)
        qpolygons_list.append(q_polygon)    #append created polygon to the list of polygons
    
    return qpolygons_list
        
        
    
    