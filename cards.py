"""
random module currently used for the shuffleing purpose
"""
import random

#CREATING A CARDS IN CARD WAR GAME
#CREATING A LIST OF SUITS

suits = ["Hearts","Daimonds","Spades","Clubs"]

#CREATING A LIST OF RANKS CARDS
list_of_rank = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen",
"King","Ace"]

#CREATING A DECTNORY TO CONVERT RANKS INTO INTEGER VALUES FOR COMPARISION BETWEEN CARDS
value = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,
"Jack":11,"Queen":12,"King":13,"Ace":14}

class Cards:
    """
    This class creates an cards
    """
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        #converts string ranks to integer values
        self.value = value[rank]

    def __str__(self):
        #returns string of a card
        return self.rank + " of " + self.suit

four_of_spades = Cards("Spades","Four")
eight_of_hearts = Cards("Hearts","Eight")

# CREATING AN DECK OF CARDS
class Deck:
    """
    this class defines to create a deck of cards,shuffel the cards,deal only with one card
    """
    def __init__(self):
        #cards were added to this list
        self.all_cards = []
        for suit in suits:
            for rank in list_of_rank:
                card = Cards(suit,rank)
                self.all_cards.append(card)

    def shuffle(self):
        """
        shuffleing the deck of all 52 cards
        """
        random.shuffle(self.all_cards)

    def deal_with_one(self):
        """
        the below method now deals with only one card
        that dituributes first card
        """
        return self.all_cards.pop(0)
    
#Creating an players class

class Player:
    """
    this class contains how many cards does a player had,removing the card,adding the cards 
    """

    def __init__(self,player_name):

        self.player_name = player_name
        self.all_cards = []

    def remov_card(self):
        self.show = 0
        """
        removes the first card form the player
        """
        return self.all_cards.pop(0)

    def adding_card(self,new_card):
        """
        adding cards for the player
        """
        # this is for list of cards
        if type(new_card) == type([]):
            self.all_cards.extend(new_card)
        else:
        #this is for single card
            self.all_cards.append(new_card)

    def __str__(self):

        return f"player {self.player_name} has {len(self.all_cards)} no of cards"

#BUILDING THE GAME LOGIC STARTS HERE...
    #set uping the game
player1 = Player("Akhi")
player2 = Player("Bittu")

new_deck = Deck()
new_deck.shuffle()

#sharing each cards to both the players

for i in range(26):
    player1.adding_card(new_deck.deal_with_one())
    player2.adding_card(new_deck.deal_with_one())

Game_on = True
round = 0
while Game_on:

    round += 1
    print(f"     Round No: {round}     ")

    if len(player1.all_cards) == 0:
        print("Player 1 has 0 number of cards")
        print("Player 2 won the game!")
        Game_on = False
    elif len(player2.all_cards) == 0:
        print("Player 2 has 0 number of cards")
        print("Player 1 won the game!")
        Game_on = False
    
    if len(player1.all_cards) > 0 and len(player2.all_cards) > 0:
        p1Card = player1.remov_card()
        p2Card = player2.remov_card()

    if p1Card.value < p2Card.value:
        #taking players1 card
        #and taking our card coz we removed it
        player2.adding_card(p2Card)
        player2.adding_card(p1Card)
    elif p1Card.value > p2Card.value:
        player1.adding_card(p1Card)
        player1.adding_card(p2Card)
    elif p1Card.value == p2Card.value:
        war = True
        while war:
            print("          WAR          ")
            if len(player1.all_cards) < 5:
                #need to check this again
                print("Player 1 has no suffecient cards..")
                print("Player 2 won the game!")
                war = False
                Game_on = False
            elif len(player2.all_cards) < 5:
                #this was working perfect
                print("Player 2 has no suffecient cards..")
                print("Player 1 won the game!")
                war = False
                Game_on = False
            else:
                take5_p1 = []
                take5_p2 = []
                for i in range(5):
                    take5_p1.append(player1.remov_card())
                    take5_p2.append(player2.remov_card())
                if take5_p1[0].value < take5_p2[0].value:
                    player2.adding_card(take5_p2)
                    player2.adding_card(take5_p1)
                    war = False
                elif take5_p1[0].value > take5_p2[0].value:
                    player1.adding_card(take5_p1)
                    player1.adding_card(take5_p2)
                    war = False