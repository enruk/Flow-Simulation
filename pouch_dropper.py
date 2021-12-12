from tkinter import *
from pouch import *



class dropper:

    def drop(self,number,canvas,xStartPos,yStartPos,thickness,xVelocity,yVelocity):
        PouchX = pouch(number,canvas,xStartPos,yStartPos,thickness,xVelocity,yVelocity,"Red")
        return PouchX


