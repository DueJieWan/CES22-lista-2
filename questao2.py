import turtle  # Tess becomes a traffic light.
turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

# Tess' pen thiccness
thiccness = 3

def draw_housing():

    global thiccness
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(thiccness)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()



draw_housing()
    
tess.penup()
    
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(thiccness)
tess.fillcolor("green")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red. We number these states 0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():


    global state_num
    if state_num == 0:  # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("blue")
        state_num = 1
    elif state_num == 1:  # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:  # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    
    wn.ontimer(advance_state_machine, 100)

advance_state_machine()

wn.listen()  # Listen for events
wn.mainloop()
