"""
upper(), lower(), capitalize(), isalpha(), isalnum(), isdecimal(), isspace(), istitle(), 
startswith(), endswith(), .join(), .split(), rjust(), ljust(), center(), pyperclip.copy(), pyperclip.paste()
casefold() - The casefold() method is an aggressive lower() method which converts strings to case folded strings for caseless matching.
find(), count(), rfind() - na której pozycji to co szukamy od prawej lub od lewej, uzywając find()
podobna fukcja index() oraz rindex(). Jeżeli nie znajdujemy szukanej literki, to funkcja index zwraca błąd, a find() -1
można szukać literki za pomoca operatora IN
"p" in text
True

>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'



>>> "Natali".upper().lower().islower()
True
>>> 
>>> lista = ['Mam', 'kotka', 'Felka']
>>> ', '.join(lista)
'Mam, kotka, Felka'
>>> ' '.join(lista)
'Mam kotka Felka'
>>> 'Mam kotka Felka'.split()
['Mam', 'kotka', 'Felka']
>>> lista = 'Mam kotka Felka'.split()
>>> lista
['Mam', 'kotka', 'Felka']
>>> slownik = {'kotek': 'Felek', 'color': 'czarny'}
>>> print(*list(slownik.keys()))
kotek color
>>> print(*list(slownik.values()), sep=',')
Felek,czarny
>>> 
>>> 'Natalia'.center(21, '*')
'*******Natalia*******'
>>> 
>>> 'Natalia'.rjust(10, '*')
'***Natalia'
>>> 'Natalia'.ljust(15, '*')
'Natalia********'
>>> 
"""

print("Cześć! Jak masz na imię?")

name = input()
name = name.capitalize()

print("\n")

print(f'{name}, Czy wszystko u Ciebie w porządku?')

mood = input()

if mood.lower() == 'tak':
    print("Bardzo się cieszę. U mnie też wszystko w porządku.")
elif mood.lower() == 'tak!':
    print("Super! U mnie też wszystko w porządku.")
elif mood.upper() == 'OK':
    print("Mam nadzieję, że to znaczy, ze jest wszystko w porządku")
else:
    print("Nie martw się. Jutro będzie lepiej!")

while True:
    print(f'{name}, Ile masz lat?')
    age = input()
    if age.isdecimal():
        break
    print("Wiek musi byc podany w postaci liczby")

age = int(age)

while True:
    if age <= 20:
        print("Całe życie przed tobą")
        break
    elif (age > 20 and age <= 40):
        print("To piękny wiek... jeszcze dużo przed tobą...")
        break
    else:
        print("Ciesz się życiem...")
        break

while True:
    print("A teraz wybierz swoje hasło(tylko litery i cyfry).")
    password = input()
    if password.isalnum():
        break
    print('Prypominam, Hasło może składać się jedynie z liter i cyfr')
print("Hasło zostało zapisane")

while True:
    print("Musimy jeszcze raz zwerifikować dane. Podaj swoje imię:")
    name_ver = input()
    name_ver = name_ver.capitalize()
    if name_ver.startswith(name):
        print("Weryfikacja przeszła pomyślnie")
        break


    """
    >>>
Cześć! Jak masz na imię?
olka


Olka, Czy wszystko u Ciebie w porządku?
mniej więcej
Nie martw się. Jutro będzie lepiej!
Olka, Ile masz lat?
oh
Wiek musi byc podany w postaci liczby
Olka, Ile masz lat?
35
To piękny wiek... jeszcze dużo przed tobą...
A teraz wybierz swoje hasło(tylko litery i cyfry).
kotkidwa!222
Prypominam, Hasło może składać się jedynie z liter i cyfr
A teraz wybierz swoje hasło(tylko litery i cyfry).
kotkidwa
Hasło zostało zapisane
Musimy jeszcze raz zwerifikować dane. Podaj swoje imię:
olka
Weryfikacja przeszła pomyślnie

>>> 
>>> 
"""

wiersz = '''Kocham życia każdą chwilę,
Słońce, co po niebie płynie,
Białe fajerwerki śniegu,
Deszcz, co po kałużach biega


I stokrotki uśmiechnięte,
Szmer jesiennych liści zwiędłych...
Nawet, gdy ktoś serce zrani
Życia kochać nie przestanę! '''

"""
>>> wiersz.split('\n')
['Kocham życia każdą chwilę,', 'Słońce, co po niebie płynie,', 'Białe fajerwerki śniegu,', 'Deszcz, co po kałużach biega', '', '', 'I stokrotki uśmiechnięte,', 'Szmer jesiennych liści zwiędłych...', 'Nawet, gdy ktoś serce zrani', 'Życia kochać nie przestanę! ']
>>> 
"""
"""
def printLection(itemsDict, leftWith, rightWith):
    print('NA LEKCJĘ'.center(leftWith + rightWith, '-'))
    for k, v in itemsDict.items():
          print(k.ljust(leftWith, '-') + str (v).rjust(rightWith))

lectionItems = {'zeszyty': 10, 'długopisy': 6, 'podręczniki dla uczniów': 5,
                'podręcznik nauczyciela': 1}

printLection(lectionItems, 23, 5)
print('\n')
printLection(lectionItems, 20, 6)
"""
>>>
---------NA LEKCJĘ----------
zeszyty----------------   10
długopisy--------------    6
podręczniki dla uczniów    5
podręcznik nauczyciela-    1


--------NA LEKCJĘ---------
zeszyty-------------    10
długopisy-----------     6
podręczniki dla uczniów     5
podręcznik nauczyciela     1
>>>
import pyperclip
>>> pyperclip.copy('Piękny ten świat')
>>> pyperclip.paste()
'Piękny ten świat'
>>> 

url = ('https://www.onet.pl/sport/onetsport//'
       'tenis-atp-w-delray-beach-christian-harrison-hubert-hurkacz-wynik//'
       'c1x3yp2,d87b6cc4')


print(url)

>>>
https://www.onet.pl/sport/onetsport//tenis-atp-w-delray-beach-christian-harrison-hubert-hurkacz-wynik//c1x3yp2,d87b6cc4
>>>
path = (r'C:/Users/user/Documents/new')


print(path)
>>>
C:/Users/user/Documents/new
>>>
imie = input("Podaj swoje imię: ")

print('Cześć, {}!'.format(imie))
print('Cześć, ' + imie + '!')
print(f'Cześć, {imie}!')

>>>
Podaj swoje imię: Nata
Cześć, Nata!
Cześć, Nata!
Cześć, Nata!
>>>
>>> "#I#like#travel#".replace('#',' ')
' I like travel '
>>> text = "#I#like#travel#"
>>> text.replace('#',' ')
' I like travel '
>>> a = '   Travel   '
>>> a.strip()
'Travel'
>>> a.lstrip()
'Travel   '
>>> a.rstrip()
'   Travel'
>>> 
>>> x = '*'.join(['apple', 'orange', 'watermelon', 'pear'])
>>> print(x)
apple*orange*watermelon*pear
>>> 

>>> x = 'Czy podróże kształcą?'
>>> x = x.lower()

>>> x = x.replace('ó', 'o').replace('ż', 'z').replace('ł', 'l').replace('ą', 'a').replace('?', '.')
>>> x
'czy podroze ksztalca.'
>>> print(len(set(x)))
15
>>>

>>> text = "This IS teXT"
>>> text.casefold()
'this is text'
>>> text = "This IS teKST"
>>> text.casefold()
'this is tekst'
>>> text = "Tę tekst jest częścią zadania"
>>> text.casefold()
'tę tekst jest częścią zadania'
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> nowa_lista = text.split(' ')
>>> nowa_lista
['Tę', 'tekst', 'jest', 'częścią', 'zadania']
>>> ' '.join(nowa_lista)
'Tę tekst jest częścią zadania'
>>> 

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''
 
lines = poem.split('\n')
 
for i in range(8):
    print(lines[i])
    print(lines[i+8])
    
>>>
>>> lines
['1.Runą i w łunach spłoną pożarnych ', 'Krzyże kościołów, krzyże ofiarne ', 'I w bezpowrotnym zgubi się szlaku ', 'W lechickiej ziemi Orzeł Polaków. ', '2.O, jasne słońce- wodzu Stalinie! ', 'Niech sława twoja nigdy nie zginie ', 'Niechaj jak orły powiedzie z gniazda ', 'Rosja i z Kremla płonąca gwiazda. ', '3.Na ziemskim globie flagi czerwone ', 'Będą na wiatrach grały jak dzwony ', 'Czerwona Armia i wódz jej Stalin ', 'Odwiecznych wrogów na zawsze obali! ', '4.Zaćmisz się rychło w czarnej godzinie ', 'Polsko- Twe córy i syny, ', 'Wiara i każdy krzyż na mogile, ', 'U stóp am legą w prochu i pyle! ']
>>> for i in range(8):
    print(lines[i])
    print(lines[i+8])

    
1.Runą i w łunach spłoną pożarnych 
3.Na ziemskim globie flagi czerwone 
Krzyże kościołów, krzyże ofiarne 
Będą na wiatrach grały jak dzwony 
I w bezpowrotnym zgubi się szlaku 
Czerwona Armia i wódz jej Stalin 
W lechickiej ziemi Orzeł Polaków. 
Odwiecznych wrogów na zawsze obali! 
2.O, jasne słońce- wodzu Stalinie! 
4.Zaćmisz się rychło w czarnej godzinie 
Niech sława twoja nigdy nie zginie 
Polsko- Twe córy i syny, 
Niechaj jak orły powiedzie z gniazda 
Wiara i każdy krzyż na mogile, 
Rosja i z Kremla płonąca gwiazda. 
U stóp am legą w prochu i pyle! 
>>> 
