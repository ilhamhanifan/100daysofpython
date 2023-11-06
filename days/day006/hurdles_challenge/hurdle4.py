def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    jump_height = 0
    turn_left()
    while not right_is_clear():
        jump_height += 1
        move()
    turn_right()
    move()
    turn_right()
    for x in range(jump_height):
        move()
    turn_left()
 
play = True
while play:
    if at_goal():
        play = False
        continue
    elif wall_in_front():
        jump()
    elif front_is_clear() :
        move()
        
        
