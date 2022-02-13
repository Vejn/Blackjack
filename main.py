# Pycharm Blackjack
import random
from black_classes import Deck, Chips, Card, Hand

# Global variable PLAY
PLAY = True

# Defining functions for the game
def take_bet(chips):

    while True:

        # Using Try/Except in case user provides invalid input
        try:
            chips.bet = int(input("How many chips would you like to bet?: "))
        except ValueError:
            print("Bet must be an Integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, you can't bet more than you have!")
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):

    global PLAY    # To control upcoming while loop

    while True:
        h_or_s = input("Would you like to Hit or Stand?(h/s) ")

        if h_or_s[0].lower() == "h":
            hit(deck, hand)

        elif h_or_s[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            PLAY = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print("<card hidden>")
    print("",dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep="\n")    # * used to show all items in collection


def show_all(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep="\n")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep="\n")
    print("Player's Hand =", player.vale)


def player_busts(player, dealer, chips):
    print("Player Busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer Busts!")
    chips.win_bet()


def dealer_wins():
    print("Dealer Wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Player and Dealer tie! It's a Push!")


# Main function

while True:
    # Printing welcome message
    print("Welcome to BlackJack! Let's Play!")

    # Creating and mixing the deck
    deck = Deck()
    deck.shuffle()

    # Creating player and adding 2 cards
    player = Hand()
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    # Creating dealer and adding 2 cards
    dealer = Hand()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    # Creating player chips with amount of 250
    player_chips = Chips(250)

    # Asking player for the bet
    take_bet(player_chips)

    # Showing initial cards
    show_some(player, dealer)

    while PLAY:
        # Asking if the player wants to hit or stand
        hit_or_stand(deck, player)
        # Showing the cards again
        show_some(player, dealer)
        # Checking the score
        if player.value > 21:
            player_busts(player, dealer, player_chips)
            break

    if player.value <= 21:

        while dealer.value < 17:
            hit(deck, dealer)

        show_all(player, dealer)

        if dealer.value > 21:
            dealer_busts(player, dealer, player_chips)

        elif dealer.value > player.value:
            dealer_wins(player, dealer, player_chips)

        elif dealer.value < player.value:
            player_wins(player, dealer, player_chips)

        else:
            push(player, dealer)


    print("\nPlayer's chips stand at: ",player_chips.total)

    new_game = input("Would you like to play another hand? 'y' or 'n'?: ")

    if new_game[0].lower() == 'y':
        PLAY = True
        continue
    else:
        print("Thanks for playing!")
        break
