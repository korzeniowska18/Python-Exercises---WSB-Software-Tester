import random

print(random.random())

prog = random.randrange(8) #wypisuje liczby w zakresie do 8

print(prog)

if prog == 0:
    print("ZERO")
else:
    print("LOSOWA LICZBA")
    
print("Twoja liczba losowa z zakresu liczb od 1 do 9 jest: " + str(random.randrange(1, 10)))
print(random.sample(range(22), 2))  #dwie liczby z zakresu do 22
print(random.sample(range(49), 6))  #5 liczb z zakresu do 49

zwierzeta = ("kotek", "myszka", "piesek", "chomik")
print(random.choice(zwierzeta))

"""
>>>0.44364718690046834
>>>7

>>>
0.18323952104352015
0
ZERO

>>>
0.5984050177811581
2
LOSOWA LICZBA

>>>
0
ZERO
Twoja liczba losowa z zakresu liczb od 1 do 9 jest: 3
>>>
[17, 9]

>>>
[17, 41, 19, 20, 9, 0]

>>>
piesek

"""
