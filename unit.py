from tkinter import *
from switch import *


class unit(object):
    
    def __init__(self,number,canvas,conveyor,thickness,destination_switch):
        self.conveyor = conveyor
        self.conveyor_number = self.conveyor.number
        self.number = number
        self.canvas = canvas
        self.xStartPos = self.conveyor.xStartPos       
        self.yStartPos = self.conveyor.yStartPos        
        self.xVelocity = self.conveyor.xVelocity        
        self.yVelocity = self.conveyor.yVelocity    
        self.color = self.conveyor.color 
        self.thickness = thickness   
        self.image = canvas.create_rectangle(self.xStartPos,self.yStartPos,self.xStartPos+self.thickness,self.yStartPos+self.thickness,fill=self.color)
        self.destination_switch = destination_switch
        self.coordinates = self.canvas.coords(self.image)
        self.needs_to_switch = FALSE
        self.was_switched = FALSE
    
    
    def get_info_of_conveyor(self, conveyor):
        self.conveyor = conveyor
        self.conveyor_number = self.conveyor.number
        #self.xStartPos = self.conveyor.xStartPos       
        #self.yStartPos = self.conveyor.yStartPos        
        self.xVelocity = self.conveyor.xVelocity        
        self.yVelocity = self.conveyor.yVelocity    
        self.color = self.conveyor.color
        self.image
        
        
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
        self.canvas.move(self.image,0,-self.yVelocity)
        
    
    def move_down(self):
        self.coordinates = self.canvas.coords(self.image)
        self.check_collision_wall()
        self.canvas.move(self.image,0,self.yVelocity)
        
        