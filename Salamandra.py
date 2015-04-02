
def checkMove(p,c):
	if  p.queen == False:
		col1 = p.getCell().getCol()
		row1 = p.getCell().getRow()
		col2 = c.getCol()
		row2 = c.getRow()
		if abs(col1-col2) == 1 and ((p.getColor() == "b" and row1-row2 == 1) or (p.getcolor()) == "w" and row2-row1 == 1)):
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
	regularList = []
	eatList = []
	col1 = p.getCell().getCol()
	row1 = p.getCell().getRow()
	if p.queen == False:
		for i in [-2,-1,1,2]:
			for j in [-2,-1,1,2]:
				tempC = board[row1+i][col1+j]
				if checkMove(p,tempC) == "regular":
					regularList.append (tempC)
				elif checkMove (p,tempC) == "eat":
					eatList.append (tempC)
		if len(eatList) != 0:
			return eatList
		else:
			return regularList
		


#click piece
for p in pieces:
	p.onclick(pieceClicked, btn=1)
for row in board:
	for cell in row:
		if cell.getColor() == "b":
			c.onclick(cellClicked, btn=1)

def convXYtoRowCol(x,y):
	topLeftCorner = (x-3.5*CELL_SIZE,y-6*CELL_SIZE)
	diff = (x-topLeftCorner[0], y-topLeftCorner[1])
	boardLoc = (int(diff[0]/CELL_SIZE), int(diff[1]/CELL_SIZE)) ##col, row 
	return boardLoc
 currentPossibleMoves = []
def pieceClicked(x,y):
	global currentPossibleMoves

	col,row = convXYtoRowCol (x,y)
	cellOfPiece = board[row][col]
	piece = cellOfPiece.getPiece()
	if selectedPiece == piece:
		selectedPiece = None
	else:
		selectedPiece = piece
		currentPossibleMoves = availableMoves(piece)

#check if empty

selectedPiece = None ## None or Piece Object







#clicking function