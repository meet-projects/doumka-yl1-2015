# DO NOT CHANGE THE NEXT 3 LINES
import turtle
import random
turtle.hideturtle()
turtle.tracer(0)
# variables that set up the game
# CHANGE THESE AS NEEDED

BOARD_HEIGHT = 8
BOARD_WIDTH = 8
START_X = -175
START_Y = -100
CELL_SIZE = 50 # side length of the square
PLAYER1 = 'white'
PLAYER2 = 'blue'
board = [[0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7],
         [0,1,2,3,4,5,6,7]]

cur_player = 1

# draws a vertical line on the screen
# It should start at (x, y) and be of size length

def vert_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+8*50)
    
# draws a horizontal line on the screen
# It should start at (x, y) and be of size length

def horiz_line(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+8*50,y)

# draw the entire game board using the vert_line
# and horiz_line functions starting at (x, y)

def fill_background(color):
    turtle.goto(-195,-120)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(-195,320)
    turtle.goto(250,320)
    turtle.goto(250,-120)
    turtle.goto(-195,-120)
    turtle.end_fill()
fill_background("#dbb67a")

# this is fill sq

def fill_black_board_sq(START_X,START_Y):
    turtle.penup()
    turtle.goto(START_X,START_Y)
    turtle.pendown()
    turtle.fillcolor("gray")
    turtle.begin_fill()
    turtle.goto(START_X+50,START_Y)
    turtle.goto(START_X+50,START_Y+50)
    turtle.goto(START_X,START_Y+50)
    turtle.goto(START_X,START_Y)
    turtle.end_fill()
    

def fill_white_board_sq(START_X,START_Y):
    turtle.penup()
    turtle.goto(START_X+50,START_Y)
    turtle.pendown()
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.goto(START_X+50,START_Y)
    turtle.goto(START_X+50,START_Y+50)
    turtle.goto(START_X,START_Y+50)
    turtle.goto(START_X,START_Y)
    turtle.end_fill()

# input the column number, row number, and piece color
# and draw a circular game piece

def draw_piece(col,row,PLAYER):
    x=25+50*col+START_X
    y=50*(7-row)+START_Y
    turtle.color(PLAYER)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(PLAYER)
    turtle.begin_fill()
    turtle.circle(22)
    turtle.end_fill()
    
    
# this function ACTUALLY DRAW THE BOARD    
def draw_board():
    turtle.pensize(4)
    x=START_X
    y=START_Y
    for i in range(0,9):
        vert_line(x,y)
        x+=50
    
    x=START_X
    
    for i in range(0,9):
        horiz_line(x,y)
        y+=50
# fill white , black sq in the board 
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)

START_X = -175
START_Y = -100
START_X+=50

for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)

START_X = -175
START_Y = -100
START_Y+= 50

for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_white_board_sq(START_X+100*i,START_Y)

START_X = -175
START_Y = -100
START_X+=50
START_Y+= 50

for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
START_Y+=100
for i in range(0,4):
    fill_black_board_sq(START_X+100*i,START_Y)
    
START_X = -175
START_Y = -100

draw_board()

#_____________________________________________________________________________

for i in range(1,9):
    turtle.pu()
    turtle.goto(START_X-10,START_Y+15)
    turtle.pd()
    START_Y+=50
    turtle.write(i, move=False, align="center", font=("Arial", 15, "bold"))
    
START_X = -175
START_Y = -100

turtle.goto(START_X+25,START_Y-23)
turtle.write("A", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+50,START_Y-23)
turtle.write("B", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+100,START_Y-23)
turtle.write("C", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+150,START_Y-23)
turtle.write("D", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+200,START_Y-23)
turtle.write("E", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+250,START_Y-23)
turtle.write("F", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+300,START_Y-23)
turtle.write("G", move=False, align="center", font=("Arial", 15, "bold"))
turtle.goto(START_X+25+350,START_Y-23)
turtle.write("H", move=False, align="center", font=("Arial", 15, "bold"))

#_________________# check for a win___________________




#_____________________________________________________


turtle.mainloop()
