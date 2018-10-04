import turtle

def main():
    alex = turtle.Turtle()
    bob = turtle.Turtle()
    christine = turtle.Turtle()

    # customize the turtles
    alex.pensize(1)
    bob.pensize(1)
    christine.pensize(1)
    alex.pencolor("red")
    bob.pencolor("green")
    christine.pencolor("blue")

    sides = int(input("Number of sides? "))
    size = int(input("Size of polygon? "))

    # space the turtles
    alex.backward(size*6)
    bob.forward(0)
    christine.forward(size*6)

    for t in (alex, bob, christine):
        drawPolygon(t, sides, size)

    #drawPolygon (alex, sides, size)
    #drawPolygon (bob, sides, size)
    #drawPolygon (christine, sides, size)

def drawPolygon (t, sides, size):
    """uses turtles to draw a n sided polygon
        input: t - a turtle
                  sides - number of sides
                  size - length of one side
    """
    for side in range(sides):
        t.forward(size)
        t.right(360/sides) # angle depends on polygon
        
# run program
main()
