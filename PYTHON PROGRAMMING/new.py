import turtle
def draw_rhombus (turtle):
    for i in range (4):
        turtle.forward(100)
        turtle.left(45)
        turtle.forward(100)
        turtle.left(135)

def draw_art():
    window=turtle.screen()
    window.bgcolor("yellow")

    bob =turtle.Turtle()
    bob.shape("turtle")
    bob.color("green")
    bob.pensize(5)
    bob.speed(100)
    for i in range(36):
        draw_rhombus(bob)
        bob.left(10)
draw_art()       