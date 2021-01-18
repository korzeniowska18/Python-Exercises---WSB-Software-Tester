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


