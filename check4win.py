import turtle
def check4win():
	global pieces
	int bc=0
	int wc=0
	for n in pieces:
		if (piece.getColor=='b'):
			bc+=1
		if (piece.getColor=='w'):
			wc+=1
	if(bc==0):
		#white wins
		turtle.write("player 1 wins!", True, align="center", font=("Arial", 80, "normal"))
		return True
	if(wc==0):
		#black wins
		turtle.write("player 2 wins!", True, align="center", font=("Arial", 80, "normal"))
		return True
	return False

turtle.mainloop()



		
			

