pracownicy = ['Rafael', 'Maria', 'Roy', 'Krisitina', 'Jon', 'Joanna']

domena = 'mojafirma.pl'

for pracownik in pracownicy:
    email = pracownik.lower() + '@' + domena
    print('Adres mailowy ', pracownik, '\tjest to', email)
else:
    print("----- Koniec listy -----")
    
>>>
Adres mailowy  Rafael 	jest to rafael@mojafirma.pl
Adres mailowy  Maria 	jest to maria@mojafirma.pl
Adres mailowy  Roy 	jest to roy@mojafirma.pl
Adres mailowy  Krisitina 	jest to krisitina@mojafirma.pl
Adres mailowy  Jon 	jest to jon@mojafirma.pl
Adres mailowy  Joanna 	jest to joanna@mojafirma.pl
----- Koniec listy -----
>>>

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for error in data:
    print(error.upper())
    
>>>
ERROR:FILE CANNOT BE OPEN
ERROR:NO FREE SPACE ON DISK
ERROR:FILE MISSING
WARNING:INTERNET CONNECTION LOST
ERROR:ACCESS DENIED
>>> 

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for e in data:
    errors = e.split(':')
    print(errors[0].upper())
    print(errors[1])
    
>>>
ERROR
File cannot be open
ERROR
No free space on disk
ERROR
File missing
WARNING
Internet connection lost
ERROR
Access denied
>>> 
for liczba in range(1,16, 2):
    print(liczba)
    
>>>
1
3
5
7
9
11
13
15
>>> 

for liczba in range(1,20):
    if liczba %2 == 0:
        print('Liczba %2d jest %s' % (liczba, 'parzysta'))
        
>>>
Liczba  2 jest parzysta
Liczba  4 jest parzysta
Liczba  6 jest parzysta
Liczba  8 jest parzysta
Liczba 10 jest parzysta
Liczba 12 jest parzysta
Liczba 14 jest parzysta
Liczba 16 jest parzysta
Liczba 18 jest parzysta
>>>
for liczba in range(1,20):
    if liczba %2 == 0:
        print('Liczba %2d jest %s' % (liczba, 'parzysta'))
    #print(liczba)
    else:
        print('Liczba %2d jest %s' % (liczba, 'nieparzysta'))
>>>
Liczba  1 jest nieparzysta
Liczba  2 jest parzysta
Liczba  3 jest nieparzysta
Liczba  4 jest parzysta
Liczba  5 jest nieparzysta
Liczba  6 jest parzysta
Liczba  7 jest nieparzysta
Liczba  8 jest parzysta
Liczba  9 jest nieparzysta
Liczba 10 jest parzysta
Liczba 11 jest nieparzysta
Liczba 12 jest parzysta
Liczba 13 jest nieparzysta
Liczba 14 jest parzysta
Liczba 15 jest nieparzysta
Liczba 16 jest parzysta
Liczba 17 jest nieparzysta
Liczba 18 jest parzysta
Liczba 19 jest nieparzysta
>>>
string_C = '+---+---+---+---+'
string_D = '|   |   |   |   |'

for s in range(11):
    print(string_C)

print('\n')

for i in range(9):
    if i % 2 == 0:
        print(string_C)
    else:
        print(string_D)

print('\n')

for i in range(1,10):
    print("x"*i)
 
print('')
 
for i in range(1,10):
    if i % 2 == 0:
        print("x"*i)
    else:
        print("o"*i)
        
 >>>
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+
+---+---+---+---+


+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+


x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx

o
xx
ooo
xxxx
ooooo
xxxxxx
ooooooo
xxxxxxxx
ooooooooo
>>> 
for x in range(1, 6):
    for y in range(1, 6):
        print(x, '*', y, '=', x*y)
        
>>>
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
>>> 
for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += '\t'+str(x*y)
    print(line)
    
>>>
1	1	2	3	4	5
2	2	4	6	8	10
3	3	6	9	12	15
4	4	8	12	16	20
5	5	10	15	20	25
>>> 

for x in range(1, 6):
    line = str(x)
    for y in range(1, 6):
        line += '\t%3d' % (x*y)
    print(line)
    
>>>
1	  1	  2	  3	  4	  5
2	  2	  4	  6	  8	 10
3	  3	  6	  9	 12	 15
4	  4	  8	 12	 16	 20
5	  5	 10	 15	 20	 25
>>> 
#Zmienna i ma wartość 10. Korzystając z pętli for wyznacz wartość
    #silnia i

i = 10
result = 1

 
for j in range(1,i+1):
    result *= j
 
print(i, result)

>>>
10 3628800
>>> 

x = 10
 
for i in range(1,x+1):
 
    result = 1
    
    for j in range(1,i+1):
        result *= j
 
    print(i, result)
    
>>>
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
10 3628800
>>> 

lista_rzeczownikow = ['piesek', 'kotek', 'cukierek', 'kwiat', 'samochód']
lista_przymiotnikow = ['biały', 'duży', 'miły', 'mały', 'nowy']
 
for rzeczownik in lista_rzeczownikow:
    for przymiotnik in lista_przymiotnikow:
        print(rzeczownik, przymiotnik)
        
>>>
piesek biały
piesek duży
piesek miły
piesek mały
piesek nowy
kotek biały
kotek duży
kotek miły
kotek mały
kotek nowy
cukierek biały
cukierek duży
cukierek miły
cukierek mały
cukierek nowy
kwiat biały
kwiat duży
kwiat miły
kwiat mały
kwiat nowy
samochód biały
samochód duży
samochód miły
samochód mały
samochód nowy
>>> 


a1 = 0
a2 = 1
a3 = a1 + a2
print("Ciąg Fibonacciego:")

for i in range(0, 20):
    print(i," Suma kolejnych liczb od 0 d0 20 jest to: ", a3)
    a1 = a2
    a2 = a3
    a3 = a1 + a2
    
>>>
Ciąg Fibonacciego:
0  Suma kolejnych liczb od 0 d0 20 jest to:  1
1  Suma kolejnych liczb od 0 d0 20 jest to:  2
2  Suma kolejnych liczb od 0 d0 20 jest to:  3
3  Suma kolejnych liczb od 0 d0 20 jest to:  5
4  Suma kolejnych liczb od 0 d0 20 jest to:  8
5  Suma kolejnych liczb od 0 d0 20 jest to:  13
6  Suma kolejnych liczb od 0 d0 20 jest to:  21
7  Suma kolejnych liczb od 0 d0 20 jest to:  34
8  Suma kolejnych liczb od 0 d0 20 jest to:  55
9  Suma kolejnych liczb od 0 d0 20 jest to:  89
10  Suma kolejnych liczb od 0 d0 20 jest to:  144
11  Suma kolejnych liczb od 0 d0 20 jest to:  233
12  Suma kolejnych liczb od 0 d0 20 jest to:  377
13  Suma kolejnych liczb od 0 d0 20 jest to:  610
14  Suma kolejnych liczb od 0 d0 20 jest to:  987
15  Suma kolejnych liczb od 0 d0 20 jest to:  1597
16  Suma kolejnych liczb od 0 d0 20 jest to:  2584
17  Suma kolejnych liczb od 0 d0 20 jest to:  4181
18  Suma kolejnych liczb od 0 d0 20 jest to:  6765
19  Suma kolejnych liczb od 0 d0 20 jest to:  10946
>>> 

text = 'Rozwiązania oparte na VPN stosowane są np. w sieciach korporacyjnych, \
których zdalni użytkownicy pracują ze swoich domów na niezabezpieczonych \
łączach. Wirtualne sieci prywatne charakteryzują się dość dużą efektywnością,\
nawet na słabych łączach (dzięki kompresji danych) oraz wysokim \
poziomem bezpieczeństwa (ze względu na szyfrowanie). Rozwiązanie to\
sprawdza się w firmach, których pracownicy często podróżują lub \
korzystają z możliwości'

print("Słowa zawierające literę 'p': ")

listOfWords = text.replace('\n',' ').split(' ')

for word in listOfWords:
    if word.lower().find('p') > 0:
        print(word)
        
>>>

Słowa zawierające literę 'p': 
oparte
VPN
np.
korporacyjnych,
niezabezpieczonych
kompresji
bezpieczeństwa
tosprawdza
>>> 

