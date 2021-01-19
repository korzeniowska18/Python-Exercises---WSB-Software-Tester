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
