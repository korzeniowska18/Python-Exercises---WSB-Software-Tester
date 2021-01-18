#Jak sprawdzić trzy kolejne rosnące liczby

liczby = [23, 45, 12, 34, 11, 16, 18, 76, 23, 46, 24, 31, 40, 15, 26]

i = 0
max = len(liczby) -2

while i < max:
    print(i, liczby[i], liczby[i+1], liczby[i+2])

    if liczby[i] < liczby[i+1] and liczby[i+1] < liczby[i+2]:
        print('\t Znaleziono rosnące liczby: ', liczby[i], liczby[i+1], liczby[i+2])
    i += 1
    
>>>
0 23 45 12
1 45 12 34
2 12 34 11
3 34 11 16
4 11 16 18
	 Znaleziono rosnące liczby:  11 16 18
5 16 18 76
	 Znaleziono rosnące liczby:  16 18 76
6 18 76 23
7 76 23 46
8 23 46 24
9 46 24 31
10 24 31 40
	 Znaleziono rosnące liczby:  24 31 40
11 31 40 15
12 40 15 26
>>> 

#Trzeba odnaleźć takie dwie kolejne liczby, że druga jest kwadratem pierwszej.
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) -1

while i < max:
    print(i, numbers[i], numbers[i + 1])

    if  numbers[i] * numbers[i] == numbers[i + 1]:
        print('\t Znaleziono: ', numbers[i], numbers[i + 1])

    i += 1  
>>>
0 8 18
1 18 2
2 2 4
	 Znaleziono:  2 4
3 4 16
	 Znaleziono:  4 16
4 16 5
5 5 25
	 Znaleziono:  5 25
6 25 4
7 4 22
8 22 3
9 3 3
10 3 5
11 5 3
12 3 9
	 Znaleziono:  3 9
13 9 81
	 Znaleziono:  9 81
14 81 11
>>> 

# należy analizować po 3 wartości na raz. Interesuje nas odnalezienie takich 3 liczb,
#że pierwsza do kwadratu równa się drugiej, a druga do kwadratu równa się trzeciej.

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers) -2

while i < max:
    print(i, numbers[i], numbers[i + 1], numbers[i + 2])

    if  numbers[i] * numbers[i] == numbers[i + 1] and numbers[i + 1] * numbers[i + 1] == numbers[i + 2]:
        print('\t Znaleziono: ', numbers[i], numbers[i + 1], numbers[i + 2])

    i += 1  
>>>
0 8 18 2
1 18 2 4
2 2 4 16
	 Znaleziono:  2 4 16
3 4 16 5
4 16 5 25
5 5 25 4
6 25 4 22
7 4 22 3
8 22 3 3
9 3 3 5
10 3 5 3
11 5 3 9
12 3 9 81
	 Znaleziono:  3 9 81
13 9 81 11
>>> 

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]


i = 0

max = len(numbers)-1


while i< max:


    print(i, numbers[i],numbers[i+1])

   

    if numbers[i]**2 == numbers[i+1]:

        print("\tFOUND!")


    i+=1


print('------------------------------')


numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]


i = 0

max = len(numbers)-2


while i< max:


    print(i, numbers[i],numbers[i+1], numbers[i+2])

   

    if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 == numbers[i+2]:

        print("\tFOUND!")


    i+=1



print('------------------------------')


texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


i = 0

max = len(texts)-1


while i< max:


    print(i, texts[i],texts[i+1])

   

    if len(texts[i]) == len(texts[i+1]):

        print("\tFOUND!")


    i+=1

#jak zapakować jak najwięcej paczek do kontenera
paczki = [30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
print(paczki)
#paczki.sort()
paczki.reverse()

rozmiarKontenera = 90
kontener = []
i = 0

while sum(kontener) + paczki[i] < rozmiarKontenera and i < len(paczki):
    kontener.append(paczki[i])
    i += 1

print("Suma paczek w kontenerze: ", sum(kontener))
print("Zawartość kontenera: ", kontener)
print("Liczba paczek w kontenerze: ", len(kontener))

[30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
Suma paczek w kontenerze:  78
Zawartość kontenera:  [3, 4, 5, 5, 7, 10, 12, 15, 17]
Liczba paczek w kontenerze:  9
>>> 
= RESTART: C:\Users\korze\Documents\Repozytorium\Python-Exercises---WSB-Software-Tester\My_Fun_with_Python\kurs_pocz.py
[30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
Suma paczek w kontenerze:  87
Zawartość kontenera:  [40, 12, 18, 4, 10, 3]
Liczba paczek w kontenerze:  6
>>> 
paczki = [30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
print(paczki)
#paczki.sort()
paczki.reverse()

rozmiarKontenera = 90
kontener = []
i = 0

while i < len(paczki)and (rozmiarKontenera - sum(kontener) >= min(paczki)):
    if (rozmiarKontenera - sum(kontener)) >= paczki[i]:
        kontener.append(paczki[i])
    i += 1

print("Suma paczek w kontenerze: ", sum(kontener))
print("Zawartość kontenera: ", kontener)
print("Liczba paczek w kontenerze: ", len(kontener))

>>>
[30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
Suma paczek w kontenerze:  87
Zawartość kontenera:  [40, 12, 18, 4, 10, 3]
Liczba paczek w kontenerze:  6
>>> 
paczki = [30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
print(paczki)
paczki.sort()
paczki.reverse()

rozmiarKontenera = 90
kontener = []
i = 0

while i < len(paczki)and (rozmiarKontenera - sum(kontener) >= min(paczki)):
    if (rozmiarKontenera - sum(kontener)) >= paczki[i]:
        kontener.append(paczki[i])
    i += 1

print("Suma paczek w kontenerze: ", sum(kontener))
print("Zawartość kontenera: ", kontener)
print("Liczba paczek w kontenerze: ", len(kontener))

>>>
[30, 20, 15, 5, 26, 45, 20, 30, 5, 7, 17, 3, 10, 4, 18, 12, 40]
Suma paczek w kontenerze:  90
Zawartość kontenera:  [45, 40, 5]
Liczba paczek w kontenerze:  3
>>>

#sumy dwóch kolejnych liczb od 0 do 50
previous_number = 0
 
while number<=50:
    print(number + previous_number)
    previous_number=number
    number+=1

>>>
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
>>> 
#Komputer wymyśli sobie liczbę od 0 do 20, a Ty musisz ją zgadnąć!





