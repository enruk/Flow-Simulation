from pouch import *
from tkinter import *
import random

class conveyor(object):
    def __init__(self,canvas,xStartPos,yStartPos,thickness,xVelocity,yVelocity,totalPouches) -> None:
        self.pouches = []

        self.xStartPos = xStartPos
        self.yStartPos = yStartPos
        self.thickness = thickness
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.totalPouches = totalPouches

        for i in range(totalPouches):
            self.pouches.append(pouch(i,canvas,xStartPos,yStartPos+i*100,thickness,xVelocity,yVelocity,"Red"))
            

