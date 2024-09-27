#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

class TurtleSpiral:
  # use interesting shapes and colors
  turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
  turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]
  # Defining variables through init function
  def __init__(self, s, new_color, startx, starty, direction, distance):
    self.t = trtl.Turtle(shape=s)
    self.t.speed(0)
    self.t.color(new_color)
    self.startx = startx
    self.starty = starty
    self.direction = direction
    self.distance = distance
  # Turtle Movements
  def moveTurtle(self):
    self.t.penup()
    self.t.goto(self.startx, self.starty)
    self.t.pendown()
    self.t.setheading(self.direction)
    self.t.forward(distance)
    self.startx = self.t.xcor()
    self.starty = self.t.ycor()
    self.direction = self.t.heading()
  # String Function for step 6
  def __str__(self):
    return (
      f"Turtle Shapes: {self.t.shape()}"
      f"Available Shapes: {self.turtle_shapes}"
      f"Turtle Colors: {self.t.color()}"
      f"Available Colors: {self.turtle_colors}"
    )
    

# create an empty list of turtles
my_turtles = []

# define x and y coordinates (starting)  
startx = 0
starty = 0
# define direction of turtle
direction = 45
#define distance between each turtle
distance = 50

# For Loop using Class TurtleSpiral <-- Modification #1 through Modification #5
for i in range(len(TurtleSpiral.turtle_shapes)):
  shape = TurtleSpiral.turtle_shapes[i]
  color = TurtleSpiral.turtle_colors.pop()
  turtleSpiral = TurtleSpiral(shape, color, startx, starty, direction, distance)
  turtleSpiral.moveTurtle()
  my_turtles.append(turtleSpiral)
  startx = turtleSpiral.t.xcor()
  starty = turtleSpiral.t.ycor()
  direction -= 45
  distance += 5
  print(turtleSpiral)

wn = trtl.Screen()
wn.mainloop()
