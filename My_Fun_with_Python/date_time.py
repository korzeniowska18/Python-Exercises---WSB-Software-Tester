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

import time
 
print(time.time())
print(time.localtime(time.time()))
 
import calendar
 
print(calendar.month(2021,2))
calendar.setfirstweekday(6)
print(calendar.month(2021,3))
 
print('2020 is leap: ', calendar.isleap(2020))
 
print(calendar.calendar(2021))

>>>>

1614327534.769173     >>>>> jest to czas unixowy
time.struct_time(tm_year=2021, tm_mon=2, tm_mday=26, tm_hour=9, tm_min=18, tm_sec=54, tm_wday=4, tm_yday=57, tm_isdst=0)
   February 2021
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28

     March 2021
Su Mo Tu We Th Fr Sa
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

2020 is leap:  True
                                  2021

      January                   February                   March
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa      Su Mo Tu We Th Fr Sa
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

>>>
import datetime

print("Minimalna wartośc i maksymalna: ", datetime.MINYEAR, datetime.MAXYEAR)

dl = datetime.timedelta(days=1, hours=2, minutes=-30)
print(dl)

dl2 = datetime.timedelta(days=-1, hours=-2, minutes=-3)

print(dl2)

print("sumę timedelta: ", dl+dl2)

print("Dziasiaj jest: ", datetime.date.today())

>>>
Minimalna wartośc i maksymalna:  1 9999
1 day, 1:30:00
-2 days, 21:57:00
sumę timedelta:  -1 day, 23:27:00
Dziasiaj jest:  2021-02-26
>>> 

from datetime import datetime
print('results generated',datetime.today())
print('results generated:',datetime.today().strftime("%Y-%m-%d"))
 
# another solution (by Tomek - thanks for cooperation!):
import datetime
print('results generated',datetime.date.today())
print('results generated:',datetime.date.today().strftime("%Y-%m-%d"))

>>>>>

results generated 2021-02-26 09:34:46.901862
results generated: 2021-02-26
results generated 2021-02-26
results generated: 2021-02-26
>>> 

from datetime import date

def IleDniDoKoncaRoku():
    dzien_dzisiejszy = date.today()
    rok_biezacy = dzien_dzisiejszy.year
    data_ostatniego_dnia_w_roku = date(rok_biezacy, 12, 31)
    delta = data_ostatniego_dnia_w_roku - dzien_dzisiejszy
    print(delta.days)
 
IleDniDoKoncaRoku()

>>>
263
>>> 
