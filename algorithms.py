from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from math import sqrt, acos, pi

class Algorithms:
    def __init__(self):
        pass
    
    def ray_crossing(self, q: QPointF, pol: QPolygonF):
        # analyze point and polygon position using ray crossing algorithm
        k = 0 #amount of intersection points
        n = len(pol)
        for i in range(n): #process all points
            
            #Get i-th point
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            
            #Get (i+1)st point
            xi1r = pol[(i+1)%n].x() - q.x()
            yi1r = pol[(i+1)%n].y() - q.y()
            
            #Test criterion
            if (yi1r > 0) and (yir <= 0) or (yi1r <= 0) and (yir > 0):
                # We found a suitable segment, now we compute intersection
                xm = (xi1r*yir - xir*yi1r)/(yi1r-yir)
                
                if xm > 0:
                    # if m is in the right half-plane; increase number of k 
                    k = k + 1
        return True if k%2 == 1 else False
    
    def winding_number(self, q: QPointF, polygon: QPolygonF):
        """
        #  init cumulative angle measure to 0 (Ω)
        # set tolerance value (small number - allow point approximation)

        # loop over subsequent pairs points (pi, pi+1...)
        # for each consecutive pair of points (pi, pi+1) in a polygon, and a point q we want to test:

            # determine the position of q
            # check where the point q is located relative to the line segment formed by pi and pi+1

            # calculate the angle of wi
            # measure the angle formed by the points pi, q, pi+1 (the turn or rotation from pi to pi+1 around q)

            # update Ω based on which side q is located
            # if q is on the left side of the line segment (pi, pi+1), add ωi to Ω
            # if q is on the right side of the line segment, subtract ωi from Ω

        # check if Ω is approximately 2π or -2π
            # if the absolute difference between |Ω| and 2π is less than ε (meaning the angle sum is nearly 2π), then q is inside the polygon (P).
            # otherwise, q is outside the polygon (P).
        """
        cum_angle_meas = 0
        tolerance = 0.01

        for i in range(len(polygon)):
            point1 = polygon[i]
            point2 = polygon[(i + 1) % len(polygon)]  # to acces the first point as the last one

            vector1 = [point1.x() - q.x(), point1.y() - q.y()]
            vector2 = [point2.x() - q.x(), point2.y() - q.y()]

            # A * B = ∥A∥∥B∥cos(θ) ==> cos(θ) = (A * B) / (∥A∥∥B∥)

            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]

            # normalize vectors
            norm1 = sqrt(vector1[0]**2 + vector1[1]**2)
            norm2 = sqrt(vector2[0]**2 + vector2[1]**2)
            angle = acos(round(dot_product / (norm1 * norm2), 10)) # get rid of small inaccuracies caused by floaters

            cross_product = (point2.x() - point1.x()) * (q.y() - point1.y()) - (point2.y() - point1.y()) * (q.x() - point1.x())
        

            if cross_product > 0: # point on the left side
                cum_angle_meas += angle
            elif cross_product <= 0:
                cum_angle_meas -= angle
            # else: if the cross_product is zero it should be on line?

        if abs(cum_angle_meas - 2 * pi) < tolerance:
            return True

        return False
    
    def minmaxbox(self, pol: QPolygonF):
        #creates minmax box of a polygon using its min and max coordinates
        mmb = QPolygonF()

        #findVertices
        x_min = min(pol, key = lambda k: k.x()).x()
        x_max = max(pol, key = lambda k: k.x()).x()

        y_min = min(pol, key = lambda k: k.y()).y()
        y_max = max(pol, key = lambda k: k.y()).y()

        v0 = QPointF(x_min, y_min)
        v1 = QPointF(x_max, y_min)
        v2 = QPointF(x_max, y_max)
        v3 = QPointF(x_min, y_max)

        mmb.append(v0)
        mmb.append(v1)
        mmb.append(v2)
        mmb.append(v3)
        
        return mmb
    
    def point_inside_minmaxbox(self, q: QPointF, mmb: QPolygonF):
        """
        #  Tests if a point is inside minmaxbox polygon using its min and max coordinates
        #  Returns True (inside) or False (outside)
        """
        if q.x() >= mmb[0].x() and q.x() <= mmb[2].x() and q.y() >= mmb[0].y() and q.y() <= mmb[2].y():
            return True
        else:
            return False
        
    def select_suspicious_polygons(self, q: QPointF, list_of_polygons):
        """
        #  Tests if a point is inside minmaxbox of each polygon from given list of polygons using its min and max coordinates
        #  Returns list of polygons whose minmax boxes have the input point inside
        """
        suspicious_polygons = []
        #searching for potential polygons (testing if the point is inside the minmax box of each polygon)
        for pol in list_of_polygons:
            mmb = self.minmaxbox(pol)
            sus = self.point_inside_minmaxbox(q,mmb)
            if sus:
                suspicious_polygons.append(pol) #adds suspicious polygon to the list of suspicious polygons
        return suspicious_polygons