# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global state
    state = 0
    global deck
    global exposed
    global prev1
    global prev2
    global turns 
    turns = 1
    
    deck_a = []
    deck_b = []
    for i in range(0,8):
        deck_a.append(i)
        deck_b.append(i)
    
    deck = deck_a + deck_b
    random.shuffle(deck)
    
    exposed = []
    for x in range(0, len(deck)):
        exposed.append("False")
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global prev1
    global prev2
    global turns
    label.set_text("Turns = " + str(turns))
    
    # flip card
    card_index = int(pos[0]/50)
    
    if exposed[card_index] == "False":
        exposed[card_index] = "True"
    
        if state == 0:
            state = 1
            prev1 = card_index
        elif state == 1:
            state = 2
            prev2 = card_index

        # state 2, check if cards are paired
        else:
            state = 1
            turns += 1

            if deck[prev1] == deck[prev2]:
                prev1 = card_index
            else:
                exposed[prev1] = "False"
                exposed[prev2] = "False"
                prev1 = card_index
                    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0,len(deck)):
        if exposed[i] == "True":
            canvas.draw_text(str(deck[i]),[15+50*i,60], 24, "White")
        else:
            canvas.draw_line((i*50+25,0),(i*50+25,100),50,'Blue')
            canvas.draw_line((i*50+25,0),(i*50+25,100),48,'Green')
          
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

