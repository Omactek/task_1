from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from itertools import combinations 

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
        return k%2  #inside - returns 1, outside - returns 0
    
    def winding_number(self, q: QPointF, pol:QPolygonF):
        """
        #  init cumulative angle measure to 0 (Ω)
        # set tolerance value (small number - allow point approximation)

        # loop over all triplets of points (pi, q, pi+1)
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

        triplets = list(combinations(QPolygonF, 2), q)

        for trip in triplets:
            
            pass
        pass