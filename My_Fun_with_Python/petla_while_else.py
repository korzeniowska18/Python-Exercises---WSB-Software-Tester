a = 1
amax = 10

while a <= amax:
    print("This is Ok")
    a +=1                   => jeśli zapomnimy zaimplementować to, wtedy pętla wykonuje się w nieskończonność
    
>>>
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
>>>

a = 1
amax = 10

while a <= amax:
    print("This is Ok")
    a +=1
else:
    print("Now a = ", a)
    
>>>
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
This is Ok
Now a =  11
>>>

a = 1
amax = 10

while a <= amax:
    print(a, "This is Ok")
    a +=1
else:
    print("Now a = ", a)
   
   
>>>
1 This is Ok
2 This is Ok
3 This is Ok
4 This is Ok
5 This is Ok
6 This is Ok
7 This is Ok
8 This is Ok
9 This is Ok
10 This is Ok
Now a =  11
>>>

a = 1
amax = 10

while a <= amax:
    print(a, "This is Ok")
    a +=2
else:
    print("Now a = ", a)
    
>>>
1 This is Ok
3 This is Ok
5 This is Ok
7 This is Ok
9 This is Ok
Now a =  11
>>>

a = 10
amin = 0

while a >= amin:
    print(a, "This is Ok")
    a -=2
else:
    print("Now a = ", a)
>>>
10 This is Ok
8 This is Ok
6 This is Ok
4 This is Ok
2 This is Ok
0 This is Ok
Now a =  -2
>>>

line = 1

lastLinie = 10

number = line

while number <= lastLinie:
    print(number*'x')
    number +=1
    
>>>
x
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxxx
xxxxxxxxxx
>>>

a = 0
b = 16

while a <= b:
    print("Dwa do potęgi ", a, "wynosi ", 2 ** a)
    a +=1

>>>
Dwa do potęgi  0 wynosi  1
Dwa do potęgi  1 wynosi  2
Dwa do potęgi  2 wynosi  4
Dwa do potęgi  3 wynosi  8
Dwa do potęgi  4 wynosi  16
Dwa do potęgi  5 wynosi  32
Dwa do potęgi  6 wynosi  64
Dwa do potęgi  7 wynosi  128
Dwa do potęgi  8 wynosi  256
Dwa do potęgi  9 wynosi  512
Dwa do potęgi  10 wynosi  1024
Dwa do potęgi  11 wynosi  2048
Dwa do potęgi  12 wynosi  4096
Dwa do potęgi  13 wynosi  8192
Dwa do potęgi  14 wynosi  16384
Dwa do potęgi  15 wynosi  32768
Dwa do potęgi  16 wynosi  65536

>>>
wplacony_kapital = 20000

procent_odsetek = 0.03

max_okres_oszczedzania = 10

rok = 0

kapital = wplacony_kapital

while rok < max_okres_oszczedzania:
    rok +=1
    kapital = round((1 + procent_odsetek)* kapital,2)
    print('Po zakończeniu ', rok, 'roku na końcie będzie kwota w wysokości', kapital)
else:
    print('Całkowita kwota oszczędności w ciągu 10 lat wynosi ', kapital - wplacony_kapital)
    
>>>
Po zakończeniu  1 roku na końcie będzie kwota w wysokości 20600.0
Po zakończeniu  2 roku na końcie będzie kwota w wysokości 21218.0
Po zakończeniu  3 roku na końcie będzie kwota w wysokości 21854.54
Po zakończeniu  4 roku na końcie będzie kwota w wysokości 22510.18
Po zakończeniu  5 roku na końcie będzie kwota w wysokości 23185.49
Po zakończeniu  6 roku na końcie będzie kwota w wysokości 23881.05
Po zakończeniu  7 roku na końcie będzie kwota w wysokości 24597.48
Po zakończeniu  8 roku na końcie będzie kwota w wysokości 25335.4
Po zakończeniu  9 roku na końcie będzie kwota w wysokości 26095.46
Po zakończeniu  10 roku na końcie będzie kwota w wysokości 26878.32
Całkowita kwota oszczędności w ciągu 10 lat wynosi  6878.32
>>> 

number=20730906
tmpnumber = number
sumOfDigits = 0
while tmpnumber >0:
    digit = tmpnumber % 10
    sumOfDigits += digit
    tmpnumber = tmpnumber//10
else:
    print('the sum of digits of ', number, ' is',sumOfDigits)
    
>>>
the sum of digits of  20730906  is 27
-------------------------------------------------------
>>> 

text = 'Rozwiązania oparte na VPN stosowane są np. w sieciach korporacyjnych, \
których zdalni użytkownicy pracują ze swoich domów na niezabezpieczonych \
łączach. Wirtualne sieci prywatne charakteryzują się dość dużą efektywnością,\
nawet na słabych łączach (dzięki kompresji danych) oraz wysokim \
poziomem bezpieczeństwa (ze względu na szyfrowanie). Rozwiązanie to\
sprawdza się w firmach, których pracownicy często podróżują lub \
korzystają z możliwości'

dlugosc_slowa = 6
krotkie_slowa = 0
dlugie_slowa = 0
i = 0

lista_slow = text.replace('(', '').replace(')', '').replace('\n', ' ').split(' ')
while i < len(lista_slow):
    if len(lista_slow[i]) > dlugosc_slowa:
        dlugie_slowa +=1
    else:
        krotkie_slowa +=1

    i+=1
print('Tekst zawiera łącznie',len(lista_slow), 'słów.')
print('Słów mniejszych niż', dlugosc_slowa,'liter jest',krotkie_slowa,'.')
print('Słów dłuższych niż',  dlugosc_slowa,'liter jest', dlugie_slowa,'.')

>>>
Tekst zawiera łącznie 55 słów.
Słów mniejszych niż 6 liter jest 26 .
Słów dłuższych niż 6 liter jest 29 .
>>> 
