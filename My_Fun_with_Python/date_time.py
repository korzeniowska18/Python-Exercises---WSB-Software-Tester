# %y %Y - rok, %a %A - dzień tygodnia, %b %B - miesiąc, %d - dzień miesiąca
# %x, %X - lokalne data i czas, PM czas -  %I:%M:%S %p,  24-godz. czas: %H:%M

from datetime import datetime
from datetime import date
from datetime import time

def main():
    obecny_czas = datetime.now()
    dzien_obecny = date.today() 
    print(obecny_czas.strftime("Obecnie jest %Y rok"))
    print(obecny_czas.strftime("Dzisiaj jest: %A, %d %B %Y"))
    print("Dzisiaj jest: ", dzien_obecny)
    dni_tygodnia = ["Poniedzialek", "Wtorek", "Sroda", "Czwartek", "Piatek", "Sobota", "Niedziela"]
    print("Obecnie jest: ", dzien_obecny.day, dzien_obecny.month, dzien_obecny.year)
    print("Dzisiaj jest dzien' tygodnia: ", dzien_obecny.weekday()) 
    print("Jaki dzisiaj jest dzien' tygodnia: ", dni_tygodnia[dzien_obecny.weekday()]) 
    print("Dzisiejsza data jest: ", obecny_czas)
    czas = datetime.time(datetime.now())
    print(czas)
    print(obecny_czas.strftime("Lokalna data i czas: %c"))
    print(obecny_czas.strftime("Lokalna data: %x"))
    print(obecny_czas.strftime("Lokalny czas: %X"))
    print(obecny_czas.strftime("Czas obecny: %I:%M:%S %p"))
    print(obecny_czas.strftime("24-godz. czas: %H:%M"))
    

if __name__ == "__main__":
    main()


"""
>>> Obecnie jest 2020 rok
>>> Dziś jest: Wednesday, 02 December 2020

>>>
Dzisiaj jest:  2020-12-07

Obecnie jest:  7 12 2020
Dzisiaj jest dzien' tygodnia:  0
Jaki dzisiaj jest dzien' tygodnia:  Poniedzialek

Dzisiejsza data jest:  2020-12-07 10:42:30.639562

13:47:09.388593

Lokalna data i czas: Mon Dec  7 13:49:49 2020

Lokalna data: 12/07/20

Lokalny czas: 13:53:13

Czas obecny: 01:55:02 PM

24-godz. czas: 13:57

"""
>>>
>>> import time
>>> import sys
>>> print(sys.version)
3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
>>>
>>> print(time.perf_counter(), time.localtime(time.perf_counter()))
89.4915672 time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=1, tm_min=1, tm_sec=29, tm_wday=3, tm_yday=1, tm_isdst=0)
>>> 

>>> import time
>>> time.time()
1614326427.3598132
>>> time.localtime(time.time())
time.struct_time(tm_year=2021, tm_mon=2, tm_mday=26, tm_hour=9, tm_min=0, tm_sec=57, tm_wday=4, tm_yday=57, tm_isdst=0)
>>> time.asctime(time.localtime(time.time()))
'Fri Feb 26 09:01:38 2021'
>>> time.localtime(time.clock())
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    time.localtime(time.clock())
AttributeError: module 'time' has no attribute 'clock'
>>> time.localtime(time.clock()))
SyntaxError: unmatched ')'
>>> import calendar
>>> calendar.month(2021, 7)
'     July 2021\nMo Tu We Th Fr Sa Su\n          1  2  3  4\n 5  6  7  8  9 10 11\n12 13 14 15 16 17 18\n19 20 21 22 23 24 25\n26 27 28 29 30 31\n'

>>> calendar.month(2021, 7, w=1, l=2)
'     July 2021\n\nMo Tu We Th Fr Sa Su\n\n          1  2  3  4\n\n 5  6  7  8  9 10 11\n\n12 13 14 15 16 17 18\n\n19 20 21 22 23 24 25\n\n26 27 28 29 30 31\n\n'
>>> calendar.setfirstweekday(6)
>>> calendar.month(2021, 7)
'     July 2021\nSu Mo Tu We Th Fr Sa\n             1  2  3\n 4  5  6  7  8  9 10\n11 12 13 14 15 16 17\n18 19 20 21 22 23 24\n25 26 27 28 29 30 31\n'
>>> 
