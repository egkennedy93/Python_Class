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

    def __str__(self):
        new_card = ' '
        for i in self.cards:
            new_card += " " + i
        return " The hand contains:" + str(new_card)

    def add_card(self, card):
        self.cards.append(card.__str__())
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def __str__(self):
        return " The total is " + str(self.total)

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet
        if self.total == 0:
            print("You have ran out of money. Thank you for playing")
            quit()


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    #print("adding card " + str(single_card) + " to the hand " + str(hand))


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("there was an error taking your bet")
        else:
            if chips.bet > chips.total:
                print("sorry you don't have enough chips! You have: {}".format(chips.total))
            else:
                break


def hit_or_stand(deck, hand):
    global playing
    pass






ready_to_play = input("Welcome to Blackjack, are you ready to play? (Yes|No)").upper()
if ready_to_play == "YES":
    print("Starting the game")
    new_deck = Deck()
    dealer = Hand()
    player = Hand()
    new_deck.shuffle()
    player.add_card(new_deck.deal())
    #player_chips = Chips()
    #hit(new_deck, player)
   # while True:
   #     print("\n"*100)
   #     print("Shuffling the deck...")
   #     time.sleep(1)
   #     new_deck.shuffle()
   #     print(new_deck)
   #     print("Dealing out the hands ")
   #     player.add_card(new_deck.deal())
   #     print(player.value)
   #     print(player.cards[0])
   #     player_chips.bet = 100
   #     take_bet(player_chips)

       # print(player_chips)
       # break








