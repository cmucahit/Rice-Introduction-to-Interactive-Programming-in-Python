# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
prompt = "Hit or stand?"
score = 0
TITLE_POS = [100, 100]
SCORE_POS = [400, 100]
DEALER_TEXT_POS = [73, 176]
PLAYER_TEXT_POS = [73, 372]
PROMPT_POS = [200 , 372]
OUTCOME_POS = [200, 176]

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def drawback(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + " "
        return s
    
    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        count_aces = 0
        for c in self.cards:
            hand_value += VALUES.get(c.get_rank())
            if c.get_rank() == 'A':
                count_aces += 1
        if count_aces == 0:
            return hand_value
        else:
            if hand_value + 10 <= 21:	 
                return hand_value + 10
            else:
                return hand_value
        
    def draw(self, canvas, pos):
        
        # draw a hand on the canvas, use the draw method for cards
        i = 0
        
        for card in self.cards:
            card.draw(canvas, [pos[0]+i*1.3*CARD_SIZE[0], pos[1]])
            i += 1
            
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
             

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop(0)
    
    def __str__(self):
        # return a string representing the deck
        s = ""
        for i in range(len(self.cards)):
            s += str(self.cards[i]) + " "
        return s

#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global my_deck, my_hand, dealer_hand
    
    if in_play == False:
        in_play = True
        outcome = ""
        my_deck = Deck()
        my_deck.shuffle()
    
        my_hand = Hand()
        dealer_hand = Hand()
    
        for i in range (0,2):
            my_hand.add_card(my_deck.deal_card())
            dealer_hand.add_card(my_deck.deal_card())
    
        in_play == True
            
    elif in_play == True:
        outcome = "Deal in middle of round. You lose."  
        in_play = False
        score -=1

def hit():
    global outcome, in_play, score
    
    
    # if the hand is in play, hit the player
    if in_play == True:
        if my_hand.get_value() <= 21:
            my_hand.add_card(my_deck.deal_card())
    
        # if busted, assign a message to outcome, update in_play and score
        if my_hand.get_value() > 21:
            outcome = "You went bust and lose."
            in_play = False
            score -= 1
    else:
        pass
        
def stand():
    global outcome, in_play, score
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play == True: 
        if my_hand.get_value() > 21:
            outcome = "You went bust already."
            in_play = False
        else:
            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(my_deck.deal_card())
        
        if dealer_hand.get_value() > 21:
            in_play = False
            outcome = "Dealer went bust. You win."
            score += 1
        else:
            if my_hand.get_value() <= dealer_hand.get_value():
                in_play = False
                outcome = "You lose."
                score -= 1
            else: 
                in_play = False
                outcome = "You win."
                score += 1
    else:
        pass
        
# draw handler    
def draw(canvas):
    global in_play
    
    canvas.draw_text("Blackjack", TITLE_POS, 36, "Blue", "sans-serif")
    canvas.draw_text("Dealer", DEALER_TEXT_POS, 26, "Black", "sans-serif")
    canvas.draw_text("Player", PLAYER_TEXT_POS, 26, "Black", "sans-serif")
    #canvas.draw_text(prompt, PROMPT_POS, 26, "Black", "sans-serif")
    canvas.draw_text(outcome, OUTCOME_POS, 26, "Black", "sans-serif")
    canvas.draw_text("Score " + str(score), SCORE_POS, 26, "Black", "sans-serif")

    if in_play == True:
        canvas.draw_text("Hit or stand?", PROMPT_POS, 26, "Black", "sans-serif")
    else: 
        canvas.draw_text("New deal?", PROMPT_POS, 26, "Black", "sans-serif")
    
    dealer_hand.draw(canvas, [CARD_SIZE[0],2*CARD_SIZE[1]])
    
    card = Card("S", "A")
    if in_play == True:
        card.drawback(canvas, [CARD_SIZE[0],2*CARD_SIZE[1]])
    
    my_hand.draw(canvas, [CARD_SIZE[0],4*CARD_SIZE[1]])
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
