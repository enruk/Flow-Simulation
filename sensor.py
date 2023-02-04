from tkinter import *

class sensor(object):
    def __init__(self,number,canvas,xPos,yPos,length,width,orientation,color):
        self.number = number
        self.canvas = canvas
        self.image = canvas.create_rectangle(xPos,yPos,xPos+length,yPos+width,fill=color)
        self.color = color
        self.coordinates = self.canvas.coords(self.image)
        self.orientation = orientation
        
    
    
        
        
        
