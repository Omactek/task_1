from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtGui import QMouseEvent, QPaintEvent
from PyQt6.QtWidgets import *

class Draw(QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__q = QPointF(0.0, 0.0)
        self.__pol = QPolygonF()
        self.__polygons = []
        self.__add_vertex = False
        self.highlighted_pol = None

    def mousePressEvent(self, e:QMouseEvent):
        
        #Get coordinates x,y
        x = e.position().x()
        y = e.position().y()
        
        #Add polygon vertex
        if self.__add_vertex:
            
            #Create new point
            p = QPointF(x, y)
        
            #Add to point to polygon
            self.__pol.append(p)
        
        #Change q coordinates
        else:
            self.__q.setX(x)
            self.__q.setY(y)
        self.repaint()
 
 
    def paintEvent(self, e: QPaintEvent):
        #Create new graphic object
        qp = QPainter(self)
      
        #Set graphic attributes, polygon
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.yellow)
        
        #Draw polygons
        for pol in self.__polygons:
            if pol == self.highlighted_pol:
                qp.setBrush(QColor(0, 255, 0, 128))
            else:
                qp.setBrush(Qt.GlobalColor.yellow)
        
            qp.setPen(Qt.GlobalColor.black)
            qp.drawPolygon(pol)
        
        #Set graphic attributes, point
        qp.setPen(Qt.GlobalColor.black)
        qp.setBrush(Qt.GlobalColor.red)
        #draw point
        r = 10
        qp.drawEllipse(int(self.__q.x()-r), int(self.__q.y()-r), 2*r, 2*r)
        
        
    def paintInputEvent(self, polygons):
        self.__polygons = polygons
        
    def switchInput(self):
        #Input point or polygon vertex
        self.__add_vertex = not (self.__add_vertex)
    
    def getQ(self):
        #Get point
        return self.__q
    
    def getPol(self):
        #Get polygon
        return self.__pol
    
    def getPolygons(self):
        return self.__polygons
    
    def highlightPolygon(self, pol):
        self.highlighted_pol = pol
        self.repaint()

    def clearData(self):
        self.__q = QPointF(0.0, 0.0)
        self.__pol = QPolygonF()
        self.__polygons = []
        self.__add_vertex = False
        self.highlighted_pol = None
        self.repaint()