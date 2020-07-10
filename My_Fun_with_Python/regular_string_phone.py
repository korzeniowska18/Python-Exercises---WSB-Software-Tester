
# 71 340 63 36, bit = message[i:i+12] - przeprowadza iterację przez cały text i sprawdza każde 12 znaków od 0 do 12, potem od 1:13, potem od 2 do 14...
# import re - używanie funkcji - re.compile(), oraz search(), group()

def IsPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[2] != ' ':
        return False
    for i in range(3, 6):
        if not text[i].isdecimal():
            return False
    if text[6] != ' ':
        return False
    for i in range(7, 9):
        if not text[i].isdecimal():
            return False
    if text[9] != ' ':
        return False
    for i in range(10, 12):
        if not text[i].isdecimal():
            return False
    return True
   

print('71 340 63 36 to jest numer telefonu')
print(IsPhoneNumber('71 340 63 36'))
print('Trala La La to jest nummer telefonu')
print(IsPhoneNumber('Trala La La'))

>>>
71 340 63 36 to jest numer telefonu
True
Trala La La to jest nummer telefonu
False
>>> 
def IsPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 2):
        if not text[i].isdecimal():
            return False
    if text[2] != ' ':
        return False
    for i in range(3, 6):
        if not text[i].isdecimal():
            return False
    if text[6] != ' ':
        return False
    for i in range(7, 9):
        if not text[i].isdecimal():
            return False
    if text[9] != ' ':
        return False
    for i in range(10, 12):
        if not text[i].isdecimal():
            return False
    return True

message = ('Urząd we Wrocławiu, Adres, \
50-153 Wrocław, tel. 71 340 63 36, tel. 71 340 63 22')

for i in range(len(message)):
    bit = message[i:i+12]
    if IsPhoneNumber(bit):
        print('Znaleziono numer telefonu: ' + bit)
print('Zadanie wykonano!')

>>>
Znaleziono numer telefonu: 71 340 63 36
Znaleziono numer telefonu: 71 340 63 22
Zadanie wykonano!
>>> 

import re

phoneNumberRegex = re.compile(r'\d\d-\d\d\d-\d\d-\d\d')

mo = phoneNumberRegex.search('Urząd we Wrocławiu, Adres, \
50-153 Wrocław, tel. 71-340-63-36, tel. 71 340 63 22')

print('Znaleziono numer telefonu: ' + mo.group())

phoneNumberRegex = re.compile(r'\d\d \d\d\d \d\d \d\d')

mo = phoneNumberRegex.search('Urząd we Wrocławiu, Adres, \
50-153 Wrocław, tel. 71-340-63-36, tel. 71 340 63 22')

print('Znaleziono numer telefonu: ' + mo.group())

>>>
Znaleziono numer telefonu: 71-340-63-36
Znaleziono numer telefonu: 71 340 63 22
>>> 
