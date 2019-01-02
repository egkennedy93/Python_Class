import random
import time
suits = ('Diamonds', 'Hearts', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ' '
        for i in self.deck:
            deck_comp += '\n' + i.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        deal_card = self.deck.pop()
        return deal_card


class Hand:

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        pass

    def __str__(self):
        return " The hand contains " + str(self.cards)

def hit(deck, hand):
    new_card = list(deck).pop()
    hand.append(new_card)
    print("adding card " + str(new_card) + " to the player hand " + str(hand))


ready_to_play = input("Welcome to Blackjack, are you ready to play? (Yes|No)").upper()
if ready_to_play == "YES":
    print("Starting the game")
    new_deck = Deck()
    dealer = Hand()
    player = Hand()

    while True:
        try:
            print("\n"*100)
            print("Shuffling the deck...")
            time.sleep(1)
            new_deck.shuffle()
            print("Dealing out the hands ")
            player.add_card(new_deck.deal())
            dealer.add_card(new_deck.deal())
            player.add_card(new_deck.deal())
            dealer.add_card(new_deck.deal())
            print(player.cards)
            player.value = values[player.cards[0][1]] + values[player.cards[1][1]]
            dealer.value = values[dealer.cards[0][1]] + values[dealer.cards[1][1]]
            if str(player.cards[0][1]).upper() == "ACE" or str(player.cards[1][1]).upper() == "ACE":
                player.aces += 1
            if str(dealer.cards[0][1]).upper() == "ACE" or str(dealer.cards[1][1]).upper() == "ACE":
                dealer.aces += 1
            # Checking the dealers dealt hand this will determine what the dealer does
            if dealer.value == 21:
                print("Dealer has blackjack. You lose!")
                break
        except IndexError:
            print("There was an error when trying to shuffle and deal the cards, deck might be empty?")
            break
        break
    while playing:
        player_option = input("What do you want to do? \n hit|stay|raise|show hand").upper()
        if player_option == "HIT":
            hit(new_deck.deck, player.cards)
            continue
        if player_option == "STAY":
            pass
        if player_option == "RAISE":
            pass
        if player_option == "SHOW HAND":
            print("\n"*100)
            print(str(player.cards))
        else:
            break

elif ready_to_play == "NO":
    print("Thank you for playing")
else:
    print("Sorry that isn't a valid response. Please enter Yes or No")

