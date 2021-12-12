from tkinter import *
from conveyor import conveyor

class stopper(object):
    def __init__(self,number,canvas,xStartPos,yStartPos,length,width,color):
        self.number = number
        self.canvas = canvas
        self.image = canvas.create_rectangle(xStartPos,yStartPos,xStartPos+length,yStartPos+width,fill=color)
        self.color = color
        self.coordinates = self.canvas.coords(self.image)
        self.actived = False
        
        
    def active(self):
        self.canvas.move(self.image,1000,0)
        self.actived = True
        self.coordinates = self.canvas.coords(self.image)
        