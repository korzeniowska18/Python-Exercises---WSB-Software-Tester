pracownicy = ['Rafael', 'Maria', 'Roy', 'Krisitina', 'Jon', 'Joanna']

domena = 'mojafirma.pl'

for pracownik in pracownicy:
    email = pracownik.lower() + '@' + domena
    print('Adres mailowy ', pracownik, '\tjest to', email)
else:
    print("----- Koniec listy -----")
    
>>>
Adres mailowy  Rafael 	jest to rafael@mojafirma.pl
Adres mailowy  Maria 	jest to maria@mojafirma.pl
Adres mailowy  Roy 	jest to roy@mojafirma.pl
Adres mailowy  Krisitina 	jest to krisitina@mojafirma.pl
Adres mailowy  Jon 	jest to jon@mojafirma.pl
Adres mailowy  Joanna 	jest to joanna@mojafirma.pl
----- Koniec listy -----
>>>

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for error in data:
    print(error.upper())
    
>>>
ERROR:FILE CANNOT BE OPEN
ERROR:NO FREE SPACE ON DISK
ERROR:FILE MISSING
WARNING:INTERNET CONNECTION LOST
ERROR:ACCESS DENIED
>>> 

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

for e in data:
    errors = e.split(':')
    print(errors[0].upper())
    print(errors[1])
    
>>>
ERROR
File cannot be open
ERROR
No free space on disk
ERROR
File missing
WARNING
Internet connection lost
ERROR
Access denied
>>> 
