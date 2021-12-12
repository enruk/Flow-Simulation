from tkinter import *
from conveyor import conveyor

class pouch(object):
    
    def __init__(self,number,canvas,xStartPos,yStartPos,thickness,xVelocity,yVelocity,color):
        self.conveyor = conveyor
        self.number = number
        self.canvas = canvas
        self.image = canvas.create_rectangle(xStartPos,yStartPos,xStartPos+thickness,yStartPos+thickness,fill="red")
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.color = color
        self.coordinates = self.canvas.coords(self.image)


    def check_collision_wall(self):
        self.coordinates = self.canvas.coords(self.image)
        if(self.coordinates[2]>=(self.canvas.winfo_width()) or self.coordinates[0]<0):
            self.xVelocity = 0

        if(self.coordinates[3]>=(self.canvas.winfo_height()) or self.coordinates[1]<0):
            self.yVelocity = 0
            
            
    def move_right(self):
        self.coordinates = self.canvas.coords(self.image)
        self.check_collision_wall()
        
        
        self.canvas.move(self.image,self.xVelocity,0)
        
        
    def move_left(self):
        self.coordinates = self.canvas.coords(self.image)
        self.check_collision_wall()
        
        self.canvas.move(self.image,-self.xVelocity,0)
    
    
    def move_up(self):
        self.coordinates = self.canvas.coords(self.image)
        self.check_collision_wall()

        self.canvas.move(self.image,0,self.yVelocity)
        
    
    def move_down(self):
        self.coordinates = self.canvas.coords(self.image)
        self.check_collision_wall()

        self.canvas.move(self.image,0,-self.yVelocity)
        
        