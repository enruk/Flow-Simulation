from tkinter import *
import random
import pouch
import stopper

class conveyor(object):
    def __init__(self,canvas,xStartPos,yStartPos,thickness,xVelocity,yVelocity,totalPouches,color,stopper) -> None:
        self.pouches = []

        self.xStartPos = xStartPos
        self.yStartPos = yStartPos
        self.thickness = thickness
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.totalPouches = totalPouches
        self.color = color
        self.stopper = stopper          # Needs to be a list

        for i in range(totalPouches):
            self.pouches.append(pouch(i,canvas,xStartPos,yStartPos+i*100,thickness,xVelocity,yVelocity,color))

    
    def check_collision_right(self,pouch_number):
        #i = len(self.pouches)
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            
            if (self.pouches[pouch_number-1].coordinates[0] - self.pouches[pouch_number].coordinates[2]<12 or self.stopper.coordinates[0] - self.pouches[pouch_number].coordinates[2]<30):
                print('Hello')
                self.pouches[pouch_number].xVelocity = 0
                self.pouches[pouch_number].yVelocity = 0
            
            else:
                print('Moin')
                self.pouches[pouch_number].xVelocity = self.xVelocity
                self.pouches[pouch_number].yVelocity = self.yVelocity
                
                
                
    def check_collision_left(self,pouch_number):
        #i = len(self.pouches)
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (abs(self.pouches[pouch_number-1].coordinates[2] - self.pouches[pouch_number].coordinates[0])<12 or abs(self.stopper.coordinates[2] - self.pouches[pouch_number].coordinates[0])<30):
                self.pouches[pouch_number].xVelocity = 0
                self.pouches[pouch_number].yVelocity = 0
              
            else:
                self.pouches[pouch_number].xVelocity = self.xVelocity
                self.pouches[pouch_number].yVelocity = self.yVelocity
                
                
                
    def check_collision_up(self,pouch_number):
        #i = len(self.pouches)
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (abs(self.pouches[pouch_number-1].coordinates[3] - self.pouches[pouch_number].coordinates[1])<12 or abs(self.stopper.coordinates[3] - self.pouches[pouch_number].coordinates[1])<30):
                self.pouches[pouch_number].xVelocity = 0
                self.pouches[pouch_number].yVelocity = 0
              
            else:
                self.pouches[pouch_number].xVelocity = self.xVelocity
                self.pouches[pouch_number].yVelocity = self.yVelocity
    
    
    
    def check_collision_down(self,pouch_number):
        #i = len(self.pouches)
        if pouch_number > 0:
            # After moving, check if collision with pouch in front
            
            if (abs(self.pouches[pouch_number-1].coordinates[1] - self.pouches[pouch_number].coordinates[3])<12 or abs(self.stopper.coordinates[1] - self.pouches[pouch_number].coordinates[3])<30):
                self.pouches[pouch_number].xVelocity = 0
                self.pouches[pouch_number].yVelocity = 0
              
            else:
                self.pouches[pouch_number].xVelocity = self.xVelocity
                self.pouches[pouch_number].yVelocity = self.yVelocity