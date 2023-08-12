# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def left_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
i = 0
for i in range(0,6):
    jump()    


#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def left_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    jump()


#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def left_square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
   
    
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()




#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while front_is_clear(): 
    move()
turn_left()
while not at_goal():

    if right_is_clear():
            turn_right()
            move()   
    elif front_is_clear():
        move()
    else:
        turn_left()