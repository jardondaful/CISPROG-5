import turtle 
from shapes import *  

def main():
  turtle.setup(width=400, height=400) 
  rect = Rectangle(-100, 50, 200, 100, turtle, (0,0,0))
  rect.draw()
  line = Line(-120,50,120,50, turtle, (0,0,0)) 
  line.draw() 
  line = Line(120,50, 0,120, turtle, (0,0,0)) 
  line.draw() 
  line = Line(0,120,-120,50, turtle, (0,0,0)) 
  line.draw() 
  rect = Rectangle(-25, 20, 50, 70, turtle, (0,0,0)) 
  rect.draw() 
  circle = Circle(13,-18,5, turtle, (0,0,0) ) 
  circle.draw()
  circle = Circle(0,-80,10, turtle, (0,0,0) ) 
  circle.draw()
  line = Line(-20,-100,20,-100, turtle, (0,0,0)) 
  line.draw()
  line = Line(0,-90,0,-125, turtle, (0,0,0)) 
  line.draw()
  line = Line(0,-125,-15,-135, turtle, (0,0,0)) 
  line.draw()
  line = Line(0,-125, 15,-135, turtle, (0,0,0)) 
  line.draw()

if __name__ == "__main__":
  main()
