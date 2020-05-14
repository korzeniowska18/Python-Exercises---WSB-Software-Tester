#!/usr/bin/python3
# -*- coding: utf-8 -*-



import random

print("I have for you some game with magic cards. Cards from this list will be shuffled.")

print("You can take the last card")

print('If your last card will be "Joker" you will be the Winner!') 

print("Lets Gooo!")

card_List = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace"
            "Joker", "Joker"]


random.shuffle(card_List)

print(card_List)

Last_Card = (card_List[-1])

print("Last card is: " + Last_Card)

Winner_Card = "Joker"

Near_Card_with_last = (card_List[-2])

if Last_Card == Winner_Card:
    print("WOW! **** You are the Winner! **** ")

elif Near_Card_with_last == Winner_Card:
    print("You are so near but please try again. Don't worry! Please smile!")

else:
    print("I'm so sorry!... This is not the Winner Card!")
    print("Please try again.")
