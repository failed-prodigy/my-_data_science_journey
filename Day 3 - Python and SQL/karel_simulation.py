
# Simulating Karel logic (not actual Karel syntax, for illustration)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
    if right_is_clear():
        turn_right()
