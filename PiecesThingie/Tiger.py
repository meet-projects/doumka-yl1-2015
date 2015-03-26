
class Piece(Turtle)
	def __init__(self,cell,color): ###color has to be 'w' or 'b'
	RawTurtle.__init__(self)
	self.queen = False
	self.color = color
	self.cell = cell
	
	def getColor(self):
		return self.color
	def getCell(self):
		return self.cell
	def setQueen(self):
		self.queen=True



##	def checkUpRight(self): #if possible, merge
##		#check the right cell.
##		#find color
##		#if color==not my team, I can eat.
##		#return true/false
##
##		if 
##		
## 	def checkUpLeft(self): #if possible, merge
##		#check the right cell.
##		#find color
##		#if color==not my team, I can eat.
##		#return true/false
##
##	def checkDownLeft(self): #if possible, merge
##		#check if queen 
##		#check the right cell.
##		#find color
##		#if color==not my team, I can eat.
##		#return true/false
##	
##	def checkDownRight(self): #if possible, merge
##		#check if queen 
##		#check the right cell.
##		#find color
##		#if color==not my team, I can eat.
##		#return true/false
##
##	def whereCanGo
##		self.checkUpLeft
##		self.checkUpRight
##		self.checkDownLeft
##		self.checkDownRight
##
##
##	def function():
##		self.color==PlayerColor
##
##		if cell==empty():
##			#add to "possible moves" list
##		if Piece.color==
