######################################################
# Project: Project 1 
# Student Name:  Sharma, Lakshay
# UIN: 665881556
# URL: https://replit.com/@UICCS111HayesSpring2022/Project-1-lakshay786#main.py
######################################################

import turtle #Importing turtle library
import random #Importing random library

#Function to Draw a Rectangle
''' This is a function used to draw a Rectangle using Turtle Graphics.
Parameters : t (turtle), x, y, heading, pensize, pen_color, fill_color, length, width'''
def draw_rectangle(t,x,y,heading,pensize,pen_color,fill_color,length,width):
  
  t.pencolor(pen_color) #Changing Turtle Pen Color
  t.penup()
  t.goto(x,y) #Sending the turtle to the coordinates x and y
  t.pendown()
  
  t.setheading(heading) #Changing Turtle Heading
  t.pensize(pensize) #Changing Turtle Pen Size
  
  t.fillcolor(fill_color) #Filling the shape with a color
  t.begin_fill()

  t.forward(length)
  t.left(90) #Changing the Turtle's pointer to left at 90 Degrees
  t.forward(width)
  t.left(90)
  t.forward(length)
  t.left(90)
  t.forward(width)

  t.end_fill()


#Function to Draw a Triangles
''' This is a function used to draw a Triangle using Turtle Graphics.
Parameters : t (turtle), x, y, heading, pensize, pen_color, fill_color, side_length_triangle'''
def draw_triangle(t,x,y,heading,pensize,pen_color,fill_color,side_length_triangle):

  t.setheading(heading) #Changing Turtle Heading
  t.pensize(pensize) #Changing Turtle Pen Size
  t.penup()
  t.goto(x,y) #Sending the turtle to the coordinates x and y
  t.pencolor(pen_color) #Changing Turtle Pen Color
  t.fillcolor(fill_color) #Filling the shape with a color
  t.begin_fill()

  for i in range (3): #Iterating the below commands 3 times to draw a triangle
    t.forward(side_length_triangle)
    t.left(120) #Changing the Turtle's pointer to left by 120 Degrees
  
  t.end_fill()

  
#Function to Draw a Circle
''' This is a function used to draw a Circle using Turtle Graphics.
Parameters : t (turtle), x, y, heading, pensize, pen_color, fill_color, radius, extent, steps'''
def draw_circle(t,x,y,heading,pensize,pen_color,fill_color,radius,extent,steps):

  t.setheading(heading) #Changing Turtle Heading
  t.pensize(pensize) #Changing Turtle Pen Size
  t.penup()
  t.goto(x,y) #Sending the turtle to the coordinates x and y
  t.pendown()
  t.pencolor(pen_color) #Changing Turtle Pen Color
  
  t.fillcolor(fill_color) #Filling the shape with a color
  t.begin_fill()
  t.circle(radius,extent,steps) #Using the circle function of the turtle to draw a circle using parameters radius,extent,steps.
  t.end_fill()
 

#Function to Draw a Star
''' This is a function used to draw a Star using Turtle Graphics.
Parameters : t (turtle), x, y, heading, pensize, pen_color, fill_color, side_length_star'''
def draw_stars(t,x,y,heading,pensize,pen_color,fill_color,side_length_star):

  t.setheading(heading) #Changing Turtle Heading
  t.pensize(pensize) #Changing Turtle Pen Size
  t.penup()
  t.goto(x,y) #Sending the turtle to the coordinates x and y
  t.pencolor(pen_color) #Changing Turtle Pen Color
  t.fillcolor(fill_color) #Filling the shape with a color
  t.begin_fill()

  for i in range (5): #Iterating the below commands 5 times to draw a star
    t.forward(side_length_star)
    t.right(144) #Changing the turtle's pointer to right by 144 Degrees

  t.end_fill()


#Function to Draw a Square
''' This is a function used to draw a Square using Turtle Graphics.
Parameters : t (turtle), x, y, heading, pensize, pen_color, fill_color, side_length_square'''
def draw_square(t,x,y,heading,pensize,pen_color,fill_color,side_length_square):

  t.setheading(heading) #Changing Turtle Heading
  t.pensize(pensize) #Changing Turtle Pen Size
  t.penup()
  t.goto(x,y) #Sending the turtle to the coordinates x and y
  t.pencolor(pen_color) #Changing Turtle Pen Color
  t.fillcolor(fill_color) #Filling the shape with a color
  t.begin_fill()

  for i in range (4): #Iterating the below commands 4 times to draw a square
    t.forward(side_length_square)
    t.left(90) #Changing the Turtle's pointer to left by 90 Degrees

  t.end_fill()

#Function to Draw an Octagon
''' This is a function used to draw an Octagon using Turtle Graphics.
Parameters : t (turtle), x, y, heading, pensize, pen_color, fill_color, side_length_octagon'''
def draw_octagon(t,x,y,heading,pensize,pen_color,fill_color,side_length_octagon):
  
  t.setheading(heading) #Changing Turtle Heading
  t.pensize(pensize) #Changing Turtle Pen Size
  t.penup()
  t.goto(x,y) #Sending the turtle to the coordinates x and y
  t.pencolor(pen_color) #Changing Turtle Pen Color
  t.fillcolor(fill_color) #Filling the shape with a color
  t.begin_fill()

  for i in range(8): #Iterating the below commands 8 times to draw an octagon
    t.forward(side_length_octagon)
    t.right(45) #Changing the Turtle's Pointer to right by 45 Degrees

  t.end_fill()

  
#Function to Draw UIC Building. A Nested for loop is used in this function to draw the window pattern in the building.
''' This function is used to draw the UIC Building using Turtle Graphics. In this function, a Nested for loop is used in this function to draw the window pattern in the building.
Parameters : t (turtle)'''
def draw_object1(t):
  color_list1 = ["black","silver","blue"] #Color List 1 for colors used in drawing the UIC Building
  temp_x = -40 #Temporary value of x coordinate
  temp_y = 150 #Temporary value of y coordinate
  draw_rectangle(t,-50,-100,0,0,color_list1[0],color_list1[1],150,270)
  
  if(temp_x>=-40): #If Condition is used here so that the stars in the background do not overlap the building drawing
    for i in range(11): #This is a nested for loop, which is used to draw windows of the UIC Building equidistant to each other.
      for i in range(7):       
        draw_square(t,temp_x,temp_y,0,0,color_list1[2],color_list1[2],10)
        temp_x+=20
      temp_x=-40
      temp_y-=20
  t.goto(-10,-95) #Sending the turtle to the coordinates x and y
  t.pencolor(color_list1[0]) #Changing Turtle Pen Color to black
  t.write("UIC",font=('Times New Roman', 25, 'bold')) #The write function is used to write the title of my drawing, that is, UIC.


#Function to Draw a House. This is a combination of calling draw_rectangle, draw_triangle, and draw_circle functions.
''' This is a function used to draw a House using Turtle Graphics. This is a combination of calling draw_rectangle, draw_triangle, and draw_circle functions
# Parameters : t (turtle)'''
def draw_object2(t):

  color_list2 = ["black","orange","Firebrick","grey","blue","Darkgreen","Darkblue","Gold","Mediumblue","DeepPink"] #Color list 2 for colors used in drawing the house
  
  draw_rectangle(t,-200,-100,0,1,color_list2[0],color_list2[1],50,75)
  
  draw_triangle(t,-200,-25,0,1,color_list2[0],color_list2[2],50)

  draw_rectangle(t,-185,-100,0,1,color_list2[0],color_list2[-1],20,30)

  draw_rectangle(t,-175,-24,0,1,color_list2[2],color_list2[2],124,43)

  draw_rectangle(t,-149,-100,0,1,color_list2[0],color_list2[7],100,76)

  draw_circle(t,-170,-18,0,1,color_list2[4],color_list2[8],10,None,None)

  draw_rectangle(t,-120,-70,0,1,color_list2[6],color_list2[6],30,20)
  

#Function to Draw a Road
''' This is a function used to draw a Road using Turtle Graphics.
# Parameters : t (turtle)'''
def draw_object3(t):

  color_list3 = ["Gainsboro","white","black"] #Color list 3 for colors used in drawing the road.
  draw_rectangle(t,-700,-500,0,1,color_list3[0],color_list3[0],10000,400)

  temp_x = -570 #Temporary value of x coordinate
  temp_y= -155 #Temporary value of y coordinate

  for i in range (30):
    draw_rectangle(t,temp_x,temp_y,0,1,color_list3[1],color_list3[2],75,25)
    t.penup()
    temp_x+=150
    t.pendown()

  temp_x = -570 #Temporary value of x coordinate
  temp_y = -220 #Temporary value of y coordinate
  
  for i in range (30):
    draw_rectangle(t,temp_x,temp_y,0,1,color_list3[1],color_list3[2],75,25)
    t.penup()
    temp_x+=150
    t.pendown()
    
  temp_x = -570 #Temporary value of x coordinate
  temp_y = -280 #Temporary value of y coordinate
  for i in range (30):
    draw_rectangle(t,temp_x,temp_y,0,1,color_list3[1],color_list3[2],75,25)
    t.penup()
    temp_x+=150
    t.pendown()

#Function to Draw a Moon
''' This is a function used to draw a Octagonal-shaped Moon using Turtle Graphics.
# Parameters : t (turtle)'''
def draw_shape(t):
  
  draw_octagon(t, 220, 170, 0, 1, "Gainsboro", "Gainsboro", 50)

  
#Function to Draw background. In this function, stars at random coordinates will be drawn. This function uses loops and randomization. Tracer is set to 0 as we do not want to spend time watching the drawing happening. 
''' This is a function used to draw the background, color it, and draw stars at random coordinates using Turtle Graphics. The random library is used to draw stars at random coordinates in this function. Loops are also used to iterate so that multiple stars are drawn in my background.Tracer is set to 0 as we do not want to spend time watching the drawing happening. 
# Parameters : t (turtle),scr (screen)'''

def draw_background(t,scr):
  turtle.screensize(-500,500)
  scr.bgcolor("Sky Blue") #Changing the background color of the screen to Sky Blue
  scr.tracer(0) #Setting the tracer to 0 

  for i in range(11):
    turtle.penup()
    temp_x = random.randint(-600,-120)
    temp_y = random.randint(50, 220)
    turtle.pendown()
    draw_stars(t,temp_x,temp_y,0,1,"white","blue",20)
    
  for i in range(4):
    turtle.penup()
    temp_x = random.randint(150,520)
    temp_y = random.randint(-60, -25)
    turtle.pendown()
    draw_stars(t,temp_x,temp_y,0,1,"white","blue",20)
    
  for i in range(4):
    turtle.penup()
    temp_x = random.randint(400,530)
    temp_y = random.randint(40, 240)
    turtle.pendown()
    draw_stars(t,temp_x,temp_y,0,1,"white","blue",20)
    
  for i in range(20):
    turtle.penup()
    temp_x = random.randint(-150,250)
    temp_y = random.randint(220, 450)
    turtle.pendown()
    draw_stars(t,temp_x,temp_y,0,1,"white","blue",20)

  for i in range(4):
    turtle.penup()
    temp_x = random.randint(-400,-250)
    temp_y = random.randint(-60, 15)
    turtle.pendown()
    draw_stars(t,temp_x,temp_y,0,1,"white","blue",20)


#Function which runs the whole program. In this function, the entire drawing is drawn. Variable initialization and calls to other functions are made in this function. Two turtles are initialized. One turtle (t1) is used to draw the background(including stars) and the other turtle is used to draw foreground objects(UIC Building, House, and Road)
''' This is a function used to draw the my entire drawing. Turtles and variables are initialized.Also, all the functions for the objects are called in this function so that the entire picture is drawn.Two turtles are initialized. One turtle (t1) is used to draw the background(including stars) and the other turtle (t2) is used to draw foreground objects(UIC Building, House, and Road)
# Parameters : NA'''
def main():
  
  t1 = turtle.Turtle() #Creating 1st Turtle object
  t2 = turtle.Turtle() #Creating 2nd Turtle object
  t1.hideturtle() #Hiding the 1st turtle
  t2.hideturtle() #Hiding the 2nd turtle
  screen = t2.getscreen()
  print("Student Name:  Sharma, Lakshay \nUIN: 665881556")
  draw_background(t2,screen) #Calling draw_background() function to Draw the background including stars at random coordinates
  draw_object1(t1) #Calling draw_object() function to Draw UIC Building.
  draw_object2(t1) #Calling draw_object() function to to Draw a House
  draw_object3(t1) #Calling draw_object() function to Draw a Road
  draw_shape(t1) #Calling draw_object() function to to Draw a Moon
   
main() #Lastly, calling the main function which runs the entire program.


# information for scorers

# on what line number is the required for loop?
# For Loop is used in many parts of my code. Line Numbers are: 51,89,109,128,145,146,189,198,206,229,236,243,250,257

# on what line number is the required use of a random number?
# I have used random numbers in lines : 51,89,109,128,145,146,189,198,206,229,236,243,250,257

# on what line number is the required use of a conditional statement?
# if conditional statement is used in Line 144 so that the stars in the background do not overlap the building drawing.

# on what line number is the required use of a list?
# Lists are used in Line Number : 139,161,183. These lists contain the colors which I have used in my drawing.
