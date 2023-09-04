from tkinter import *
from PIL import ImageTk, Image
import random
from playsound import playsound

gametab = Tk()
gametab.title("Mancala")
gametab.geometry("1200x1200")
bg = PhotoImage(file = "mancaladownload.png") #mancala board
canvas1 = Canvas(gametab, width = 400, height = 800, bg  =  "aliceblue")
canvas1.pack(fill = "both", expand= True)

canvas1.create_image(500, 60, image = bg, anchor = "nw") #500 = xcoordinates, 60 = ycoordinates, top left = 00 00, down and right = increasing positively 
#gametab.iconbitmap('C:\Users\freda\OneDrive - London Academy of Excellence\Coding\EPQ\Coding and coding files') #icon next to title
gametab.iconbitmap('marbles.ico') #I REPLACED THE ABOVE LINE WITH THIS LINE (RELATIVE FILE NAME) SO IT WORKS WHEN RUNNING ON A DIFFERENT COMPUTER - DR. WATTS

#allowing player to exit game

def leavegame():
    exit()

#allowing player to reset the pieces/choose game mode
def regular():
	regulargame()

def chooseavalanche():
	avalanche()

exitbutton = Button(gametab, text="EXIT", padx=8, pady=2, command=leavegame)
exitbutton_canvas = canvas1.create_window(0, 0, anchor = "nw", window = exitbutton)

regularbutton = Button(gametab, text="REGULAR", padx=16, pady=2, command=regular)
regularbutton_canvas = canvas1.create_window(50, 0, anchor = "nw", window = regularbutton)

avalanchebutton = Button(gametab, text="AVALANCHE", padx=16, pady=2, command=chooseavalanche)
avalanchebutton_canvas = canvas1.create_window(145, 0, anchor = "nw", window = avalanchebutton)


def regulargame(): 
	global n
	global pebbles
	global pebbles2
	global pebbles3
	global pebbles4
	n=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]
	#button=["pebble0","pebble1","pebble2","pebble3","pebble4","pebble5","pebble6","pebble7","pebble8","pebble9","pebble10","pebble11","pebble12","pebble13"]
	#above line was previously used on the basic model of the game.

	player = ["Player 1 (left hand side) starts", "Player 2 (right hand side) starts"]
	starter = random.choice(player)
	top= Toplevel(gametab)
	top.geometry("300x125")
	top.title("Who's turn is it? (REGULAR MODE)")
	Label(top, text= starter, font=('calibri 12 bold')).place(x=45,y=40)

	Player1 = True 
	
	if starter == player[0]:
		Player1 = True
		print(Player1)
	else:
		Player1 = False
		print(Player1)
	

	def pebble_move(index):
		nonlocal Player1 #must call on the nonlocal player1 as this is a nestled function
		
		playsound('soundeffects2.mp3')


		#print(index)
		hand = n[index]
		#print(hand)
		print(n)
		n[index]=0
		#print(hand)
		#print(n)
		#print(n[index])
		#print(n[index+1])


#going round the board and dropping one stone mechanism below
		for numberofpebbles in range(len(n)):
			if Player1 == True:
				if numberofpebbles > index: #if index1 is after indexofchosendeposit
					if hand>0:
						if numberofpebbles != 13:
							n[numberofpebbles] +=1
							print(n)
							hand=hand-1
							lastplaceindex = numberofpebbles
							lastdepositvalue = n[numberofpebbles]
	
			else:
				if numberofpebbles > index: #if index1 is after indexofchosendeposit
					if hand>0:
						if numberofpebbles != 6:
							n[numberofpebbles] +=1
							print(n)
							hand=hand-1
							lastplaceindex = numberofpebbles
							lastdepositvalue = n[numberofpebbles] 


		print("No of marbles in hand: ", hand)
		while hand!=0:
			for numberofpebbles in range(len(n)):
				if hand>0:
					if Player1 == False:
						if numberofpebbles != 6:
							n[numberofpebbles] += 1
							hand = hand - 1
							print(n)
							lastplaceindex = numberofpebbles
							lastdepositvalue = n[numberofpebbles]
					else:
						if numberofpebbles != 13:
							n[numberofpebbles] += 1
							hand = hand - 1
							print(n)
							lastplaceindex = numberofpebbles
							lastdepositvalue = n[numberofpebbles] 


#capturing opponent's stones
		if hand == 0:
			if lastdepositvalue == 1 and lastplaceindex != 6 and lastplaceindex != 13:
				if Player1 == True:
					oppositepair = 12 - lastplaceindex
					if n[oppositepair] != 0:
						n[6] = n[6] + n[oppositepair] + n[lastplaceindex]
						n[oppositepair] = 0
						n[lastplaceindex] = 0
				else:
					oppositepair = 12 - lastplaceindex
					if n[oppositepair] != 0:
						n[13] = n[13] + n[oppositepair] + n[lastplaceindex]
						n[oppositepair] = 0
						n[lastplaceindex] = 0

#getting extra turns or swapping to the other player
		if hand == 0 and lastplaceindex == 6:
			Player1=True  
		elif hand == 0 and lastplaceindex == 13:
			Player1 = False
		else:
			if Player1 == True:
				Player1 = False
			else:
				Player1 = True
		print(Player1)



#updating pebble count
		deposit0.config(text = n[0])
		deposit1.config(text = n[1])
		deposit2.config(text = n[2])
		deposit3.config(text = n[3])
		deposit4.config(text = n[4])
		deposit5.config(text = n[5])
		deposit6.config(text = n[6])
		deposit7.config(text = n[7])
		deposit8.config(text = n[8])
		deposit9.config(text = n[9])
		deposit10.config(text = n[10])
		deposit11.config(text = n[11])
		deposit12.config(text = n[12])
		deposit13.config(text = n[13])

		
#disabling and enabling sides of the board		
		if Player1 == True:
			deposit0.config(state=NORMAL)
			deposit1.config(state = NORMAL)
			deposit2.config(state = NORMAL)
			deposit3.config(state = NORMAL)
			deposit4.config(state = NORMAL)
			deposit5.config(state = NORMAL)                   
			deposit7.config(state = DISABLED)
			deposit8.config(state = DISABLED)
			deposit9.config(state = DISABLED)
			deposit10.config(state = DISABLED)
			deposit11.config(state = DISABLED)
			deposit12.config(state = DISABLED)

		else:
			deposit0.config(state = DISABLED)
			deposit1.config(state = DISABLED)
			deposit2.config(state = DISABLED)
			deposit3.config(state = DISABLED)
			deposit4.config(state = DISABLED)
			deposit5.config(state = DISABLED)
			deposit7.config(state = NORMAL)
			deposit8.config(state = NORMAL)
			deposit9.config(state = NORMAL)
			deposit10.config(state = NORMAL)
			deposit11.config(state = NORMAL)
			deposit12.config(state = NORMAL)


#declaring a winner
		leftover = 0
		for i in range(6):
			if n[i] >0:
				leftover +=1
			else:
				leftover = leftover
		if leftover == 0:
			print("Gameover. Player 1 is out of marbles")
			for i in range(len(n)):
				if i > 6 and i !=13:
					n[13] = n[i] + n[13]
					n[i] = 0
			deposit0.config(state = DISABLED)
			deposit1.config(state = DISABLED)
			deposit2.config(state = DISABLED)
			deposit3.config(state = DISABLED)
			deposit4.config(state = DISABLED)
			deposit5.config(state = DISABLED)
			deposit7.config(state = DISABLED)
			deposit8.config(state = DISABLED)
			deposit9.config(state = DISABLED)
			deposit10.config(state = DISABLED)
			deposit11.config(state = DISABLED)
			deposit12.config(state = DISABLED)

			if n[13]> n[6]:
				winner = "Player 2 won! "
			elif n[13]<n[6]:
				winner = "Player 1 won!"
			else:
				winner = "It's a tie!"

			top= Toplevel(gametab)
			top.geometry("300x125")
			top.title("Who won?")
			Label(top, text= winner, font=('calibri 12 bold')).place(x=45,y=40)
			print(n)

		leftover2 = 0
		for i in range(7,13):
			if n[i] >0:
				leftover2 +=1
			else:
				leftover2= leftover2
		if leftover2 ==0:
			print("Gameover, player 2 is out of marbles")
			for i in range(len(n)):
				if i<6:
					n[6] = n[6] + n[i]
					n[i] = 0
			deposit0.config(state = DISABLED)
			deposit1.config(state = DISABLED)
			deposit2.config(state = DISABLED)
			deposit3.config(state = DISABLED)
			deposit4.config(state = DISABLED)
			deposit5.config(state = DISABLED)
			deposit7.config(state = DISABLED)
			deposit8.config(state = DISABLED)
			deposit9.config(state = DISABLED)
			deposit10.config(state = DISABLED)
			deposit11.config(state = DISABLED)
			deposit12.config(state = DISABLED)

			if n[13]> n[6]:
				winner = "Player 2 won! "
			elif n[13]<n[6]:
				winner = "Player 1 won!"
			else:
				winner = "It's a tie!"

			top= Toplevel(gametab)
			top.geometry("300x125")
			top.title("Who won?")
			Label(top, text= winner, font=('calibri 12 bold')).place(x=45,y=40)
			print(n)


		deposit0.config(text = n[0])
		deposit1.config(text = n[1])
		deposit2.config(text = n[2])
		deposit3.config(text = n[3])
		deposit4.config(text = n[4])
		deposit5.config(text = n[5])
		deposit6.config(text = n[6])
		deposit7.config(text = n[7])
		deposit8.config(text = n[8])
		deposit9.config(text = n[9])
		deposit10.config(text = n[10])
		deposit11.config(text = n[11])
		deposit12.config(text = n[12])
		deposit13.config(text = n[13])


#adding the image files to the code as variables
	pebbles = ImageTk.PhotoImage(file="marbletry2.png")
	pebbles2 = ImageTk.PhotoImage(file="marbletry5.png")
	pebbles3 = ImageTk.PhotoImage(file="marble6.png")
	pebbles4 = ImageTk.PhotoImage(file="marble4.png")


#adding images of pebbles
	pebble_000 = canvas1.create_image(550, 152, anchor = 'nw', image = pebbles)
	pebble_025 = canvas1.create_image(575, 152, anchor = 'nw', image = pebbles2)
	pebble_050 = canvas1.create_image(550, 176, anchor = 'nw', image = pebbles2)
	pebble_075 = canvas1.create_image(575, 176, anchor = 'nw', image = pebbles)


	pebble_100 = canvas1.create_image(550, 224, anchor = 'nw', image = pebbles)
	pebble_125 = canvas1.create_image(575, 224, anchor = 'nw', image = pebbles2)
	pebble_150 = canvas1.create_image(550, 248, anchor = 'nw', image = pebbles2)
	pebble_175 = canvas1.create_image(575, 248, anchor = 'nw', image = pebbles)


	pebble_200 = canvas1.create_image(550, 294, anchor = 'nw', image = pebbles)
	pebble_225 = canvas1.create_image(575, 294, anchor = 'nw', image = pebbles2)
	pebble_250 = canvas1.create_image(550, 318, anchor = 'nw', image = pebbles4)
	pebble_275 = canvas1.create_image(575, 318, anchor = 'nw', image = pebbles)

	pebble_300 = canvas1.create_image(550, 364, anchor = 'nw', image = pebbles)
	pebble_325 = canvas1.create_image(575, 364, anchor = 'nw', image = pebbles2)
	pebble_350 = canvas1.create_image(550, 388, anchor = 'nw', image = pebbles2)
	pebble_375 = canvas1.create_image(575, 388, anchor = 'nw', image = pebbles)

	pebble_400 = canvas1.create_image(550, 434, anchor = 'nw', image = pebbles)
	pebble_425 = canvas1.create_image(575, 434, anchor = 'nw', image = pebbles2)
	pebble_450 = canvas1.create_image(550, 458, anchor = 'nw', image = pebbles2)
	pebble_475 = canvas1.create_image(575, 458, anchor = 'nw', image = pebbles)	

	pebble_500 = canvas1.create_image(550, 504, anchor = 'nw', image = pebbles)
	pebble_525 = canvas1.create_image(575, 504, anchor = 'nw', image = pebbles2)
	pebble_550 = canvas1.create_image(550, 528, anchor = 'nw', image = pebbles2)
	pebble_575 = canvas1.create_image(575, 528, anchor = 'nw', image = pebbles)

	pebble_600 = canvas1.create_image(593, 574, anchor = 'nw', image = pebbles)
	pebble_625 = canvas1.create_image(568, 574, anchor = 'nw', image = pebbles4)
	pebble_650 = canvas1.create_image(619, 573, anchor = 'nw', image = pebbles2)
	pebble_675 = canvas1.create_image(645, 574, anchor = 'nw', image = pebbles)
	pebble_650 = canvas1.create_image(593, 598, anchor = 'nw', image = pebbles2)
	pebble_675 = canvas1.create_image(568, 598, anchor = 'nw', image = pebbles)
	pebble_600 = canvas1.create_image(619, 598, anchor = 'nw', image = pebbles4)
	pebble_625 = canvas1.create_image(645, 598, anchor = 'nw', image = pebbles2)


	pebble_700 = canvas1.create_image(636, 504, anchor = 'nw', image = pebbles2)
	pebble_725 = canvas1.create_image(661, 504, anchor = 'nw', image = pebbles)
	pebble_750 = canvas1.create_image(636, 528, anchor = 'nw', image = pebbles)
	pebble_775 = canvas1.create_image(661, 528, anchor = 'nw', image = pebbles2)

	pebble_800 = canvas1.create_image(636, 434, anchor = 'nw', image = pebbles2)
	pebble_825 = canvas1.create_image(661, 434, anchor = 'nw', image = pebbles)
	pebble_850 = canvas1.create_image(636, 458, anchor = 'nw', image = pebbles)
	pebble_875 = canvas1.create_image(661, 458, anchor = 'nw', image = pebbles2)
	
	pebble_900 = canvas1.create_image(636, 364, anchor = 'nw', image = pebbles2)
	pebble_925 = canvas1.create_image(661, 364, anchor = 'nw', image = pebbles4)
	pebble_950 = canvas1.create_image(636, 388, anchor = 'nw', image = pebbles)
	pebble_975 = canvas1.create_image(661, 388, anchor = 'nw', image = pebbles2)
	
	pebble_1000 = canvas1.create_image(636, 294, anchor = 'nw', image = pebbles2)
	pebble_1025 = canvas1.create_image(661, 294, anchor = 'nw', image = pebbles)
	pebble_1050 = canvas1.create_image(636, 318, anchor = 'nw', image = pebbles)
	pebble_1075 = canvas1.create_image(661, 318, anchor = 'nw', image = pebbles2)
	
	pebble_1100 = canvas1.create_image(636, 224, anchor = 'nw', image = pebbles2)
	pebble_1125 = canvas1.create_image(661, 224, anchor = 'nw', image = pebbles)
	pebble_1150 = canvas1.create_image(636, 248, anchor = 'nw', image = pebbles)
	pebble_1175 = canvas1.create_image(661, 248, anchor = 'nw', image = pebbles2)	

	pebble_1200 = canvas1.create_image(636, 152, anchor = 'nw', image = pebbles2)
	pebble_1225 = canvas1.create_image(661, 152, anchor = 'nw', image = pebbles)
	pebble_1250 = canvas1.create_image(636, 176, anchor = 'nw', image = pebbles)
	pebble_1275 = canvas1.create_image(661, 176, anchor = 'nw', image = pebbles2)

	pebble_1300 = canvas1.create_image(591, 84, anchor = 'nw', image = pebbles)
	pebble_1325 = canvas1.create_image(565, 84, anchor = 'nw', image = pebbles2)
	pebble_1350 = canvas1.create_image(589, 108, anchor = 'nw', image = pebbles4)
	pebble_1375 = canvas1.create_image(565, 110, anchor = 'nw', image = pebbles)
	pebble_1350 = canvas1.create_image(616, 84, anchor = 'nw', image = pebbles2)
	pebble_1375 = canvas1.create_image(642, 84, anchor = 'nw', image = pebbles4)
	pebble_1300 = canvas1.create_image(616, 108, anchor = 'nw', image = pebbles)
	pebble_1325 = canvas1.create_image(642, 108, anchor = 'nw', image = pebbles2)



	
	#counter buttons
	
	deposit0 = Button(gametab, text=n[0], padx=1, pady=0.5, bg = 'chartreuse3', command= lambda: pebble_move(0))
	deposit0_canvas = canvas1.create_window(564, 162, anchor = "nw", window=deposit0)
	deposit1 = Button(gametab, text=n[1], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(1))
	deposit1_canvas = canvas1.create_window(564, 232, anchor = "nw", window=deposit1)
	deposit2 = Button(gametab, text=n[2], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(2))
	deposit2_canvas = canvas1.create_window(564, 302, anchor = "nw", window=deposit2)
	deposit3 = Button(gametab, text=n[3], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(3))
	deposit3_canvas = canvas1.create_window(564, 372, anchor = "nw", window=deposit3)
	deposit4 = Button(gametab, text=n[4], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(4))
	deposit4_canvas = canvas1.create_window(564, 442, anchor = "nw", window=deposit4)
	deposit5= Button(gametab, text=n[5], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(5))
	deposit5_canvas = canvas1.create_window(564, 512, anchor = "nw", window=deposit5)

	deposit6 = Label(gametab, text=n[6], padx=1, pady=1, bg = 'chartreuse3')
	deposit6_canvas = canvas1.create_window(609, 588, anchor = "nw", window=deposit6)
	
	deposit7 = Button(gametab, text=n[7], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(7))
	deposit7_canvas = canvas1.create_window(650, 512, anchor = "nw", window=deposit7)
	deposit8 = Button(gametab, text=n[8], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(8))
	deposit8_canvas = canvas1.create_window(650, 442, anchor = "nw", window=deposit8)
	deposit9 = Button(gametab, text=n[9], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(9))
	deposit9_canvas = canvas1.create_window(650, 372, anchor = "nw", window=deposit9)
	deposit10 = Button(gametab, text=n[10], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(10))
	deposit10_canvas = canvas1.create_window(650, 302, anchor = "nw", window=deposit10)
	deposit11 = Button(gametab, text=n[11], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(11))
	deposit11_canvas = canvas1.create_window(650, 232, anchor = "nw", window=deposit11)
	deposit12 = Button(gametab, text=n[12], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(12))
	deposit12_canvas = canvas1.create_window(650,162, anchor = "nw", window=deposit12)
	deposit13 = Label(gametab, text=n[13], padx=1, pady=1, bg = 'chartreuse3')
	deposit13_canvas = canvas1.create_window(607, 98, anchor = "nw", window=deposit13)

	




def avalanche(): 
	global n
	global pebbles
	global pebbles2
	global pebbles4
	n=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]
	
	player = ["Player 1 (left hand side) starts", "Player 2 (right hand side) starts"]
	starter = random.choice(player)
	top= Toplevel(gametab)
	top.geometry("300x125")
	top.title("Who's turn is it? (AVALANCHE MODE)")
	Label(top, text= starter, font=('calibri 12 bold')).place(x=45,y=40)

	Player1 = True 
	
	if starter == player[0]:
		Player1 = True
		print(Player1)
	else:
		Player1 = False
		print(Player1)
	

	def pebble_move(index):
		nonlocal Player1 #must call on the nonlocal player1 as this is a nestled function
		playsound('soundeffects2.mp3')
		
		hand = n[index]
		n[index]=0

		
		lastdepositvalue = 2


#moving around the board
		while hand != 0 and index != 6 and index != 13 and lastdepositvalue > 1:
			for numberofpebbles in range(len(n)):
				if Player1 == True:
					if numberofpebbles > index: #if index1 is after indexofchosendeposit
						if hand>0:
							if numberofpebbles != 13:
								n[numberofpebbles] +=1
								print(n)
								hand=hand-1
								index = numberofpebbles
								lastdepositvalue = n[numberofpebbles]
	
				else:
					if numberofpebbles > index: #if index1 is after indexofchosendeposit
						if hand>0:
							if numberofpebbles != 6:
								n[numberofpebbles] +=1
								print(n)
								hand=hand-1
								index = numberofpebbles
								lastdepositvalue = n[numberofpebbles]
			playsound('soundeffects2.mp3') 
 


			print("No of marbles in hand: ", hand)
			while hand!=0:
				for numberofpebbles in range(len(n)):
					if hand>0:
						if Player1 == False:
							if numberofpebbles != 6:
								n[numberofpebbles] += 1
								hand = hand - 1
								print(n)
								index = numberofpebbles
								lastdepositvalue = n[numberofpebbles]
						else:
							if numberofpebbles != 13:
								n[numberofpebbles] += 1
								hand = hand - 1
								print(n)
								index = numberofpebbles
								lastdepositvalue = n[numberofpebbles]
				#playsound('soundeffects2.mp3')
			if lastdepositvalue > 1: 
				hand = lastdepositvalue
			else:
				hand = 0
			if index != 6 and index != 13 and lastdepositvalue >1:
				n[index] = 0

		deposit0.config(text = n[0])
		deposit1.config(text = n[1])
		deposit2.config(text = n[2])
		deposit3.config(text = n[3])
		deposit4.config(text = n[4])
		deposit5.config(text = n[5])
		deposit6.config(text = n[6])
		deposit7.config(text = n[7])
		deposit8.config(text = n[8])
		deposit9.config(text = n[9])
		deposit10.config(text = n[10])
		deposit11.config(text = n[11])
		deposit12.config(text = n[12])
		deposit13.config(text = n[13])


#changing form player 1 to 2 or vice versa			
		if Player1 == True:
			Player1 = False
		else:
			Player1 = True
		print(Player1)




		deposit0.config(text = n[0])
		deposit1.config(text = n[1])
		deposit2.config(text = n[2])
		deposit3.config(text = n[3])
		deposit4.config(text = n[4])
		deposit5.config(text = n[5])
		deposit6.config(text = n[6])
		deposit7.config(text = n[7])
		deposit8.config(text = n[8])
		deposit9.config(text = n[9])
		deposit10.config(text = n[10])
		deposit11.config(text = n[11])
		deposit12.config(text = n[12])
		deposit13.config(text = n[13])

		
	#disabling and enabling buttons	
		if Player1 == True:
			deposit0.config(state=NORMAL)
			deposit1.config(state = NORMAL)
			deposit2.config(state = NORMAL)
			deposit3.config(state = NORMAL)
			deposit4.config(state = NORMAL)
			deposit5.config(state = NORMAL)                   
			deposit7.config(state = DISABLED)
			deposit8.config(state = DISABLED)
			deposit9.config(state = DISABLED)
			deposit10.config(state = DISABLED)
			deposit11.config(state = DISABLED)
			deposit12.config(state = DISABLED)

		else:
			deposit0.config(state = DISABLED)
			deposit1.config(state = DISABLED)
			deposit2.config(state = DISABLED)
			deposit3.config(state = DISABLED)
			deposit4.config(state = DISABLED)
			deposit5.config(state = DISABLED)
			deposit7.config(state = NORMAL)
			deposit8.config(state = NORMAL)
			deposit9.config(state = NORMAL)
			deposit10.config(state = NORMAL)
			deposit11.config(state = NORMAL)
			deposit12.config(state = NORMAL)


#declaring a winner
		leftover = 0
		for i in range(6):
			if n[i] >0:
				leftover +=1
			else:
				leftover = leftover
		if leftover == 0:
			print("Gameover. Player 1 is out of marbles")
			for i in range(len(n)):
				if i > 6 and i !=13:
					n[13] = n[i] + n[13]
					n[i] = 0
			deposit0.config(state = DISABLED)
			deposit1.config(state = DISABLED)
			deposit2.config(state = DISABLED)
			deposit3.config(state = DISABLED)
			deposit4.config(state = DISABLED)
			deposit5.config(state = DISABLED)
			deposit7.config(state = DISABLED)
			deposit8.config(state = DISABLED)
			deposit9.config(state = DISABLED)
			deposit10.config(state = DISABLED)
			deposit11.config(state = DISABLED)
			deposit12.config(state = DISABLED)

			if n[13]> n[6]:
				winner = "Player 2 won! "
			elif n[13]<n[6]:
				winner = "Player 1 won!"
			else:
				winner = "It's a tie!"

			top= Toplevel(gametab)
			top.geometry("300x125")
			top.title("Who won?")
			Label(top, text= winner, font=('calibri 12 bold')).place(x=45,y=40)
			print(n)

		leftover2 = 0
		for i in range(7,13):
			if n[i] >0:
				leftover2 +=1
			else:
				leftover2= leftover2
		if leftover2 ==0:
			print("Gameover, player 2 is out of marbles")
			for i in range(len(n)):
				if i<6:
					n[6] = n[6] + n[i]
					n[i] = 0
			deposit0.config(state = DISABLED)
			deposit1.config(state = DISABLED)
			deposit2.config(state = DISABLED)
			deposit3.config(state = DISABLED)
			deposit4.config(state = DISABLED)
			deposit5.config(state = DISABLED)
			deposit7.config(state = DISABLED)
			deposit8.config(state = DISABLED)
			deposit9.config(state = DISABLED)
			deposit10.config(state = DISABLED)
			deposit11.config(state = DISABLED)
			deposit12.config(state = DISABLED)

			if n[13]> n[6]:
				winner = "Player 2 won! "
			elif n[13]<n[6]:
				winner = "Player 1 won!"
			else:
				winner = "It's a tie!"

			top= Toplevel(gametab)
			top.geometry("300x125")
			top.title("Who won?")
			Label(top, text= winner, font=('calibri 12 bold')).place(x=45,y=40)
			print(n)

		

		deposit0.config(text = n[0])
		deposit1.config(text = n[1])
		deposit2.config(text = n[2])
		deposit3.config(text = n[3])
		deposit4.config(text = n[4])
		deposit5.config(text = n[5])
		deposit6.config(text = n[6])
		deposit7.config(text = n[7])
		deposit8.config(text = n[8])
		deposit9.config(text = n[9])
		deposit10.config(text = n[10])
		deposit11.config(text = n[11])
		deposit12.config(text = n[12])
		deposit13.config(text = n[13])


#adding pebble files to code
	pebbles = ImageTk.PhotoImage(file="marbletry2.png")
	pebbles2 = ImageTk.PhotoImage(file="marbletry5.png")
	pebbles3 = ImageTk.PhotoImage(file="marble6.png")
	pebbles4 = ImageTk.PhotoImage(file="marble4.png")


#adding pebble images
	pebble_000 = canvas1.create_image(550, 152, anchor = 'nw', image = pebbles)
	pebble_025 = canvas1.create_image(575, 152, anchor = 'nw', image = pebbles2)
	pebble_050 = canvas1.create_image(550, 176, anchor = 'nw', image = pebbles2)
	pebble_075 = canvas1.create_image(575, 176, anchor = 'nw', image = pebbles)


	pebble_100 = canvas1.create_image(550, 224, anchor = 'nw', image = pebbles)
	pebble_125 = canvas1.create_image(575, 224, anchor = 'nw', image = pebbles2)
	pebble_150 = canvas1.create_image(550, 248, anchor = 'nw', image = pebbles2)
	pebble_175 = canvas1.create_image(575, 248, anchor = 'nw', image = pebbles)


	pebble_200 = canvas1.create_image(550, 294, anchor = 'nw', image = pebbles)
	pebble_225 = canvas1.create_image(575, 294, anchor = 'nw', image = pebbles2)
	pebble_250 = canvas1.create_image(550, 318, anchor = 'nw', image = pebbles4)
	pebble_275 = canvas1.create_image(575, 318, anchor = 'nw', image = pebbles)

	pebble_300 = canvas1.create_image(550, 364, anchor = 'nw', image = pebbles)
	pebble_325 = canvas1.create_image(575, 364, anchor = 'nw', image = pebbles2)
	pebble_350 = canvas1.create_image(550, 388, anchor = 'nw', image = pebbles2)
	pebble_375 = canvas1.create_image(575, 388, anchor = 'nw', image = pebbles)

	pebble_400 = canvas1.create_image(550, 434, anchor = 'nw', image = pebbles)
	pebble_425 = canvas1.create_image(575, 434, anchor = 'nw', image = pebbles2)
	pebble_450 = canvas1.create_image(550, 458, anchor = 'nw', image = pebbles2)
	pebble_475 = canvas1.create_image(575, 458, anchor = 'nw', image = pebbles)	

	pebble_500 = canvas1.create_image(550, 504, anchor = 'nw', image = pebbles)
	pebble_525 = canvas1.create_image(575, 504, anchor = 'nw', image = pebbles2)
	pebble_550 = canvas1.create_image(550, 528, anchor = 'nw', image = pebbles2)
	pebble_575 = canvas1.create_image(575, 528, anchor = 'nw', image = pebbles)

	pebble_600 = canvas1.create_image(593, 574, anchor = 'nw', image = pebbles)
	pebble_625 = canvas1.create_image(568, 574, anchor = 'nw', image = pebbles4)
	pebble_650 = canvas1.create_image(619, 573, anchor = 'nw', image = pebbles2)
	pebble_675 = canvas1.create_image(645, 574, anchor = 'nw', image = pebbles)
	pebble_650 = canvas1.create_image(593, 598, anchor = 'nw', image = pebbles2)
	pebble_675 = canvas1.create_image(568, 598, anchor = 'nw', image = pebbles)
	pebble_600 = canvas1.create_image(619, 598, anchor = 'nw', image = pebbles4)
	pebble_625 = canvas1.create_image(645, 598, anchor = 'nw', image = pebbles2)


	pebble_700 = canvas1.create_image(636, 504, anchor = 'nw', image = pebbles2)
	pebble_725 = canvas1.create_image(661, 504, anchor = 'nw', image = pebbles)
	pebble_750 = canvas1.create_image(636, 528, anchor = 'nw', image = pebbles)
	pebble_775 = canvas1.create_image(661, 528, anchor = 'nw', image = pebbles2)

	pebble_800 = canvas1.create_image(636, 434, anchor = 'nw', image = pebbles2)
	pebble_825 = canvas1.create_image(661, 434, anchor = 'nw', image = pebbles)
	pebble_850 = canvas1.create_image(636, 458, anchor = 'nw', image = pebbles)
	pebble_875 = canvas1.create_image(661, 458, anchor = 'nw', image = pebbles2)
	
	pebble_900 = canvas1.create_image(636, 364, anchor = 'nw', image = pebbles2)
	pebble_925 = canvas1.create_image(661, 364, anchor = 'nw', image = pebbles4)
	pebble_950 = canvas1.create_image(636, 388, anchor = 'nw', image = pebbles)
	pebble_975 = canvas1.create_image(661, 388, anchor = 'nw', image = pebbles2)
	
	pebble_1000 = canvas1.create_image(636, 294, anchor = 'nw', image = pebbles2)
	pebble_1025 = canvas1.create_image(661, 294, anchor = 'nw', image = pebbles)
	pebble_1050 = canvas1.create_image(636, 318, anchor = 'nw', image = pebbles)
	pebble_1075 = canvas1.create_image(661, 318, anchor = 'nw', image = pebbles2)
	
	pebble_1100 = canvas1.create_image(636, 224, anchor = 'nw', image = pebbles2)
	pebble_1125 = canvas1.create_image(661, 224, anchor = 'nw', image = pebbles)
	pebble_1150 = canvas1.create_image(636, 248, anchor = 'nw', image = pebbles)
	pebble_1175 = canvas1.create_image(661, 248, anchor = 'nw', image = pebbles2)	

	pebble_1200 = canvas1.create_image(636, 152, anchor = 'nw', image = pebbles2)
	pebble_1225 = canvas1.create_image(661, 152, anchor = 'nw', image = pebbles)
	pebble_1250 = canvas1.create_image(636, 176, anchor = 'nw', image = pebbles)
	pebble_1275 = canvas1.create_image(661, 176, anchor = 'nw', image = pebbles2)

	pebble_1300 = canvas1.create_image(591, 84, anchor = 'nw', image = pebbles)
	pebble_1325 = canvas1.create_image(565, 84, anchor = 'nw', image = pebbles2)
	pebble_1350 = canvas1.create_image(589, 108, anchor = 'nw', image = pebbles4)
	pebble_1375 = canvas1.create_image(565, 110, anchor = 'nw', image = pebbles)
	pebble_1350 = canvas1.create_image(616, 84, anchor = 'nw', image = pebbles2)
	pebble_1375 = canvas1.create_image(642, 84, anchor = 'nw', image = pebbles4)
	pebble_1300 = canvas1.create_image(616, 108, anchor = 'nw', image = pebbles)
	pebble_1325 = canvas1.create_image(642, 108, anchor = 'nw', image = pebbles2)




	#counter buttons
	
	deposit0 = Button(gametab, text=n[0], padx=1, pady=0.5, bg = 'chartreuse3', command= lambda: pebble_move(0))
	deposit0_canvas = canvas1.create_window(564, 162, anchor = "nw", window=deposit0)
	deposit1 = Button(gametab, text=n[1], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(1))
	deposit1_canvas = canvas1.create_window(564, 232, anchor = "nw", window=deposit1)
	deposit2 = Button(gametab, text=n[2], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(2))
	deposit2_canvas = canvas1.create_window(564, 302, anchor = "nw", window=deposit2)
	deposit3 = Button(gametab, text=n[3], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(3))
	deposit3_canvas = canvas1.create_window(564, 372, anchor = "nw", window=deposit3)
	deposit4 = Button(gametab, text=n[4], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(4))
	deposit4_canvas = canvas1.create_window(564, 442, anchor = "nw", window=deposit4)
	deposit5= Button(gametab, text=n[5], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(5))
	deposit5_canvas = canvas1.create_window(564, 512, anchor = "nw", window=deposit5)

	deposit6 = Label(gametab, text=n[6], padx=1, pady=1, bg = 'chartreuse3')
	deposit6_canvas = canvas1.create_window(609, 588, anchor = "nw", window=deposit6)
	
	deposit7 = Button(gametab, text=n[7], padx=1, pady=1, bg = 'chartreuse3', command= lambda: pebble_move(7))
	deposit7_canvas = canvas1.create_window(650, 512, anchor = "nw", window=deposit7)
	deposit8 = Button(gametab, text=n[8], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(8))
	deposit8_canvas = canvas1.create_window(650, 442, anchor = "nw", window=deposit8)
	deposit9 = Button(gametab, text=n[9], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(9))
	deposit9_canvas = canvas1.create_window(650, 372, anchor = "nw", window=deposit9)
	deposit10 = Button(gametab, text=n[10], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(10))
	deposit10_canvas = canvas1.create_window(650, 302, anchor = "nw", window=deposit10)
	deposit11 = Button(gametab, text=n[11], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(11))
	deposit11_canvas = canvas1.create_window(650, 232, anchor = "nw", window=deposit11)
	deposit12 = Button(gametab, text=n[12], padx=1, pady=1, bg = 'chartreuse3',command= lambda: pebble_move(12))
	deposit12_canvas = canvas1.create_window(650,162, anchor = "nw", window=deposit12)
	deposit13 = Label(gametab, text=n[13], padx=1, pady=1, bg = 'chartreuse3')
	deposit13_canvas = canvas1.create_window(607, 98, anchor = "nw", window=deposit13)









regulargame()
gametab.mainloop()
