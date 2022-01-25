from tkinter import *
import random
import unit
import stopper

class conveyor(object):
    def __init__(self,canvas,xStartPos,yStartPos,thickness,xVelocity,yVelocity,totalPouches,color,stopper):
        self.units = []
        self.xStartPos = xStartPos
        self.yStartPos = yStartPos
        self.thickness = thickness
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.totalPouches = totalPouches
        self.color = color
        self.stopper = stopper          # Needs to be a list

        for i in range(totalPouches):
            self.units.append(unit(i,canvas,xStartPos,yStartPos+i*100,thickness,xVelocity,yVelocity,color))

    
    def check_collision_right(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with: next unit in the list, stopper or switch
                        
            
            if (self.units[pouch_number-1].coordinates[0] - self.units[pouch_number].coordinates[2]<12 or self.stopper.coordinates[0] - self.units[pouch_number].coordinates[2]<30):
                print('Hello')
                self.units[pouch_number].xVelocity = 0
                self.units[pouch_number].yVelocity = 0
            
            else:
                print('Moin')
                self.units[pouch_number].xVelocity = self.xVelocity
                self.units[pouch_number].yVelocity = self.yVelocity
                
                
                
    def check_collision_left(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (abs(self.units[pouch_number-1].coordinates[2] - self.units[pouch_number].coordinates[0])<12 or abs(self.stopper.coordinates[2] - self.units[pouch_number].coordinates[0])<30):
                self.units[pouch_number].xVelocity = 0
                self.units[pouch_number].yVelocity = 0
              
            else:
                self.units[pouch_number].xVelocity = self.xVelocity
                self.units[pouch_number].yVelocity = self.yVelocity
                
                
                
    def check_collision_up(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (abs(self.units[pouch_number-1].coordinates[3] - self.units[pouch_number].coordinates[1])<12 or abs(self.stopper.coordinates[3] - self.units[pouch_number].coordinates[1])<30):
                self.units[pouch_number].xVelocity = 0
                self.units[pouch_number].yVelocity = 0
              
            else:
                self.units[pouch_number].xVelocity = self.xVelocity
                self.units[pouch_number].yVelocity = self.yVelocity
    
    
    
    def check_collision_down(self,pouch_number):
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (abs(self.units[pouch_number-1].coordinates[1] - self.units[pouch_number].coordinates[3])<12 or abs(self.stopper.coordinates[1] - self.units[pouch_number].coordinates[3])<30):
                self.units[pouch_number].xVelocity = 0
                self.units[pouch_number].yVelocity = 0
              
            else:
                self.units[pouch_number].xVelocity = self.xVelocity
                self.units[pouch_number].yVelocity = self.yVelocity