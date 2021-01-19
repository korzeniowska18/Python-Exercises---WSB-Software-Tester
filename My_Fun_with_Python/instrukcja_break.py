# instrukcję break używamy w pętlach FOR i WHILE, kiedy uważamy, że dalsze wykonywanie
# pętli nie ma sensu

# 1 przykład bez instrukcji break

for kandydat in range(2, 21):
    for dzielnik in range(2, kandydat):
        if kandydat % dzielnik == 0:
            print('%2d nie jest liczbą pierwszą - \
                    dzielnik jest %2d' %(kandydat, dzielnik))
                    
>>>
 4 nie jest liczbą pierwszą -                     dzielnik jest  2
 6 nie jest liczbą pierwszą -                     dzielnik jest  2
 6 nie jest liczbą pierwszą -                     dzielnik jest  3
 8 nie jest liczbą pierwszą -                     dzielnik jest  2
 8 nie jest liczbą pierwszą -                     dzielnik jest  4
 9 nie jest liczbą pierwszą -                     dzielnik jest  3
10 nie jest liczbą pierwszą -                     dzielnik jest  2
10 nie jest liczbą pierwszą -                     dzielnik jest  5
12 nie jest liczbą pierwszą -                     dzielnik jest  2
12 nie jest liczbą pierwszą -                     dzielnik jest  3
12 nie jest liczbą pierwszą -                     dzielnik jest  4
12 nie jest liczbą pierwszą -                     dzielnik jest  6
14 nie jest liczbą pierwszą -                     dzielnik jest  2
14 nie jest liczbą pierwszą -                     dzielnik jest  7
15 nie jest liczbą pierwszą -                     dzielnik jest  3
15 nie jest liczbą pierwszą -                     dzielnik jest  5
16 nie jest liczbą pierwszą -                     dzielnik jest  2
16 nie jest liczbą pierwszą -                     dzielnik jest  4
16 nie jest liczbą pierwszą -                     dzielnik jest  8
18 nie jest liczbą pierwszą -                     dzielnik jest  2
18 nie jest liczbą pierwszą -                     dzielnik jest  3
18 nie jest liczbą pierwszą -                     dzielnik jest  6
18 nie jest liczbą pierwszą -                     dzielnik jest  9
20 nie jest liczbą pierwszą -                     dzielnik jest  2
20 nie jest liczbą pierwszą -                     dzielnik jest  4
20 nie jest liczbą pierwszą -                     dzielnik jest  5
20 nie jest liczbą pierwszą -                     dzielnik jest 10
>>>

# z instrukcją break

for kandydat in range(2, 21):
    for dzielnik in range(2, kandydat):
        if kandydat % dzielnik == 0:
            print('%2d nie jest liczbą pierwszą - \
                    dzielnik jest %2d' %(kandydat, dzielnik))
            break
            
>>>
 4 nie jest liczbą pierwszą -                     dzielnik jest  2
 6 nie jest liczbą pierwszą -                     dzielnik jest  2
 8 nie jest liczbą pierwszą -                     dzielnik jest  2
 9 nie jest liczbą pierwszą -                     dzielnik jest  3
10 nie jest liczbą pierwszą -                     dzielnik jest  2
12 nie jest liczbą pierwszą -                     dzielnik jest  2
14 nie jest liczbą pierwszą -                     dzielnik jest  2
15 nie jest liczbą pierwszą -                     dzielnik jest  3
16 nie jest liczbą pierwszą -                     dzielnik jest  2
18 nie jest liczbą pierwszą -                     dzielnik jest  2
20 nie jest liczbą pierwszą -                     dzielnik jest  2
>>> 

for kandydat in range(2, 21):
    liczba_pierwsza = True
    for dzielnik in range(2, kandydat):
        if kandydat % dzielnik == 0:
            liczba_pierwsza = False
            print('%2d nie jest liczbą pierwszą - \
                    dzielnik jest %2d' %(kandydat, dzielnik))
            break
    if liczba_pierwsza:
        print('%2d jest liczbą pierwszą!' %(kandydat))
        
>>>
 2 jest liczbą pierwszą!
 3 jest liczbą pierwszą!
 4 nie jest liczbą pierwszą -                     dzielnik jest  2
 5 jest liczbą pierwszą!
 6 nie jest liczbą pierwszą -                     dzielnik jest  2
 7 jest liczbą pierwszą!
 8 nie jest liczbą pierwszą -                     dzielnik jest  2
 9 nie jest liczbą pierwszą -                     dzielnik jest  3
10 nie jest liczbą pierwszą -                     dzielnik jest  2
11 jest liczbą pierwszą!
12 nie jest liczbą pierwszą -                     dzielnik jest  2
13 jest liczbą pierwszą!
14 nie jest liczbą pierwszą -                     dzielnik jest  2
15 nie jest liczbą pierwszą -                     dzielnik jest  3
16 nie jest liczbą pierwszą -                     dzielnik jest  2
17 jest liczbą pierwszą!
18 nie jest liczbą pierwszą -                     dzielnik jest  2
19 jest liczbą pierwszą!
20 nie jest liczbą pierwszą -                     dzielnik jest  2
>>> 

# instrukcja else nie będzie wykonana jeżeli jest break

for kandydat in range(2, 21):
    for dzielnik in range(2, kandydat):
        if kandydat % dzielnik == 0:
            liczba_pierwsza = False
            print('%2d nie jest liczbą pierwszą - \
                    dzielnik jest %2d' %(kandydat, dzielnik))
    else:
        print('%2d jest liczbą pierwszą!' %(kandydat))
        
>>>
 2 jest liczbą pierwszą!
 3 jest liczbą pierwszą!
 4 nie jest liczbą pierwszą -                     dzielnik jest  2
 4 jest liczbą pierwszą!
 5 jest liczbą pierwszą!
 6 nie jest liczbą pierwszą -                     dzielnik jest  2
 6 nie jest liczbą pierwszą -                     dzielnik jest  3
 6 jest liczbą pierwszą!
 7 jest liczbą pierwszą!
 8 nie jest liczbą pierwszą -                     dzielnik jest  2
 8 nie jest liczbą pierwszą -                     dzielnik jest  4
 8 jest liczbą pierwszą!
 9 nie jest liczbą pierwszą -                     dzielnik jest  3
 9 jest liczbą pierwszą!
10 nie jest liczbą pierwszą -                     dzielnik jest  2
10 nie jest liczbą pierwszą -                     dzielnik jest  5
10 jest liczbą pierwszą!
11 jest liczbą pierwszą!
12 nie jest liczbą pierwszą -                     dzielnik jest  2
12 nie jest liczbą pierwszą -                     dzielnik jest  3
12 nie jest liczbą pierwszą -                     dzielnik jest  4
12 nie jest liczbą pierwszą -                     dzielnik jest  6
12 jest liczbą pierwszą!
13 jest liczbą pierwszą!
14 nie jest liczbą pierwszą -                     dzielnik jest  2
14 nie jest liczbą pierwszą -                     dzielnik jest  7
14 jest liczbą pierwszą!
15 nie jest liczbą pierwszą -                     dzielnik jest  3
15 nie jest liczbą pierwszą -                     dzielnik jest  5
15 jest liczbą pierwszą!
16 nie jest liczbą pierwszą -                     dzielnik jest  2
16 nie jest liczbą pierwszą -                     dzielnik jest  4
16 nie jest liczbą pierwszą -                     dzielnik jest  8
16 jest liczbą pierwszą!
17 jest liczbą pierwszą!
18 nie jest liczbą pierwszą -                     dzielnik jest  2
18 nie jest liczbą pierwszą -                     dzielnik jest  3
18 nie jest liczbą pierwszą -                     dzielnik jest  6
18 nie jest liczbą pierwszą -                     dzielnik jest  9
18 jest liczbą pierwszą!
19 jest liczbą pierwszą!
20 nie jest liczbą pierwszą -                     dzielnik jest  2
20 nie jest liczbą pierwszą -                     dzielnik jest  4
20 nie jest liczbą pierwszą -                     dzielnik jest  5
20 nie jest liczbą pierwszą -                     dzielnik jest 10
20 jest liczbą pierwszą!
>>> 



  
