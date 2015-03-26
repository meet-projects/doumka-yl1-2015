# DO NOT CHANGE THE NEXT 3 LINES
import turtle
import random
import Tiger
from Tiger import *
import class_cell
from class_cell import *

turtle.hideturtle()
turtle.tracer(1)
# variables that set up the game
# CHANGE THESE AS NEEDED

BOARD_HEIGHT = 8
BOARD_WIDTH = 8
START_X = -175
START_Y = -100
CELL_SIZE = 50 # side length of the square
screen = turtle.getscreen()

PLAYER1 = 'w'
PLAYER2 = 'b'
#board = [["black","white","black","white","black","white","black","white"], #row0
         #["white","black","white","black","white","black","white","black"], #row1
         #["black","white","black","white","black","white","black","white"], #row2
         #["white","black","white","black","white","black","white","black"], #row3
         #["black","white","black","white","black","white","black","white"], #row4
         #["white","black","white","black","white","black","white","black"], #row5
         #["black","white","black","white","black","white","black","white"], #row6
         #["white","black","white","black","white","black","white","black"]] #row7
board = []
for i in range(8):
    board.append([])
for rowNum in range(8):
    for colNum in range(8):
        if (rowNum+colNum)%2 == 0:
            board[rowNum].append(Cell(screen,rowNum, colNum, "b"))
        else:
            board[rowNum].append(Cell(screen,rowNum, colNum, "w"))

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
##      self.checkDownRight
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
turtle.penup()
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

turtle.penup()
############## creating pieces
pieces = []
for i in range (5,8):
	for j in range(0,8,2):
		if i % 2 == 0:
			pieces.append(Piece(screen, board[i][j], "b"))
		else:
			pieces.append(Piece(screen, board[i][j+1], "b"))
for i in range (0,3):
	for j in range(0,8,2):
		if i % 2 == 0:
			pieces.append(Piece(screen, board[i][j], "w"))
		else:
			pieces.append(Piece(screen, board[i][j+1], "w"))


def draw_pieces():
	global pieces
	for p in pieces:
		turtle.penup()
		cellLoc = (p.getCell().getCol(), p.getCell().getRow()) ##(
		cellCenter = (CELL_SIZE*BOARD_WIDTH-225-CELL_SIZE*cellLoc[0]+25, CELL_SIZE*BOARD_HEIGHT-150-CELL_SIZE*cellLoc[1]+25)
		
		turtle.goto(cellCenter)
		turtle.pendown()
		if p.getColor()=="b":
			turtle.color("black")
			turtle.dot(CELL_SIZE-10)
		else:
			turtle.color("White")
			turtle.dot(CELL_SIZE-10)
	
	

draw_pieces()


def main():
	global screen
	pass
	
#interactions with cell class+ pieces#

##  def checkUpRight(self): #if possible, merge

##      #check the right cell.
##      #find color
##      #if color==not my team, check cell x+1, y+1
        #if cell==empty , I can eat.
##     
##      
##  def checkUpLeft(self): #if possible, merge

##      #check the right cell.
##      #find color
##      #if color==not my team, check one cell y+1, x-1
        #if empty,I can eat.
##      #return true/false
##
##  def checkDownLeft(self): #if possible, merge
##      #check if queen 
##      #check the right cell.
##      #find color
##      #if color==not my team, check cell x-1, y-1
        #if cell==empty, I can eat.
##      #return true/false
##  
##  def checkDownRight(self): #if possible, merge
##      #check if queen 
##      #check the right cell.
##      #find color
##      #if color==not my team, check x+1, y-1
        #if cell==empty, I can eat.
##      #return true/false
##
##  def whereCanGo
##      self.checkUpLeft
##      self.checkUpRight
##      self.checkDownLeft
##      self.checkDownRight
##
##
##  def function():
##      self.color==PlayerColor
##
##      if cell==empty():
##          #add to "possible moves" list
##      if Piece.color==


#_________________# check for a win___________________




#_____________________________________________________


turtle.mainloop()
