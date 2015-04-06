# DO NOT CHANGE THE NEXT 3 LINES
import turtle
import random
import Tiger
from Tiger import *
import class_cell
from class_cell import *

turtle.hideturtle()
##turtle.tracer(0)
# variables that set up the game
# CHANGE THESE AS NEEDED
turtle.speed(0)

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


##cur_player = 1

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

selectedPiece = None ## None or Piece Object
def checkMove(p,c):
	if  p.queen == False:
		col1 = p.getCell().getCol()
		row1 = p.getCell().getRow()
		col2 = c.getCol()
		row2 = c.getRow()
		if abs(col1-col2) == 1 and ((p.getColor() == "b" and row1-row2 == 1) or (p.getColor() == "w" and row2-row1 == 1)):
			if c.getPiece() == None:
				return "regular"
			else:
				p2 = c.getPiece()
				if p1.getColor() == p2.getcolor():
					return False
				else:
					col3 = col2 + (col2 - col1)
					row3 = row2 + (row2 - row1)
					if col3 < 0 or col3 > 7 or row3 < 0 or row3 > 7 :
						return False
					else:
						c3 = board[row3][col3]
						if c3.getPiece() == None:
							return "eat"
						else:
							return False


def availableMoves(p):
	global goingToEat
	regularList = []
	eatList = []
	col1 = p.getCell().getCol()
	row1 = p.getCell().getRow()
	if p.queen == False:
		for i in [-2,-1,1,2]:
			for j in [-2,-1,1,2]:
				if (row1+i >= 0 and row1+i <=7 and col1+j >=0 and col1+j <=7):
					tempC = board[row1+i][col1+j]
					if checkMove(p,tempC) == "regular":
						regularList.append (tempC)
					elif checkMove (p,tempC) == "eat":
						eatList.append (tempC)
		if len(eatList) != 0:
			goingToEat = True
			return eatList
		else:
			goingToEat = False
			return regularList
		
def pieceClicked(x,y):
	##print((x,y))
	global currentPossibleMoves
	global selectedPiece
	col,row = convXYtoRowCol(x,y)
	##print((col,row))
	cellOfPiece = board[row][col]
	##print (cellOfPiece.getRow())
	piece = cellOfPiece.getPiece()
	print("piece: " + str(piece))
	if selectedPiece == piece:
		print("canceled selection")
		selectedPiece = None
		currentPossibleMoves = []
		goingToEat = False
	else:
		if piece.getColor() == turn:
			print("selected")
			selectedPiece = piece
			currentPossibleMoves = availableMoves(piece)

def cellClicked(x,y):
	if selectedPiece != None:
		col,row = convXYtoRowCol()
		cell = board [row][col]
		if cell in currentPossibleMoves:
			move(selectedPiece, cell)
			selectedPiece = None
			goingToEat = False
			currentPossibleMoves = []
			changeTurn()
		   

def move(piece, destCell):
	selectedPiece.setCell(cell)
	cell.setPiece(selectedPiece)
	currentCell = piece.getCell()
	while currentCell != destCell:
		currentCell = moveOne(piece,destCell)
		if currentCell.getPiece() != None:
			foundPiece = currentCell.getPiece()
			foundPiece.ht()
			currentCell.setPiece(None)
			pieces.remove(foundPiece)




def moveOne(piece,destCell):
	col1 = piece.getCell().getCol()
	row1 = piece.getCell().getRow()
	destRow = destCell.getRow()
	destCol = destCell.getCol()
	direc = ((destRow - row1)/(abs(destRow - row1)), (destCol - col)/(abs(destCol - col1)))
	nextRow, nextCol = (row1 + direc[0], col1 + direc[1])
	nextCell = board[nextRow][nextCol]
	piece.goto(cellCenter(nextCell))
	return nextCell



def print2(x,y):
	print(x,y)


##def printC(x,y):
	##print(convXYtoRowCol(x,y))
	##turtle.onscreenclick(print)
def convXYtoRowCol(x,y):
	topLeftCorner = (-3.5*CELL_SIZE, 6*CELL_SIZE)
	##print("topLeft: " + str(topLeftCorner))
	diff = (x-topLeftCorner[0], topLeftCorner[1]-y)
	boardLoc = (int(diff[0]/CELL_SIZE), int(diff[1]/CELL_SIZE)) ##col, row 
	return boardLoc
currentPossibleMoves = []
goingToEat = False

def intersect(piece1,piece2):
	global pieces
	dist = math.sqrt((piece1.xcor() - piece2.xcor())**2 + (piece1.ycor() - piece2.ycor())**2)
	radius1=(CELL_SIZE-10)/2
	radius2=(CELL_SIZE-10)/2
	if dist <= radius1+radius2:
		return True
	else:
		return False


def getCenter(cell):
	cellLoc = (cell.getCol(), cell.getRow()) ##(
	cellCenter = (CELL_SIZE*BOARD_WIDTH-225-CELL_SIZE*cellLoc[0]+25, CELL_SIZE*BOARD_HEIGHT-150-CELL_SIZE*cellLoc[1]+25)
	return cellCenter  

#check if empty



############## creating pieces
pieces = []
for i in range (5,8):
	for j in range(0,8,2):
		if i % 2 == 0:
			t = Piece(screen, board[i][j], "b")
			board[i][j-1].setPiece(t)
			t.shape("triangle")
			t.pu()
			t.goto(getCenter(t.getCell()))
			pieces.append(t)
		else:
			t = Piece(screen, board[i][j+1], "b")
			board[i][j].setPiece(t)
			t.shape("triangle")
			t.pu()
			t.goto(getCenter(t.getCell()))
			pieces.append(t)
for i in range (0,3):
	for j in range(0,8,2):
		if i % 2 == 0:
			t = Piece(screen, board[i][j], "w")
			board[i][j-1].setPiece(t)
			t.shape("triangle")
			t.showturtle()
			t.pu()
			t.goto(getCenter(t.getCell()))
			pieces.append(t)
		else:
			t = Piece(screen, board[i][j+1], "w")
			board[i][j].setPiece(t)
			t.shape("triangle")
			t.pu()
			t.goto(getCenter(t.getCell()))
			pieces.append(t)
turtle.hideturtle()




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


for p in pieces:
	p.onclick(pieceClicked, btn=1)
	##p.shape("triangle")
	##print(p)
for row in board:
	for cell in row:
		if cell.getColor() == "b":
			cell.onclick(cellClicked, btn=1)

	
	

##draw_pieces()

##c = turtle.Turtle()
##c.shape("triangle")
##c.showturtle()   
##c.pendown()
##c.shapesize(2000)
##turtle.onscreenclick(c.goto)

#interactions with cell class+ pieces#






turn = "w"
def changeTurn():
	if turn == 'w':
		turn = 'b'
	else:
		turn = 'w'
def check4win():
	global pieces
	bc=0
	wc=0
	for n in pieces:
		if piece.getColor=='b':
			bc+=1
		if piece.getColor=='w':
			wc+=1
	if bc==0:
		#white wins
		turtle.write("player 1 wins!", True, align="center", font=("Arial", 80, "normal"))
		return True
	if wc==0:
		#black wins
		turtle.write("player 2 wins!", True, align="center", font=("Arial", 80, "normal"))
		return True
	return False

screen.listen()

for row in board:
	for cell in row:
		print("row: "+ str(cell.getRow()) + " col: " + str(cell.getCol()) + " Piece: " + str(cell.getPiece()))
	


#clicking function
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
