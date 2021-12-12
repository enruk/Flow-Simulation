import tkinter as tk
from tkinter import Canvas
from time import *
from conveyor import conveyor
from pouch import *
from pouch_dropper import dropper
from stopper import stopper


root = tk.Tk()
root.geometry("1400x1400")

WIDTH = 1200
HEIGHT = 1200
canvas=Canvas(root,width=WIDTH,height=HEIGHT,bg="White")
canvas.pack(pady=200)

totalpouches = 0
PaF1 = conveyor(1,canvas,0,600,8,20,0,totalpouches)

num = 0
starttime = time()
mark1 = time()

Stopper1 = stopper(1,canvas,600,200,50,50,"White") 

while root.mainloop:
    
    #Wait a second
    sleep(0.01)
    

    processtime = time() - starttime
    if processtime > 0.3:
        starttime = time()
        
        #Create new Pouch
        num = num + 1
        pouchX = pouch(num,canvas,0,200,8,3,0,"Red")
        PaF1.pouches.append(pouchX)

    if time()-mark1 > 10:
        Stopper1.active()

    
    #Tell all pouches to move
    for i in range(len(PaF1.pouches)):
        PaF1.pouches[i].move_right()
        pouchMovingStatus =  True
        
        if i > 0:
            # After moving, check if collision with pouch in front
            
            if (PaF1.pouches[i-1].coordinates[0] - PaF1.pouches[i].coordinates[2]<12 or Stopper1.coordinates[0] - PaF1.pouches[i].coordinates[2]<30):
                PaF1.pouches[i].xVelocity = 0
                PaF1.pouches[i].yVelocity = 0
              
            else:
                PaF1.pouches[i].xVelocity = pouchX.xVelocity
                PaF1.pouches[i].yVelocity = pouchX.yVelocity
                   
    root.update()

root.mainloop()

    




