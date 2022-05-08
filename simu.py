import tkinter as tk
from tkinter import Canvas
from time import *
from conveyor import conveyor
from unit import *
from stopper import stopper
import copy


root = tk.Tk()
root.geometry("1400x1400")

WIDTH = 1500
HEIGHT = 1200
canvas=Canvas(root,width=WIDTH,height=HEIGHT,bg="White")
canvas.pack(pady=200)

Stopper1 = stopper(1,canvas,600,600,50,50,"White") 


switch1 = switch(1,canvas,500,600,50,50,"Black")
switch2 = switch(2,canvas,700,600,50,50,"Black")
switch3 = switch(3,canvas,900,600,50,50,"Black")
switch4 = switch(4,canvas,1100,600,50,50,"Black")
switch5 = switch(5,canvas,1300,600,50,50,"Black")
switches = [switch1, switch2, switch3, switch4, switch5]

total_units = 0
red_conveyor = conveyor(canvas,1,10,600,8,5,5,total_units,"Red",switches,Stopper1)



green_conveyor1 = conveyor(canvas,1,500,500,8,2,2,total_units,"Green",0,0)
green_conveyor2 = conveyor(canvas,2,700,500,8,2,2,total_units,"Green",0,0)
green_conveyor3 = conveyor(canvas,3,900,500,8,2,2,total_units,"Green",0,0)
green_conveyor4 = conveyor(canvas,4,1100,500,8,2,2,total_units,"Green",0,0)
green_conveyor5 = conveyor(canvas,5,1300,500,8,2,2,total_units,"Green",0,0)
green_conveyors = [green_conveyor1, green_conveyor2, green_conveyor3, green_conveyor4, green_conveyor5]


num = 0

starttime = time()
mark1 = time()
max_units = 2
temp_array = []


while root.mainloop:
    
    #Wait a second
    sleep(0.05)
    
    

    processtime = time() - starttime
    if processtime > 5 and num < max_units:
        starttime = time()
        
        num = num + 1
        
        # Random destination
        destination_switch=random.randrange(1,5,1)
        
        #Create new Unit 
        unitX = unit(num,canvas,red_conveyor,8,destination_switch)
        red_conveyor.units.append(unitX)
        
        #Create new Pouch on Gravity
        #unitY = unit(num,canvas,green_conveyor,8)
        #green_conveyor.units.append(unitY)


    #Stoppper
    if time()-mark1 > 10:
        Stopper1.active()


    if len(red_conveyor.units)>0:
        for i in range(len(red_conveyor.units)):
            red_conveyor.units[i].move_right()
            red_conveyor.check_collision_right(i)
            red_conveyor.check_unit_at_switch(i)
            
            #if i > 0:
                # After moving, check if collision with pouch in front
                
                #if (PaF1.pouches[i-1].coordinates[0] - PaF1.pouches[i].coordinates[2]<12 or Stopper1.coordinates[0] - PaF1.pouches[i].coordinates[2]<30):
                    #PaF1.pouches[i].xVelocity = 0
                    #PaF1.pouches[i].yVelocity = 0
                
                #else:
                    #PaF1.pouches[i].xVelocity = pouchX.xVelocity
                    #PaF1.pouches[i].yVelocity = pouchX.yVelocity
                    
    for i in range(len(green_conveyors)):
        if len(green_conveyors[i].units)>0:
            print(len(green_conveyors[i].units))
            for i in range(len(green_conveyors[i].units)):
                canvas.itemconfig(green_conveyors[i].units[i],fill = green_conveyors[i].color)
                green_conveyors[i].units[i].move_up()
                print(green_conveyors[i].units[i].color)
                green_conveyors[i].check_collision_up(i)
                
                #if i > 0:
                    # After moving, check if collision with pouch in front
                    
                    #if (Gravity.pouches[i-1].coordinates[0] - Gravity.pouches[i].coordinates[2]<12 or Stopper1.coordinates[0] - Gravity.pouches[i].coordinates[2]<30):
                        #Gravity.pouches[i].xVelocity = 0
                        #Gravity.pouches[i].yVelocity = 0
                    
                    #else:
                        #Gravity.pouches[i].xVelocity = pouchY.xVelocity
                        #Gravity.pouches[i].yVelocity = pouchY.yVelocity


    # After moving all units, check if some units need to switch the conveyor         
    for i in range(len(red_conveyor.units)):
        # if yes, move the unit to the new conveyor 
        if red_conveyor.units[i].needs_to_switch == TRUE:
            destination = red_conveyor.units[i].destination_switch
            for i in range (len(green_conveyors)):
                if green_conveyors[i].number == destination:
                    destination_conveyor = i
            green_conveyors[destination_conveyor].units.append(red_conveyor.units[i])
            green_conveyors[destination_conveyor].units[-1].get_info_of_conveyor(green_conveyor1)
            #del green_conveyor.units[-1]

            
    
    
    # After moving to other conveyor, remove from old conveyor
    
    #del temp_array[:]
    #row_temp_conveyor = 0
    for i in range(len(red_conveyor.units)-1,-1,-1):
        # Make a temporary array and copy it back after getting all units that still on the conveyor
        if red_conveyor.units[i].needs_to_switch == TRUE:
            del red_conveyor.units[i]
            print("Item gelöscht"+str(i))
            #temp_array.append(red_conveyor.units[i])
            #row_temp_conveyor += 1
    #del red_conveyor.units[:]
    #red_conveyor.units = copy.deepcopy(temp_array)
    
                   
    root.update()

root.mainloop()

    




