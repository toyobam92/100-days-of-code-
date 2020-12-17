def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_jump():
    move()
    jump()

def move_left():
    move()
    turn_left()
    
    
def final():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

def hurdle():
    move_left()
    move_jump()
    move_jump()
    move_left()
    
while not at_goal():
    if wall_in_front():
      final()
    else:
        move()
    
#number_of_hurdles = 6 
#while number_of_hurdles > 0:
   # hurdle()
    #number_of_hurdles -=1
   # print(number_of_hurdles)
    
#for step in range(0,6):
   # hurdle()
    
#while not at_goal():
   # hurdle()
    #continue
    #if at_goal == True:
        #break

        
       # move()
       # turn_left()
      #  turn_left()
      #  turn_left()
       # move()
   
    #else:
     #   hurdle()
    
    
    
    
    
    
    
    


