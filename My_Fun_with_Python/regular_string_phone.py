
# 71 340 63 36

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
