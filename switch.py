from tkinter import *
import random
import unit
from conveyor import *

class switch(object):
    def __init__(self,number,canvas,xStartPos,yStartPos,length,width,color):
        self.number = number
        self.canvas = canvas
        self.image = canvas.create_rectangle(xStartPos,yStartPos,xStartPos+length,yStartPos+width,fill=color)
        self.color = color
        self.coordinates = self.canvas.coords(self.image)
        self.actived = False
        
        
    
        