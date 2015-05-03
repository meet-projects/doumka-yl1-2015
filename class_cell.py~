import turtle
from turtle import *
class Cell(Turtle):
	def __init__(self,canvas, row,col,x ,y,color):
		RawTurtle.__init__(self, canvas)
		self.col = col
		self.row = row
		self.piece = None
		self.color = color
		self.shape("square")
		self.goto(x*50-150,y*50-75)
		if (color == "b"):
			self.pencolor("red")
			self.fillcolor("red")
		else:
			self.pencolor("white")
			self.pencolor("black")
   		
		
	def getCol(self):
		return self.col

	def getRow(self): 
		return self.row

	def getColor(self):
		return self.color
		
	def getPiece(self) :
		return self.piece
	
	def setPiece(self,piece):
		self.piece = piece

