import tkinter as tk
from tkinter import Canvas
from time import *
from conveyor import conveyor
from unit import *
from stopper import stopper


root = tk.Tk()
root.geometry("1400x1400")

WIDTH = 1200
HEIGHT = 1200
canvas=Canvas(root,width=WIDTH,height=HEIGHT,bg="White")
canvas.pack(pady=200)

Stopper1 = stopper(1,canvas,600,600,50,50,"White") 


total_units = 0
PaF1 = conveyor(canvas,0,600,8,3,3,total_units,"Red",Stopper1)
Gravity = conveyor(canvas,500,500,8,2,2,total_units,"Green",Stopper1)


num = 0
starttime = time()
mark1 = time()
max_units = 10


while root.mainloop:
    
    #Wait a second
    sleep(0.01)
    
    

    processtime = time() - starttime
    if processtime > 1 and num < max_units:
        starttime = time()
        
        num = num + 1
        
        #Create new Pouch on PaF
        unitX = unit(num,canvas,PaF1,8,"Red")
        PaF1.units.append(unitX)
        
        #Create new Pouch on Gravity
        unitY = unit(num,canvas,Gravity,8,"Green")
        Gravity.units.append(unitY)


    # Stoppper
    if time()-mark1 > 10:
        Stopper1.active()

    
    #Tell all pouches in this conveyor to move
    for i in range(len(PaF1.units)):
        PaF1.units[i].move_right()
        PaF1.check_collision_right(i)
        
        
        #if i > 0:
            # After moving, check if collision with pouch in front
            
            #if (PaF1.pouches[i-1].coordinates[0] - PaF1.pouches[i].coordinates[2]<12 or Stopper1.coordinates[0] - PaF1.pouches[i].coordinates[2]<30):
                #PaF1.pouches[i].xVelocity = 0
                #PaF1.pouches[i].yVelocity = 0
              
            #else:
                #PaF1.pouches[i].xVelocity = pouchX.xVelocity
                #PaF1.pouches[i].yVelocity = pouchX.yVelocity
                
            # After moving, check if pouches were moved to an other conveyor
    
    
    for i in range(len(Gravity.units)):
        Gravity.units[i].move_up()
        Gravity.check_collision_up(i)
        
        #if i > 0:
            # After moving, check if collision with pouch in front
            
            #if (Gravity.pouches[i-1].coordinates[0] - Gravity.pouches[i].coordinates[2]<12 or Stopper1.coordinates[0] - Gravity.pouches[i].coordinates[2]<30):
                #Gravity.pouches[i].xVelocity = 0
                #Gravity.pouches[i].yVelocity = 0
              
            #else:
                #Gravity.pouches[i].xVelocity = pouchY.xVelocity
                #Gravity.pouches[i].yVelocity = pouchY.yVelocity
                
            # After moving, check if pouches were moved to an other conveyor
    
                   
    root.update()

root.mainloop()

    




