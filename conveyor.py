from tkinter import *
import random
from tokenize import Number
from unit import *
from stopper import *
import switch

class conveyor(object):
    def __init__(self,canvas,number,xStartPos,yStartPos,thickness,xVelocity,yVelocity,totalPouches,color,switches,stopper):
        self.number = number
        self.units = []
        self.xStartPos = xStartPos
        self.yStartPos = yStartPos
        self.thickness = thickness
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.totalPouches = totalPouches
        self.color = color         # Needs to be a list
        self.switches = switches
        self.stopper = stopper
        for i in range(totalPouches):
            self.units.append(unit(i,canvas,self,thickness,color))

    
    def check_collision_right(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with: next unit in the list, stopper or switch
            
            if (self.stopper!= 0):     
                if (self.units[pouch_number-1].coordinates[0] - self.units[pouch_number].coordinates[2]<30 or self.stopper.coordinates[0] - self.units[pouch_number].coordinates[2]<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
                    
            else:
                if (self.units[pouch_number-1].coordinates[0] - self.units[pouch_number].coordinates[2]<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
                
                
                
    def check_collision_left(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (self.stopper!= 0): 
                if (abs(self.units[pouch_number-1].coordinates[2] - self.units[pouch_number].coordinates[0])<30 or abs(self.stopper.coordinates[2] - self.units[pouch_number].coordinates[0])<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
            else:
                if (abs(self.units[pouch_number-1].coordinates[2] - self.units[pouch_number].coordinates[0])<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
                
                
                
    def check_collision_up(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (self.stopper!= 0):
                if (abs(self.units[pouch_number-1].coordinates[3] - self.units[pouch_number].coordinates[1])<30 or abs(self.stopper.coordinates[3] - self.units[pouch_number].coordinates[1])<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
            else:
                if (abs(self.units[pouch_number-1].coordinates[3] - self.units[pouch_number].coordinates[1])<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
    
    
    
    def check_collision_down(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (self.stopper!= 0):
                if (abs(self.units[pouch_number-1].coordinates[1] - self.units[pouch_number].coordinates[3])<30 or abs(self.stopper.coordinates[1] - self.units[pouch_number].coordinates[3])<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
            else:
                if (abs(self.units[pouch_number-1].coordinates[1] - self.units[pouch_number].coordinates[3])<30):
                    self.units[pouch_number].xVelocity = 0
                    self.units[pouch_number].yVelocity = 0
                
                else:
                    self.units[pouch_number].xVelocity = self.xVelocity
                    self.units[pouch_number].yVelocity = self.yVelocity
                
      
    def check_unit_at_switch(self,pouch_number):
        divert_switch = self.units[pouch_number].destination_switch
        if abs(self.units[pouch_number].coordinates[2] - self.switches[divert_switch].coordinates[2])<30:
            self.units[pouch_number].needs_to_switch = TRUE
            print('Unit needs to switch')