# Module for deck and other classes
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
    'Queen': 10, 'King': 10, 'Ace': 11
}


# Creating Card Class
class Card:
    # Initializing card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    # String representation of the card
    def __str__(self):
        return self.rank + "of" + self.suit


# Creating Deck Class
class Deck:
    # Initializing Deck
    def __init__(self):
        self.deck = []    # starting with empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))    # building card objects and adding them to the list

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

    # Shuffling the deck
    def shuffle(self):
        random.shuffle(self.deck)

    # Dealing the card
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0    # Attribute to track aces, we need it to adjust score accordingly

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":    # If the card is Ace, we add 1 to self.aces
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:    # If the value of player hand is greater than 21 and there is an Ace
            self.value -= 10    # We remove 10 from the score
            self.aces -= 1      # And we remove Ace from self aces


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet
