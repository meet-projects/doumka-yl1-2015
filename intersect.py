def intersect(piece1,piece2):
	global pieces
	dist = math.sqrt((piece1.xcor() - piece2.xcor())**2 + (piece1.ycor() - piece2.ycor())**2)
	radius1=(CELL_SIZE-10)/2
	radius2=(CELL_SIZE-10)/2
	if dist <= radius1+radius2:
            return True
            piece2.ht()
            pieces.remove(piece2)
        else:
            return False

