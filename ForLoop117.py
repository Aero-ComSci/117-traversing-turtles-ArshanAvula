#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

# define x and y coordinates (starting)  
startx = 0
starty = 0

# define direction of turtle
direction = 45
#define distance between each turtle
distance = 50

# iterates over every turtle created, to move it 50 forward and 45 degrees to the right from the starting point
for t in my_turtles:
  t.speed(0)
  #Modification 1: set pen up before and set pen down after (start position)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  #Modification 3: change color for each turtle drawn
  new_color = turtle_colors.pop()
  t.fillcolor(new_color)
  t.begin_fill()
  t.end_fill()
  t.pencolor(new_color)
  #Modification 4: change heading/direction of turtle
  t.setheading(direction)
  direction -= 45
  #Modification 5: expanding, so that the turtle spirals outwards
  t.forward(distance)
  distance += 5
  # Modificaion 2: set turtle to where it left off
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()
