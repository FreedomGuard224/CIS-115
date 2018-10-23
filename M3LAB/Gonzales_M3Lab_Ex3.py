import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def main():

    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.000001

    pumpkin(bob)

def pumpkin(bob):
    lt(bob,90)
    fd(bob,100)
    lt(bob,45)

    big_curve(bob)

    lt(bob,35)
    fd(bob,100)
    lt(bob,45)

    big_curve(bob)

    rt(bob,120)
    
    small_curve(bob)
    end_curve(bob)
    
    for x in range (25):
        fd(bob,2)
        lt(bob,1)
        
    for x in range (50):
        fd(bob,2)
        lt(bob,2)
        
    for x in range (25):
        fd(bob,2)
        lt(bob,2)
        
    for x in range (10):
        fd(bob,2)
        lt(bob,3)
    
    pu(bob)
    lt(bob,50)
    fd(bob,120)

    pd(bob)

    fd(bob,25)
    rt(bob,90)
    fd(bob,5)
    rt(bob,90)
    fd(bob,25)

    pu(bob)
    fd(bob,150)

def big_curve(bob):
    for x in range (50):
        fd(bob,1)
        lt(bob,2)

def small_curve(bob):
    for x in range (50):
        fd(bob,1)
        lt(bob,2)
    for x in range (50):
        fd(bob,2)
        lt(bob,2)
           
def end_curve(bob):
    for x in range (50):
        fd(bob,2)
        lt(bob,1)
        

    
        

    
    
main()

