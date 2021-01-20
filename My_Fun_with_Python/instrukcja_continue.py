# jeśli instrukcja continue będzie wykonywana w pętli, to nie będą wykonane kolejne instrukcje zawarte w pętli,
# ale po prostu sterowanie przeskoczy do warunku określającego pętlę, czyli na początek pętli

#bez continue

pracownicy = ['Rafael', 'Maria@sales.mojafirma.pl', \
              'Roy', 'Krisitina', 'Jon@mojafirma.com', 'Joanna']

domena = 'mojafirma.pl'
emails = []

for pracownik in pracownicy:
    if '@' in pracownik:
        emails.append(pracownik.lower())
    else:
        email = pracownik.lower() + '@' + domena
        emails.append(email)
        
for email in emails:
    print(email)
    
>>>
rafael@mojafirma.pl
maria@sales.mojafirma.pl
roy@mojafirma.pl
krisitina@mojafirma.pl
jon@mojafirma.com
joanna@mojafirma.pl
>>> 

pracownicy = ['Rafael', 'Maria@sales.mojafirma.pl', \
              'Roy', 'Krisitina', 'Jon@mojafirma.com', 'Joanna']

domena = 'mojafirma.pl'
emails = []

for pracownik in pracownicy:
    if '@' in pracownik:
        emails.append(pracownik.lower())
        continue
    email = pracownik.lower() + '@' + domena
    emails.append(email)

for email in emails:
    print(email)
    
>>>
rafael@mojafirma.pl
maria@sales.mojafirma.pl
roy@mojafirma.pl
krisitina@mojafirma.pl
jon@mojafirma.com
joanna@mojafirma.pl
>>> 

menu = '''
Wybiezr na co masz ochotę:
1 - KAWA
2 - HERBATA
3 - UŚMIECHNIJ SIĘ
---------------
Żeby zakończyć ten program, wybierz 0
'''
 
usmiech = '''
 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""
'''

while True:
 
    print(menu)
    wybor = input('Wprowadź twój wybór:  ')
 
    if wybor == '1':
        print("Funkcja KAWA na razie nie jest dostępna")
        input('Naciśnij enter')
        continue
    
    if wybor == '2':
        print("Funkcja HERBATA na razie nie jest dostępna")
        input('Naciśnij enter')
        continue
    
    if wybor =='3':
        print(usmiech)
        input('Naciśnij enter')        
        continue
        
    if wybor == '0':
        break
 
    input('Musisz dokonac prawidłowego wybory, spróbuj jeszcze raz od nowa!')

  >>>
  Wybiezr na co masz ochotę:
1 - KAWA
2 - HERBATA
3 - UŚMIECHNIJ SIĘ
---------------
Żeby zakończyć ten program, wybierz 0

Wprowadź twój wybór:  1
Funkcja KAWA na razie nie jest dostępna
Naciśnij enter

Wybiezr na co masz ochotę:
1 - KAWA
2 - HERBATA
3 - UŚMIECHNIJ SIĘ
---------------
Żeby zakończyć ten program, wybierz 0

Wprowadź twój wybór:  2
Funkcja HERBATA na razie nie jest dostępna
Naciśnij enter

Wybiezr na co masz ochotę:
1 - KAWA
2 - HERBATA
3 - UŚMIECHNIJ SIĘ
---------------
Żeby zakończyć ten program, wybierz 0

Wprowadź twój wybór:  
Musisz dokonac prawidłowego wybory, spróbuj jeszcze raz od nowa!

Wybiezr na co masz ochotę:
1 - KAWA
2 - HERBATA
3 - UŚMIECHNIJ SIĘ
---------------
Żeby zakończyć ten program, wybierz 0

Wprowadź twój wybór:  3

 
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
"$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
   "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
   o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
 """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
            "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
              $$$o          "$$""$$$$$$""""           o$$$
               $$$$o                                o$$$"
                "$$$$o      o$$$$$$o"$$$$o        o$$$$
                  "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
                     ""$$$$$oooo  "$$$o$$$$$$$$$"""
                        ""$$$$$$$oo $$$$$$$$$$
                                """"$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$"
                                      "$$$""""

Naciśnij enter

Wybiezr na co masz ochotę:
1 - KAWA
2 - HERBATA
3 - UŚMIECHNIJ SIĘ
---------------
Żeby zakończyć ten program, wybierz 0

Wprowadź twój wybór:  0
>>> 
