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
---------------------
>>>

import random
 
for i in range(10):
    print(random.randint(1,100))
    
print('----------')
 
number1 = random.randint(1,100)
print("The first generated number is %d" %(number1))
 
counter = 1
number2 = random.randint(1,100)
 
while number1 != number2:
    counter+=1
    number2=random.randint(1,100)
    print(counter, number2)
    
print("I needed %d attempts to generate %d again" % (counter, number1))
 
print('----------')
 
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
 
random.shuffle(countries)
 
groupNumber = 0
 
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])
math_ls = dir(math) 
print(math_ls)

>>>>

55
18
21
72
53
64
27
34
16
79
----------
The first generated number is 52
2 97
3 29
4 76
5 8
6 87
7 28
8 73
9 39
10 72
11 77
12 47
13 72
14 89
15 68
16 23
17 3
18 41
19 99
20 39
21 15
22 10
23 2
24 56
25 53
26 75
27 66
28 14
29 76
30 16
31 59
32 28
33 66
34 77
35 60
36 46
37 46
38 70
39 2
40 10
41 36
42 18
43 27
44 31
45 18
46 47
47 88
48 100
49 28
50 66
51 56
52 13
53 78
54 52
I needed 54 attempts to generate 52 again
----------
========== Group 1 ==========
Serbia
Colombia
Brazil
Germany
========== Group 2 ==========
Russia
Iceland
Nigeria
Switzerland
========== Group 3 ==========
Portugal
Peru
Morocco
Argentina
========== Group 4 ==========
Japan
Iran
Panama
Tunisia
========== Group 5 ==========
England
Egypt
Korea Republic
Mexico
========== Group 6 ==========
Poland
Senegal
Costa Rica
Saudi Arabia
========== Group 7 ==========
Belgium
Australia
France
Uruguay
========== Group 8 ==========
Croatia
Sweden
Denmark
Spain

>>>>>>>>>
73
77
47
99
76
19
32
60
10
28
----------
The first generated number is 13
2 47
3 83
4 52
5 3
6 44
7 38
8 13
I needed 8 attempts to generate 13 again
----------
========== Group 1 ==========
Mexico
Senegal
Spain
Iran
========== Group 2 ==========
Serbia
Poland
Portugal
Brazil
========== Group 3 ==========
Colombia
Germany
Peru
France
========== Group 4 ==========
Belgium
Russia
Sweden
Iceland
========== Group 5 ==========
Croatia
Egypt
Costa Rica
Panama
========== Group 6 ==========
Denmark
Japan
Argentina
Tunisia
========== Group 7 ==========
Saudi Arabia
Korea Republic
England
Morocco
========== Group 8 ==========
Nigeria
Australia
Switzerland
Uruguay
>>>>

import random
 
min = 1
max = 6
 
dice = random.randint(min,max)
 
if dice == 1:
    print('   ')
    print(' o ')
    print('   ')
elif dice == 2:
    print('  o')
    print('   ')
    print('o  ')
elif dice == 3:
    print('  o')
    print(' o ')
    print('o  ')
elif dice == 4:
    print('o o')
    print('   ')
    print('o o')
elif dice == 5:
    print('o o')
    print(' o ')
    print('o o')
else:
    print('o o')
    print('o o')
    print('o o')
 
print('----------------------')
 
dices = []
for i in range(5):
    dices.append(random.randint(min,max))
 
dices.sort()
print(dices)

>>>

o o
o o
o o
----------------------
[2, 3, 4, 5, 6]
>>> 
============== RESTART:  ==============
   
 o 
   
----------------------
[1, 5, 5, 6, 6]
>>> 
============== RESTART:  ==============
o o
   
o o
----------------------
[1, 1, 2, 3, 4]
>>> 
==============  ==============
o o
 o 
o o
----------------------
[2, 2, 5, 6, 6]
>>> 

import random

liczby = range(33, 124)
haslo = ""

for i in range(15):
    haslo += chr(random.choice(liczby))

print("Hasło: ", haslo)

>>>>
Hasło:  JYDU)f]Y#&u{.6&
>>> 
