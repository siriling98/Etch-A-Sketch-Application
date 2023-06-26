from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    """Moves the turtle forward by 10 steps"""
    timmy.forward(10)


def move_backward():
    """Moves the turtle back by 10 steps"""
    timmy.back(10)


def move_counter_clockwise():
    """Move turtle in anti clockwise direction"""
    timmy.left(10)


def move_clockwise():
    """Moves turtle in clockwise direction"""
    timmy.right(10)


screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_counter_clockwise, "a")
screen.onkeypress(move_clockwise, "d")
screen.onkeypress(timmy.reset, "z")
screen.exitonclick()

