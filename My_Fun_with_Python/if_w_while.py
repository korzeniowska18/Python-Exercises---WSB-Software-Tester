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
