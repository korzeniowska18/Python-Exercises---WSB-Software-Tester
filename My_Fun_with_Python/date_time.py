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
