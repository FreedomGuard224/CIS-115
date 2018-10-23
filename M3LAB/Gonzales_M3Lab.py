"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def main():
    """ I don't know what I'm doing"""
    
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.000001

    print("-----Menu-----".center(40))
    print(" Task 1: Turtle draws 2 cirlces, a square, and a triangle.")
    print(" Task 2: Turtle draws 3 different pies.")

    choice = input("Pick a task: ")
    
    if choice == "1":
        illuminati(bob)
    elif choice == "2":
        pu(bob)
        lt(bob,180)
        fd(bob,125)
        rt(bob,180)
        five_pie(bob)
        six_pie(bob)
        seven_pie(bob)
    
def illuminati(bob):
    # draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    pu(bob)
    lt(bob, 90)
    fd(bob, 100)

    radius = 50
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    pu(bob)
    lt(bob, 90)
    fd(bob, 150)
    lt(bob, 90)
    pd(bob)

    for i in range(4):
        fd(bob, 100)
        lt(bob,)
        fd(bob, 100)

    lt(bob, 60)
    for c in range(3):
        fd(bob, 180)
        lt(bob, 120)
    
    lt(bob, 210)

    wait_for_user()



def five_pie(bob):

    for x in range (5):  
        five_pie_algo(bob)


    lt(bob,54)
    fd(bob,40)

    lt(bob,34)
    fd(bob,45)

    lt(bob,128)
    fd(bob,50)

    lt(bob,124)
    fd(bob,42)

    lt(bob,40)
    fd(bob,43)

    rt(bob,180)
    fd(bob,43)

    lt(bob,108)
    fd(bob,42)

    pu(bob)
    fd(bob,50)

def five_pie_algo(bob):

    #outline for five pie
    pd(bob)
    fd(bob,50)
    lt(bob,72)

def six_pie(bob):
    lt(bob,80)
    fd(bob,110)
    
    for x in range (5):
        six_pie_algo(bob)
        lt(bob,60)
        fd(bob,50)

def six_pie_algo(bob):
    
    pd(bob)
    for x in range (3):
        lt(bob,120)
        fd(bob,50)

def seven_pie(bob):

    pu(bob)
    lt(bob,35)
    fd(bob,110)
    pd(bob)
    
    for x in range (7):
        seven_pie_algo(bob)

    fd(bob,3)

    lt(bob,65)
    fd(bob,60)

    lt(bob,28)
    fd(bob,56)
    rt(bob,180)
    fd(bob,56)

    lt(bob,20)
    fd(bob,60)
    rt(bob,180)
    fd(bob,60)

    lt(bob,32)
    fd(bob,60)
    rt(bob,180)
    fd(bob,60)

    lt(bob,23)
    fd(bob,55)
    rt(bob,180)
    fd(bob,55)

    lt(bob,26)
    fd(bob,61)
    rt(bob,180)
    fd(bob,61)

    lt(bob,28)
    fd(bob,54)
    rt(bob,180)
    fd(bob,54)
        
    pu(bob)
    fd(bob,100)
def seven_pie_algo(bob):

    #outline for seven pie
    fd(bob,50)
    lt(bob,51)

def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    
    Reviewed and looks good.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees

    Reviewed and looks good.
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius

    Reviewed and looks good.
    """
    arc(t, r, 360)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    main()
 
