import turtle
from turtle import *
class Cell(Turtle):
	def __init__(self,canvas, row,col,color):
		RawTurtle.__init__(self, canvas)
		self.col = col
		self.row = row
		self.piece = None
		self.color = color
		
	def getCol(self):
		return self.col

	def getRow(self): 
		return self.row

	def getColor(self):
		return self.color
		
	def getPiece(self) :
		return self.piece
	
	def setPiece(self):
		self.piece = piece

