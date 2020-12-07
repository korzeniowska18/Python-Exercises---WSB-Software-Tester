from datetime import date
from datetime import time
from datetime import datetime 
from datetime import timedelta 

print(timedelta(days=365, hours=5, minutes=1))

obecny_czas = datetime.now()
print("Dzisiaj jest: " + str(obecny_czas))

print("Za rok od tego momentu będzie: " + str(obecny_czas + timedelta(days=365)))
print("Za 3 dni i 3 tygodni będzie: " + str(obecny_czas + timedelta(days=3, weeks=3)))

czas = datetime.now() - timedelta(weeks=1)
tydzien_temu = czas.strftime("%A %B %d, %Y")
print("Tydzien temu mieliśmy: " + tydzien_temu)

dzisiaj = date.today()
wd = date(dzisiaj.year, 2, 14)

if wd < dzisiaj:
    print("Walentynki już były %d dni temu" % ((dzisiaj-wd).days))
    wdn= wd.replace(year=dzisiaj.year+1)

czas_do_wd = wd - dzisiaj

print("Jest ", czas_do_wd.days, "dni do Walentynek")

"""
>>>
365 days, 5:01:00
Dzisiaj jest: 2020-12-07 14:07:48.106082

Za rok od tego momentu będzie: 2021-12-07 14:09:16.691504

Za 3 dni i 3 tygodni będzie: 2020-12-31 14:11:03.196199

Tydzien temu mieliśmy: Monday November 30, 2020

Walentynki już były 297 dni temu
Jest  -297 dni do Walentynek


"""
