wiek = 20
IsOdpowiedniStroj = True
IsInneOgraniczenia = False

if wiek < 18:
    print("W zawodach mogą brac udział tylko osoby pełnoletnie")
elif not IsOdpowiedniStroj:
    print("W zawodach mogą brac udział tylko osoby posiadające odpowiedni stroj")
elif IsInneOgraniczenia:
    print("W zawodach mogą brac udział tylko osoby z brakiem innych ograniczeń")
else:
    print("Możesz brać udział w zawodach")
    
>>>
Możesz brać udział w zawodach
>>>

# do sprawdzenia kilka warunków

wiek = 15
IsOdpowiedniStroj = True
IsInneOgraniczenia = False

if wiek < 18:
    print("W zawodach mogą brac udział tylko osoby pełnoletnie")
elif not IsOdpowiedniStroj:
    print("W zawodach mogą brac udział tylko osoby posiadające odpowiedni stroj")
elif IsInneOgraniczenia:
    print("W zawodach mogą brac udział tylko osoby z brakiem innych ograniczeń")
else:
    print("Możesz brać udział w zawodach")
    
>>>
W zawodach mogą brac udział tylko osoby pełnoletnie
>>>
wiek = 26
IsOdpowiedniStroj = False
IsInneOgraniczenia = False

if wiek < 18:
    print("W zawodach mogą brac udział tylko osoby pełnoletnie")
elif not IsOdpowiedniStroj:
    print("W zawodach mogą brac udział tylko osoby posiadające odpowiedni stroj")
elif IsInneOgraniczenia:
    print("W zawodach mogą brac udział tylko osoby z brakiem innych ograniczeń")
else:
    print("Możesz brać udział w zawodach")
>>>
W zawodach mogą brac udział tylko osoby posiadające odpowiedni stroj
>>>

wiek = 26
IsOdpowiedniStroj = True
IsInneOgraniczenia = True

if wiek < 18:
    print("W zawodach mogą brac udział tylko osoby pełnoletnie")
elif not IsOdpowiedniStroj:
    print("W zawodach mogą brac udział tylko osoby posiadające odpowiedni stroj")
elif IsInneOgraniczenia:
    print("W zawodach mogą brac udział tylko osoby z brakiem innych ograniczeń")
else:
    print("Możesz brać udział w zawodach")
    
>>>
W zawodach mogą brac udział tylko osoby z brakiem innych ograniczeń
>>>
