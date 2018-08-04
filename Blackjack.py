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
CARD_POS = [80, 200]
CARD_SPACE = [30, 80]
in_play = False
outcome = ""
score = 0
message = "Hit or Stand ?"

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
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand_list = []

    def __str__(self):
        # return a string representation of a hand
        hand_str = ""
        for i in range(len(self.hand_list)):
            hand_str += str(self.hand_list[i]) + " "
        return "Hand contains " + hand_str

    def add_card(self, card):
        # add a card object to a hand
        self.hand_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        ace = True
        hand_value = 0
        for card in self.hand_list:
            if card.get_rank() == RANKS[0]:
                ace = False
            hand_value += VALUES[card.get_rank()]
        if ace :
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
                
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.hand_list)):
            self.hand_list[i].draw(canvas, [pos[0] + i * (CARD_SIZE[0] + CARD_SPACE[0]),
                                    pos[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_list = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck_list.append(Card(SUITS[i], RANKS[j]))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.deck_list)

    def deal_card(self):
        # deal a card object from the deck
        deal = self.deck_list[-1]
        self.deck_list.remove(deal)
        return deal
    
    def __str__(self):
        # return a string representing the deck
        deck_str = ""
        for i in range(len(self.deck_list)):
            deck_str += str(self.deck_list[i]) + " " 
        return "Deck contains " + deck_str


#define event handlers for buttons
def deal():
    global outcome, message, in_play, deck, player_hand, dealer_hand, score
    if in_play:
        outcome = "You quit the game and lose."
        message = "Hit or Stand ?"
        score -= 1
    else:
        deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
    # your code goes here
        deck.shuffle()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
        in_play = True
        outcome = ""
        message = "Hit or Stand ?"

def hit():
    # replace with your code below
    global in_play, message, outcome, score
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
    if in_play:
        player_hand.add_card(deck.deal_card())
        if player_hand.get_value() > 21:
            in_play = False
            outcome = "You went bust and lose."
            message = "New deal?"
            score -= 1
         
def stand():
    # replace with your code below
    global message, outcome, score, in_play
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer went bust and you win!"
            message = "New deal?"
            score += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            outcome = "You lose."
            message = "New deal?"
            score -= 1
        else:
            outcome = "You win!"
            message = "New deal?"
            score += 1
        in_play = False

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", [150, 75], 40, "aqua")
    canvas.draw_text("Dealer", [75, 180], 25, "black")
    canvas.draw_text("Player", [75, 360], 25, "balck")
    canvas.draw_text("Score "+ str(score), [400, 120], 30, "black")
    canvas.draw_text(outcome, [190, 180], 25, "black")
    canvas.draw_text(message, [190, 360], 25, "black")
    if in_play: 
        dealer_hand.draw(canvas, CARD_POS)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, 
                          [CARD_POS[0] + CARD_BACK_CENTER[0], CARD_POS[1] + CARD_BACK_CENTER[1]],
                           CARD_BACK_SIZE)
    else:
        dealer_hand.draw(canvas, CARD_POS)
    player_hand.draw(canvas, [CARD_POS[0], CARD_POS[1] + CARD_SIZE[1] + CARD_SPACE[1]])

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


# remember to review the gradic rubric